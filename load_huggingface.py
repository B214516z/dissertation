from datasets import load_dataset
data_link = "https://huggingface.co/datasets/google/fleurs/tree/main/data/cy_gb"
dataset = load_dataset("text", data_files=data_link, cache_dir="./huggingface/")
