import csv
from textblob import TextBlob
import pandas as pd 
import numpy as np 

# Import csv file
infile = '/Users/subfolder/keywords.csv'
bloblist = list() 

# Open file
with open(infile, 'r') as csvfile:
    rows = csv.reader(csvfile)

    for row in rows:
        sentence = row[0]
        blob = TextBlob(sentence)
        blob.correct()
        bloblist.append((blob.sentiment.polarity, blob.tags))
        
# Add headers and append output
df = pd.DataFrame(bloblist, columns = ['polarity', 'tags'])

# print to CSV
df.to_csv('output35.csv')
