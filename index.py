import pandas as pd
import numpy as np
from Classes import SentenceGetter as sg
from keras.preprocessing.sequence import pad_sequences

sgc = sg.SentenceGetter
data = pd.read_csv("PreProServices/main_corp.csv", encoding="utf-8-sig")
data = data.fillna(method="ffill")
words = list(set(data["Word"].values))
words.append("ENDPAD")
n_words = len(words)
tags = list(set(data["Tag"].values))
n_tags = len(tags)
max_len = 75
word2idx = {w: i + 1 for i, w in enumerate(words)}
tag2idx = {t: i for i, t in enumerate(tags)}
X = []
for word in words:
    X.append(word2idx[word])
print(X)




