import os,sys
import io,codecs

import re
import numpy as np

from keras.preprocessing.text import one_hot
from keras.preprocessing import sequence

from sklearn import svm
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression



fh = codecs.open(sys.argv[1],'r','ISO-8859-1') # Tweets.csv
lines = fh.readlines()
fh.close()
tweets = []
y = []
for i in range(1,len(lines)):
	arr = lines[i].strip().split('\t')
	tid = arr[0].strip()
	s = arr[1].strip().lower()
	sentiment = 0
	if s == 'positive':
		sentiment = 1
	elif s == 'negative':
		sentiment = 2
	text = arr[2].strip()
	tweets.append(text)
	y.append(sentiment)

vocab_size = 100
encoded_tweets = [one_hot(d, vocab_size) for d in tweets]
X = np.array(encoded_tweets)

# padding
max_tweet_length = 100
X = sequence.pad_sequences(X, maxlen=max_tweet_length)
y = np.array(y)

# classify, with n-fold cross validation
cvscores = []
kfold = KFold(n_splits=10,shuffle=True,random_state=2020)

model = svm.SVC()
model = LogisticRegression(random_state=2020)
for train, test in kfold.split(X):
	model.fit(X[train],y[train])
	acc = model.score(X[test],y[test])

	cvscores.append(acc)

print("%.5f%% (+/- %.5f%%)" % (np.mean(cvscores), np.std(cvscores)))
