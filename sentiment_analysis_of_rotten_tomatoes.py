# -*- coding: utf-8 -*-
"""
  Sentiment Analysis of Rotten Tomatoes
  @author Richard Alvarez
"""

import sys
from datetime import datetime
import pandas as pd
import seaborn as sb
import numpy as np # linear algebra
import pysbd
import tqdm
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
english_stopwords = stopwords.words('english')

rt_reviews_df = pd.read_csv("./rt_reviews.csv", encoding="ISO-8859-1")

rt_reviews_df.head()

rt_reviews_df.info()

rt_reviews_df['Freshness'].value_counts()

sb.countplot(rt_reviews_df, x='Freshness')

SID = SentimentIntensityAnalyzer()
SEG = pysbd.Segmenter(language="en", clean=True)

sentiment_scores = []
for index, row in tqdm.tqdm(rt_reviews_df.iterrows(), total=480000):
    raw_review = word_tokenize(row['Review'].lower())
    review_segmented = SEG.segment(' '.join([t for t in raw_review if t not in english_stopwords]))
    scores = []
    for segement in review_segmented:
      scores.append(SID.polarity_scores(segement))
    sentiment_scores.append(scores)

rt_reviews_df['scores'] = sentiment_scores

consistency = []
averages = []
for index, row in tqdm.tqdm(rt_reviews_df.iterrows(), total=480000):
  average = 0.0
  for score in row['scores']:
    average += score['compound']
  if average > 0 and row['Freshness'] == 'rotten':
    consistency.append(0)
  elif average < 0 and row['Freshness'] == 'fresh':
    consistency.append(0)
  else:
    consistency.append(1)
  averages.append(average)

rt_reviews_df['consistent'] = consistency
rt_reviews_df['average'] = averages

rt_reviews_df['consistent'] = rt_reviews_df['consistent'].apply(lambda x : 'Inconsistent' if x == 0 else 'Consistent')

plt = sb.countplot(rt_reviews_df['consistent'])
plt.set(xlabel='Consistency', title='Rotten Tomato review\'s consistency with sentiment analysis')

rt_reviews_df['consistent'].value_counts()

rt_reviews_con_df = rt_reviews_df[rt_reviews_df['consistent'] == 1]

plt = sb.catplot(data=rt_reviews_df, y='average', x='consistent', kind="swarm")