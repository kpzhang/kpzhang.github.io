import os,sys

import io,codecs

import numpy as np 
from numpy import array

from keras.preprocessing.text import one_hot
from keras.preprocessing import sequence
from keras.utils import np_utils

from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, GRU

from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder


fh = codecs.open(sys.argv[1],'r','ISO-8859-1') # Tweets.csv
lines = fh.readlines()
fh.close()
tweets = []
sentiments = []
for i in range(1,len(lines)):
	arr = lines[i].strip().split('\t')
	tid = arr[0].strip()
	s = arr[1].strip().lower()
	text = arr[2].strip()
	tweets.append(text)
	sentiments.append(s)

vocab_size = 100
encoded_tweets = [one_hot(d, vocab_size) for d in tweets]
X = np.array(encoded_tweets)

# padding
max_tweet_length = 100
X = sequence.pad_sequences(X, maxlen=max_tweet_length)

encoder = LabelEncoder()
encoder.fit(sentiments)
y = encoder.transform(sentiments)
y = np_utils.to_categorical(y)


embedding_vector_length = 64
model = Sequential()
model.add(Embedding(vocab_size,embedding_vector_length,input_length=max_tweet_length))
model.add(GRU(units=32,dropout=0.2,recurrent_dropout=0.2))
model.add(Dense(3,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

kfold = KFold(n_splits=10,shuffle=True,random_state=2020)
cvscores = []
for train, test in kfold.split(X):
	hist = model.fit(X[train],y[train],batch_size=64,epochs=10,validation_data=(X[test],y[test]),verbose=0)
	acc = hist.history['val_acc'][-1]
	cvscores.append(acc)

print("%.4f%% (+/- %.4f%%)" % (np.mean(cvscores), np.std(cvscores)))
