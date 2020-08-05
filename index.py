import pandas as pd
import numpy as np
data = pd.read_csv("PreProServices/main_corp.csv", encoding="utf-8-sig")
# data = data.fillna(method="ffill")
words = list(set(data["Word"].values))
words.append("ENDPAD")
n_words = len(words);
tags = list(set(data["Tag"].values))
n_tags = len(tags);
print(words)


