<h1 align="center">MMFakeBench: A Mixed-Source Multimodal Misinformation Detection Benchmark for LVLMs</h1>
<h3 align="center">ICLR 2025 </h3>
<p align='center' style="text-align:center;font-size:1em;">
Xuannan Liu, Zekun Li, Peipei Li, Huaibo Huang, Shuhan Xia, Xing Cui, Linzhi Huang, Weihong Deng, Zhaofeng He
</p>


[![Project page](https://img.shields.io/badge/Project-Page-brightgreen)](https://liuxuannan.github.io/MMFakeBench.github.io/)
[![arXiv](https://img.shields.io/badge/ArXiv-2403.01988-brightgreen)](https://arxiv.org/abs/2406.08772)


This is the official code repository of the MMFakeBench dataset. 

## News

`2025/03` 🎙🎙🎙 MMFakeBench dataset is updated!

`2025/01` 🎊🎊🎊 MMFakeBench is accepted by ICLR 2025!

`2024/05` 🔥🔥🔥 We release the code and dataset of MMFakeBench!


## Data repository

You should strictly follow the data usage guidelines by filling in [Data Usage Protocol on Huggingface](https://huggingface.co/datasets/liuxuannan/MMFakeBench).

### Annotations
Each iamge-text sample in the dataset is provided with annotations. For example, the annotation of a multimodal misinformation sample with mixed-source type may look like this in the MMFakeBench_val.json/MMFakeBench_test.json file:

```
  {
    "text": "Wi-Fi is a trademark of Microsoft.",
    "image_path": "/fake/fever_AI_val_100/fever_dalle_val_1.png",
    "text_source": "Fever",
    "image_source": "AI-generated Image",
    "gt_answers": "Fake",
    "fake_cls": "textual_veracity_distortion"
  }
```

Where `text` refers to the manipulated text caption, `image_path` is the relative path to the manipulated image, `text_source` and `image_source` denote the sources of the text and image data respectively, `gt_answers` represents the binary label indicating the type of misinformation and `fake_cls` specifies the multiclass label identifying the source of the misinformation.

## Data Structure
This dataset is structured around mixed-source multimodal misinformation detection.

```
.
├── MMFakeBench_val
│   ├── source
│   │   ├── MMFakeBench_val.json
│   ├── real
│   │   ├── bbc_val_50
│   │   │   ├── BBC_val_0.png
│   │   │   ├── BBC_val_1.png
│   │   │   └── ...
│   │   ├── guardian_val_50
│   │   │   ├── guardian_val_0.png
│   │   │   ├── guardian_val_1.png
│   │   │   └── ...
│   │   ├── usa_today_val_50
│   │   │   ├── usa_today_val_0.png
│   │   │   ├── usa_today_val_1.png
│   │   │   └── ...
│   │   ├── wash_val_50
│   │   │   ├── wash_val_0.png
│   │   │   ├── wash_val_1.png
│   │   │   └── ...
│   │   ├── fakeddit_val_50
│   │   │   ├── fakeddit_val_0.png
│   │   │   ├── fakeddit_val_1.png
│   │   │   └── ...
│   │   ├── coco_val_50
│   │   │   ├── coco_val_0.png
│   │   │   ├── coco_val_1.png
│   │   │   └── ...
│   ├── fake
# textual veracity distortion
│   │   ├── fever_AI_val_100
│   │   │   ├── fever_dalle_val_1.png
│   │   │   ├── fever_val_SD_1.png
│   │   │   ├── fever_val_AI_1.png
│   │   │   └── ...
│   │   ├── politicat_match_val_50
│   │   │   ├── politicat_match_val_0.png
│   │   │   ├── politicat_match_val_1.png
│   │   │   └── ...
│   │   ├── gossipcop_match_val_25
│   │   │   ├── gossipcop_match_val_0.png
│   │   │   ├── pgossipcop_match_val_1.png
│   │   │   └── ...
│   │   ├── gossipcop_midjourney_val_25
│   │   │   ├── gossipcop_val_1.png
│   │   │   ├── gossipcop_val_2.png
│   │   │   └── ...
│   │   ├── chatgpt_match_val_50
│   │   │   ├── chatgpt_match_val_0.png
│   │   │   ├── chatgpt_match_val_1.png
│   │   │   └── ...
│   │   ├── llm_gossip_md_generation_val_10
│   │   │   ├── llm_gossip_val_1.png
│   │   │   ├── llm_gossip_val_2.png
│   │   │   └── ...
│   │   ├── llm_science_md_generation_val_10
│   │   │   ├── llm_science_val_1.png
│   │   │   ├── llm_science_val_2.png
│   │   │   └── ...
│   │   ├── llm_rewrite_val_30
│   │   │   ├── chatgpt_rewrite_md_val_1.png
│   │   │   ├── chatgpt_rewrite_dalle_val_3.png
│   │   │   └── ...
# visual veracity distortion
│   │   ├── Fakeddit_photo_edit_val_50
│   │   │   ├── Fakeddit_photo_edit_val_0.png
│   │   │   ├── Fakeddit_photo_edit_val_1.png
│   │   │   └── ...
│   │   ├── antifact_image_generation_val_50
│   │   │   ├── coco_antifact_val_1.png
│   │   │   ├── coco_antifact_val_2.png
│   │   │   └── ...
# cross-modal consistency distortion
│   │   ├── Newsclipings_person_val_50
│   │   │   ├── Newsclipings_person_val_0.png
│   │   │   ├── Newsclipings_person_val_1.png
│   │   │   └── ...
│   │   ├── Newsclipings_scene_val_50
│   │   │   ├── Newsclipings_scene_val_0.png
│   │   │   ├── Newsclipings_scene_val_1.png
│   │   │   └── ...
│   │   ├── Newsclipings_semantic_val_50
│   │   │   ├── Newsclipings_semantic_val_0.png
│   │   │   ├── Newsclipings_semantic_val_1.png
│   │   │   └── ...
│   │   ├── DGM4_text_edit_senti_val_50
│   │   │   ├── DGM4_text_edit_senti_val_0.png
│   │   │   ├── DGM4_text_edit_senti_val_1.png
│   │   │   └── ...
│   │   ├── coco_text_edit_val_50
│   │   │   ├── coco_text_edit_val_0.png
│   │   │   ├── coco_text_edit_val_1.png
│   │   │   └── ...
│   │   ├── coco_text_edit_val_50
│   │   │   ├── coco_image_edit_val_0.png
│   │   │   ├── coco_image_edit_val_1.png
│   │   │   └── ...
```


## License
This dataset is under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.


# Citation:
If you found MMFakeBench useful in your research or applications, please kindly cite using the following BibTeX:
```
@inproceedings{liu2024mmfakebench,
  title={MMFakeBench: A Mixed-Source Multimodal Misinformation Detection Benchmark for LVLMs},
  author={Liu, Xuannan and Li, Zekun and Li, Peipei and Huang, Huaibo and Xia, Shuhan and Cui, Xing and Huang, Linzhi and Deng, Weihong and He, Zhaofeng},
  booktitle={ICLR},
  year={2025}
}
```
