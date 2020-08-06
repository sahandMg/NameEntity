import pandas as pd
import numpy as np
from Classes import SentenceGetter as sg
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.models import Model, Input
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
from keras_contrib.layers import CRF


# read_file = pd.read_excel (r'PreProServices/ner.xlsx')
# read_file.to_csv (r'PreProServices/ner2.csv', index = None, header=True,encoding='utf-8-sig')
data = pd.read_csv("PreProServices/feili300.csv" , encoding='utf-8-sig')
data = data.fillna(method="ffill")
# print(data.tail(10)['Word'])
words = list(set(data["Word"].values))
words.append("ENDPAD")
n_words = len(words)
tags = list(set(data["Tag"].values))
n_tags = len(tags)
sgc = sg.SentenceGetter(data)
sent = sgc.get_next()
sentences = sgc.sentences
max_len = 75
word2idx = {w: i + 1 for i, w in enumerate(words)}
tag2idx = {t: i for i, t in enumerate(tags)}
X = [[word2idx[w[0]] for w in s] for s in sentences]
X = pad_sequences(maxlen=max_len, sequences=X, padding="post", value=0)

y = [[tag2idx[w[1]] for w in s] for s in sentences]


y = pad_sequences(maxlen=max_len, sequences=y, padding="post", value=tag2idx["O"])
y = [to_categorical(i, num_classes=n_tags) for i in y]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.1)

input = Input(shape=(max_len,))
model = Embedding(input_dim=n_words + 1, output_dim=20,
                  input_length=max_len, mask_zero=True)(input)  # 20-dim embedding
model = Bidirectional(LSTM(units=50, return_sequences=True,
                           recurrent_dropout=0.1))(model)  # variational biLSTM
model = TimeDistributed(Dense(50, activation="relu"))(model)  # a dense layer as suggested by neuralNer
crf = CRF(n_tags)  # CRF layer
out = crf(model)  # output

model = Model(input, out)
model.compile(optimizer="rmsprop", loss=crf.loss_function, metrics=[crf.accuracy])
model.summary()





