import argparse
import json
from utils.tools import VQAEval, calculate_multiclass_metrics, label_regular

def parse_args():
    parser = argparse.ArgumentParser(description="Eval")

    # models
    parser.add_argument("--model-name", type=str, default="LLaVA-1.6-34B")

    # datasets
    parser.add_argument("--dataset-names", type=str, default="MMFakeBench_test")
    parser.add_argument("--log_path", type=str, default='standard_prompt')

    # result_path
    parser.add_argument("--answer_path", type=str, default="./example_outputs")

    args = parser.parse_args()
    return args


binary_label_map = {'True': 0, 'Fake': 1}
multiclass_label_map = {'original': 0, 'textual_veracity_distortion': 1, 'visual_veracity_distortion': 2, 'mismatch':3}


def main(args):
    answer_path = args.answer_path + '/' + args.model_name +  '/' + args.log_path + '/'+  args.dataset_names + '.json'

    eval = VQAEval()

    multiclass_predict_label_all  = []
    multiclass_gt_label_all = []

    bina_predict_label_all  = []
    bina_gt_label_all = []
   

    X_num = 0
    result = {}
    result_path = args.answer_path + '/' + args.model_name +  '/' + args.log_path + '/'+ 'result.json'

    with open(answer_path, 'r') as f:
            dict = json.load(f)

            for i in range(len(dict)):
                dict_item = dict[i]
                output = dict_item['answer']
                if isinstance(output, list):
                    list_num = len(output)
                    output = output[list_num-1]

                multiclass_gt_label = multiclass_label_map[dict_item["multiple_gt_answers"]]

                bina_gt_label = binary_label_map[dict_item["gt_answers"][0]]

                bina_predict_label, multiclass_predict_label = label_regular(output)

                multiclass_predict_label_all.append(multiclass_predict_label)
                multiclass_gt_label_all.append(multiclass_gt_label)

                bina_predict_label_all.append(bina_predict_label)
                bina_gt_label_all.append(bina_gt_label)


    mulple_class_metrisc= calculate_multiclass_metrics(multiclass_gt_label_all, multiclass_predict_label_all, 4)

    bina_class_metrisc= calculate_multiclass_metrics(bina_gt_label_all, bina_predict_label_all, 2)

    
    #bina
    bina_accuracy = bina_class_metrisc['accuracy']
    bina_Recall =  bina_class_metrisc['recall']
    bina_F1 = bina_class_metrisc['f1_score']
    bina_Precision = bina_class_metrisc['precision']

    result['bina_ACC'] = bina_accuracy
    result['bina_RECALL'] = bina_Recall
    result['bina_F1'] = bina_F1
    result['bina_Precision'] = bina_Precision

    # multiple_class
    accuracy_multiple_class = mulple_class_metrisc['accuracy']
    recall_multiple_class = mulple_class_metrisc['recall']
    f1_multiple_class = mulple_class_metrisc['f1_score']
    precision_multiple_class = mulple_class_metrisc['precision']

    result['mlc_ACC'] = accuracy_multiple_class
    result['mlc_RECALL'] = recall_multiple_class
    result['mcl_F1'] = f1_multiple_class
    result['mcl_precision'] = precision_multiple_class


    # save 
    with open(result_path, 'a') as f:
        json.dump(result, f, indent=4)

    # print
    print('X_label_num:%d'%X_num)

    print('bina_accuracy:%.3f' %bina_accuracy)
    print('bina_Recall:%.3f' %bina_Recall)
    print('bina_F1:%.3f' %bina_F1)
    print('bina_Precision:%.3f' %bina_Precision)

    print('multiclass_accuracy:%.3f' %accuracy_multiple_class)
    print('multiclass_Recall:%.3f' %recall_multiple_class)
    print('multiclass_F1:%.3f' %f1_multiple_class)
    print('multiclass_Precision:%.3f' %precision_multiple_class)

if __name__ == "__main__":
    args = parse_args()
    main(args)