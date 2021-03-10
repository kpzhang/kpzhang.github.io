import os,sys

import pandas as pd 
import numpy as np 

import re
from nltk.tokenize import word_tokenize

from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors

from scipy import spatial


df = pd.read_csv('brown.csv',header=0,usecols=['tokenized_text'])
docs = df.values 
#df.sample(10)

# preprocess the text and generate corpus
import re
from nltk.tokenize import word_tokenize

corpus = []

for doc in docs:
  doc = ' '.join(doc.tolist()).lower()
  doc.replace('\n', ' ')
  doc = re.sub('[^a-z ]+', '', doc)
  corpus.append([w for w in doc.split() if w != ''])

#print(corpus[:5])

google_wv = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin',binary=True, encoding='utf8')

# update the vocab with our own text
model = Word2Vec(size=300, min_count=1, iter=10)
model.build_vocab(corpus)
training_samples_count = model.corpus_count
model.build_vocab([list(google_wv.vocab.keys())],update=True)
model.intersect_word2vec_format('GoogleNews-vectors-negative300.bin',binary=True,lockf=1.0)

# train the model
model.train(corpus,total_examples=training_samples_count,epochs=model.iter)

# save the model
model.save('w2v_model')
model.wv.save('w2v_model_vectors')


# load the trained model to save time
model = Word2Vec.load('w2v_model')

vocabs = list(model.wv.vocab.keys())
vectors = model[vocabs]

# find the top N similar words to a given focal word
word1 = sys.argv[1] # for example 'question'
n = int(sys.argv[2]) # top n

idx = vocabs.index(word1)
vec1 = list(vectors[idx,:])

top_n_words = ['']*n
top_n_sim = np.zeros(n)
for i in range(len(vocabs)):
  if i == idx:
    continue
  word2 = vocabs[i]
  vec2 = list(vectors[i,:])
  sim_score = 1 - spatial.distance.cosine(vec1,vec2)

  # if the similarity score of the current word is greater than the min score, 
  # replace that word with the current word
  min_idx = np.argmin(top_n_sim)
  min_score = top_n_sim[min_idx]
  if sim_score > min_score:
    top_n_sim[min_idx] = sim_score
    top_n_words[min_idx] = word2

# print out results
for w,s in zip(top_n_words,list(top_n_sim)):
  print(w,',',s)