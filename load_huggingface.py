from datasets import load_dataset
#data_link = "https://huggingface.co/datasets/google/fleurs/blob/main/data/cy_gb/dev.tsv"
fleurs_asr = load_dataset("google/fleurs", "cy_gb", cache_dir="./huggingface/")

print("\n👉 First item 'fleurs_asr[0]':")