CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python run_llava.py --model_name llava-1.6-34b --dataset_name MMFakeBench_val --sampled-root ./data/MMFakeBench_val  --prompt_type standard_prompt  --model-path ./lvlm_pretrained_ckpt/llava-v1.6-34b

