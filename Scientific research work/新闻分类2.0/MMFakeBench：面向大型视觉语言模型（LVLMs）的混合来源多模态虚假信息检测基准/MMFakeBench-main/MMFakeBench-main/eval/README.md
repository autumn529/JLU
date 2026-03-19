# Evaluation Guidelines
We provide detailed instructions for evaluation. 

## Evaluation Only
If you want to use your own parsing logic and *only provide the final answer*, you can use `main_eval_only.py`.

Then run eval_only with:
```
python main_eval_only.py --answer_path ./example_outputs  --model-name LLaVA-1.6-34B  --dataset-names MMFakeBench_test  --log_path standard_prompt
```

Please refer to [example output](https://github.com/liuxuannan/MMFakeBench/tree/main/eval/example_outputs/LLaVA-1.6-34B/standard_prompt/MMFakeBench_test.json) for a detailed prediction file form.


## Reproduce the results of LLaVA
By seeting up the env for llava via following steps:

Step 1:
```init
git clone https://github.com/haotian-liu/LLaVA.git
cd LLaVA
```
In Step 2:
```
conda create -n llava python=3.10 -y
conda activate llava
pip install --upgrade pip  # enable PEP 660 support
pip install -e .
```

Then put the MMFakeBench dataset under the folder ./data, you can run llava with the following command:
```
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 nohup python run_llava.py \
--model_name llava-1.6-34b \
--dataset_name MMFakeBench_val \
--sampled-root ./data/MMFakeBench_val \
--prompt_type standard_prompt \
--model-path liuhaotian/llava-v1.6-34b
```
