import argparse
import torch
import tqdm

from llava.constants import (
    IMAGE_TOKEN_INDEX,
    DEFAULT_IMAGE_TOKEN,
    DEFAULT_IM_START_TOKEN,
    DEFAULT_IM_END_TOKEN,
    IMAGE_PLACEHOLDER,
)
from llava.conversation import conv_templates, SeparatorStyle
from llava.model.builder import load_pretrained_model
from llava.utils import disable_torch_init
from llava.mm_utils import (
    process_images,
    tokenizer_image_token,
    get_model_name_from_path,
)

from PIL import Image

import requests
from PIL import Image
from io import BytesIO
import re
from task_datasets import Misinformation_Dataset

from torch.utils.data import DataLoader


import random
import numpy as np
import sys
import os
import datetime
import json
from utils.vqa import evaluate_VQA, evaluate_VQA_MMD_Agent


def image_parser(args):
    out = args.image_file.split(args.sep)
    return out


def load_image(image_file):
    if image_file.startswith("http") or image_file.startswith("https"):
        response = requests.get(image_file)
        image = Image.open(BytesIO(response.content)).convert("RGB")
    else:
        image = Image.open(image_file).convert("RGB")
    return image


def load_images(image_files):
    out = []
    for image_file in image_files:
        image = load_image(image_file)
        out.append(image)
    return out

def set_seed(seed_value):
    """
    Set the seed for PyTorch (both CPU and CUDA), Python, and NumPy for reproducible results.

    :param seed_value: An integer value to be used as the seed.
    """
    torch.manual_seed(seed_value)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed_value)
        torch.cuda.manual_seed_all(seed_value)  # For multi-GPU setups
    random.seed(seed_value)
    np.random.seed(seed_value)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def eval_model(args):
    # Model
    disable_torch_init()

    dataset_name = args.dataset_name
    dataset = Misinformation_Dataset(dataset_name, root=args.sampled_root, prompt_type=args.prompt_type)

    model_name = get_model_name_from_path(args.model_path)
    tokenizer, model, vis_processors, _ = load_pretrained_model(args.model_path, None,
                                                                model_name)
    

    if "llama-2" in model_name.lower():
        conv_mode = "llava_llama_2"
    elif "mistral" in model_name.lower():
        conv_mode = "mistral_instruct"
    elif "v1.6-34b" in model_name.lower():
        conv_mode = "chatml_direct"
    elif "v1" in model_name.lower():
        conv_mode = "llava_v1"
    elif "mpt" in model_name.lower():
        conv_mode = "mpt"
    else:
        conv_mode = "llava_v0"

    if args.conv_mode is not None and conv_mode != args.conv_mode:
        print(
            "[WARNING] the auto inferred conversation mode is {}, while `--conv-mode` is {}, using {}".format(
                conv_mode, args.conv_mode, args.conv_mode
            )
        )
    else:
        args.conv_mode = conv_mode


    set_seed(args.seed)

    print('llava_initializing...')
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_' + args.prompt_type
    if args.prompt_type == 'standard_prompt':
        evaluate_VQA(model, dataset, tokenizer, vis_processors, args, args.dataset_name, time)
    elif args.prompt_type == 'MMD_Agent':
        evaluate_VQA_MMD_Agent(model, dataset, tokenizer, vis_processors, args, args.dataset_name, time)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, default="./lvlm_pretrained_ckpt/llava-v1.6-vicuna-7b")
    parser.add_argument("--model-base", type=str, default=None)
    parser.add_argument("--conv-mode", type=str, default=None)
    parser.add_argument("--sep", type=str, default=",")
    parser.add_argument("--temperature", type=float, default=0)
    parser.add_argument("--top_p", type=float, default=None)
    parser.add_argument("--num_beams", type=int, default=1)
    parser.add_argument("--max_new_tokens", type=int, default=512)
    parser.add_argument("--sampled-root", type=str, default='./data/MMFakeBench_val')
    parser.add_argument("--prompt_type", type=str, default="standard_prompt", choices=["standard_prompt", "MMD_Agent"])
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--model_name', type=str, default='llava-1.6-7b')
    parser.add_argument('--answer_path', type=str, default='./answers')
    parser.add_argument('--dataset_name', type=str, default='MMFakeBench_val')


    args = parser.parse_args()

    eval_model(args)
