import pandas as pd
import numpy as np
import scipy as sp
import csv
from textblob import TextBlob, Word
news = pd.read_csv('newsText.csv')

file = open("score_test.csv", "wt")

try:
    writer = csv.writer(file)
    writer.writerow(('date', 'score'))

    for row in news.itertuples():
        text = TextBlob(row.Text)
        score = text.sentiment.polarity
        dates = row.Date
        writer.writerow((dates,score))

finally:
    file.close()
