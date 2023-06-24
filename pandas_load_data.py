import pandas as pd

sets = ['train', 'dev', 'test']

dev_tsv = pd.read_csv("dev.tsv", sep="\t", header=None)

