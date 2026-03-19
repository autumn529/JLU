import os
import json
from tqdm import tqdm
from torch.utils.data import DataLoader
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report
import numpy as np

from .tools import VQAEval
from .data_utils import get_image
from .model_utils import call_llava_engine_df
from .wiki_search import search_wiki_knowledge
import torch


fake_type = ['textual_veracity_distortion', 'visual_veracity_distortion', 'mismatch','original']

def clean_data(answer):

    answer = answer.replace("\n", " ")
    answer = answer.replace("\t", " ")
    answer = answer.strip()
    return answer

def evaluate_VQA_MMD_Agent(
    model,
    dataset,
    tokenizer,
    vis_processors,
    args,
    dataset_name,
    time,
    batch_size=1,
    answer_path='./answers'
):
    predictions=[]
    dataloader = DataLoader(dataset, batch_size=batch_size, collate_fn=lambda batch: {key: [dict[key] for dict in batch] for key in batch[0]})
    eval = VQAEval()
    for batch in tqdm(dataloader, desc="Running inference"):
        question_all = []
        answer_all = []
        for image_path, question_fix_text_check, question_fix_image_check, question_fix_consistency_reason, gt_answer, multiple_gt_answers in zip(batch['image_path'], batch['question_fix_text_check'], batch['question_fix_image_check'], batch['question_fix_consistency_reason'], batch['gt_answers'], batch['fake_cls']):
            answer_dict={'gt_answers': gt_answer, 'image_path': image_path, 'model_name': args.model_name, 'multiple_gt_answers': multiple_gt_answers}
            for i in range(3):
                if i == 0:

                    text_check_action_1 = question_fix_text_check.split('Action 1:')[0].strip() + "Please answer in the form: 'Finish: [key entity noun].'"
                    
                    # action_1
                    image_sizes, images_tensor = get_image(image_path, model,vis_processors)
                    output = call_llava_engine_df(args, text_check_action_1, model, images_tensor, image_sizes, tokenizer)

                    key_entity, wiki_knowledge = search_wiki_knowledge(output)
                    text_check_action_2 = question_fix_text_check.split('[Analysis]')[0].strip()

                    #incorporating key entity and wiki knowledge
                    text_check_action_2 = text_check_action_2.replace('[key entity noun]',key_entity)
                    text_check_action_2 = text_check_action_2.replace('[External Knowledge]',wiki_knowledge)

                    # action_2
                    output = call_llava_engine_df(args, text_check_action_2, model, images_tensor, image_sizes, tokenizer)

                    if "Analysis:" in output:
                        output = output.split('Analysis:')[1]
                    analysis = clean_data(output)
                    
                    #incorporating analysis
                    text_check_action_3 = question_fix_text_check.replace('[key entity noun]',key_entity)
                    text_check_action_3 = text_check_action_3.replace('[External Knowledge]',wiki_knowledge)
                    text_check_action_3 = text_check_action_3.replace('[Analysis]', analysis)

                    question_all.append(text_check_action_3)

                     # action_3
                    output = call_llava_engine_df(args, text_check_action_3, model, images_tensor, image_sizes, tokenizer)
                    answer_all.append(output)
                    torch.cuda.empty_cache()

                    output_first_line = (output.split('\n')[0]).split('.')[0]
                    if eval.evaluate(output_first_line, 'TEXT REFUTES'):
                                    answer_dict['binary_fake_type'] = 'Fake'
                                    answer_dict['fake_type'] = fake_type[i]
                                    answer_dict['question'] = question_all
                                    answer_dict['answer'] = answer_all
                                    predictions.append(answer_dict)
                                    break

                elif i ==1:
                    
                    image_sizes, images_tensor = get_image(image_path, model,vis_processors)

                     # action_1
                    visual_check_action_1 = question_fix_image_check.split('Observation:')[0].strip()

                    output = call_llava_engine_df(args, visual_check_action_1, model, images_tensor, image_sizes, tokenizer)

                    if "Thought 2" in output:
                        output = output.split('Thought 2')[0]
                    output = clean_data(output)
                    img_descrip = output

                    # incorporating fact_conflicting content

                    visual_check_action_2 = question_fix_image_check.replace('[Fact-conflicting Description]', img_descrip)

                     # action_2
                    output = call_llava_engine_df(args, visual_check_action_2, model, images_tensor, image_sizes, tokenizer)
                    
                    question_all.append(visual_check_action_2)
                    answer_all.append(output)
                    torch.cuda.empty_cache()

                    output_first_line = (output.split('\n')[0]).split('.')[0]
                    if eval.evaluate(output_first_line, 'IMAGE REFUTES'):
                        answer_dict['binary_fake_type'] = 'Fake'
                        answer_dict['fake_type'] = fake_type[i]
                        answer_dict['question'] = question_all
                        answer_dict['answer'] = answer_all
                        predictions.append(answer_dict)
                        break
                
                else:
                    img_descrip = img_descrip.split('. ')[0]
                    image_sizes, images_tensor = get_image(image_path, model,vis_processors)

                    # action 1
                    consistency_check_action_1 = question_fix_consistency_reason.replace('[image content description]', img_descrip)
                    output = call_llava_engine_df(args, consistency_check_action_1, model, images_tensor, image_sizes, tokenizer)

                   
                    question_all.append(consistency_check_action_1)
                    answer_all.append(output)
                    torch.cuda.empty_cache()

                    output_first_line = (output.split('\n')[0]).split('.')[0]
                    if eval.evaluate(output_first_line, 'mismatch'):
                        answer_dict['binary_fake_type'] = 'Fake'
                        answer_dict['fake_type'] = fake_type[i]
                        answer_dict['question'] = question_all
                        answer_dict['answer'] = answer_all
                        predictions.append(answer_dict)
                        break

                    elif i==2:
                        answer_dict['binary_fake_type'] = 'True'
                        answer_dict['fake_type'] = fake_type[3]
                        answer_dict['question'] = question_all
                        answer_dict['answer'] = answer_all
                        predictions.append(answer_dict)

    
    answer_path = os.path.join(args.answer_path,args.model_name)
    answer_dir = os.path.join(answer_path, time)
    os.makedirs(answer_dir, exist_ok=True)
    answer_path = os.path.join(answer_dir, f"{dataset_name}.json")

    with open(answer_path, "w") as f:
        f.write(json.dumps(predictions, indent=4))
 


