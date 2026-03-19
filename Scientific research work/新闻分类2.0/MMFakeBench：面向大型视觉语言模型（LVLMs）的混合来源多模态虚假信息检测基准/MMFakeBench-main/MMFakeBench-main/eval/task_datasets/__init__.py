import json
from functools import partial
from torch.utils.data import Dataset
import sys


def ensure_ends_with_period(text):

    stripped_text = text.rstrip()
    if not stripped_text.endswith('.'):  
        return stripped_text + '.'  
    else:
        return text  

class Misinformation_Dataset(Dataset):
    def __init__(
        self,
        dataset_name,
        root='tiny_lvlm_datasets',
        prompt_type = 'direct'
    ):
        self.root = root
        self.dataset_name = dataset_name
        with open(f"{root}/source/{dataset_name}.json", 'r') as f:
            self.dataset = json.load(f)
        self.prompt_type = prompt_type
        
        if 'MMD_Agent' in prompt_type:
            self.template_text_judge = open('./prompt_template/MMD_Agent/textual_veracity_check.txt').read()
            self.template_image_judge = open('./prompt_template/MMD_Agent/visual_veracity_check.txt').read()
            self.template_consistency_judge = open('./prompt_template/MMD_Agent/cross_modal_consistency_reason.txt').read()
        elif prompt_type == 'standard_prompt':
            self.sp_template = open('./prompt_template/standard_prompt/standard_prompt.txt').read()

            
    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        sample = self.dataset[idx]
        sample['image_path'] = f"{self.root}/{sample['image_path']}"
        text = ensure_ends_with_period(f"{sample['text']}")
        if self.prompt_type == 'MMD_Agent':

            question_fix_text_check = f"{self.template_text_judge}".replace('[News caption]', text)
            question_fix_consistency_reason = f"{self.template_consistency_judge}".replace('[News caption]', text)
            sample['question_fix_text_check'] = question_fix_text_check
            sample['question_fix_image_check'] = f"{self.template_image_judge}"
            sample['question_fix_consistency_reason'] = question_fix_consistency_reason

        elif self.prompt_type == 'standard_prompt':
            sample['question'] = f"{self.sp_template}".replace('[News caption]', text)

    
        return sample


