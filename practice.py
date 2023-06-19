from datasets import load_dataset
#data_link = "https://huggingface.co/datasets/google/fleurs/blob/main/data/cy_gb/dev.tsv"
fleurs_asr = load_dataset("google/fleurs", "cy_gb", cache_dir="./huggingface/")

print(fleurs_asr)

audio_input = fleurs_asr["train"][0]["audio"]
print(audio_input)