def evaluate_VQA(
    model,
    dataset,
    tokenizer,
    vis_processors,
    args,
    dataset_name,
    time,
    batch_size=1,
    answer_path='./answers'
):
    predictions=[]
    dataloader = DataLoader(dataset, batch_size=batch_size, collate_fn=lambda batch: {key: [dict[key] for dict in batch] for key in batch[0]})

    for batch in tqdm(dataloader, desc="Running inference"):

        for image_path, question, gt_answer, multiple_gt_answers in zip(batch['image_path'], batch['question'], batch['gt_answers'], batch['fake_cls']):
            image_sizes, images_tensor = get_image(image_path, model,vis_processors)
            output = call_llava_engine_df(args, question, model, images_tensor, image_sizes, tokenizer)
            
            answer_dict={'question': question, 'answer': output,
            'gt_answers': gt_answer, 'image_path': image_path,
            'model_name': args.model_name, 'multiple_gt_answers': multiple_gt_answers}
            predictions.append(answer_dict)
    
    answer_path = os.path.join(args.answer_path,args.model_name)
    answer_dir = os.path.join(answer_path, time)
    os.makedirs(answer_dir, exist_ok=True)
    answer_path = os.path.join(answer_dir, f"{dataset_name}.json")

    with open(answer_path, "w") as f:
        f.write(json.dumps(predictions, indent=4))

