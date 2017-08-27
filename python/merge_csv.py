import csv
import sys
import os
import re
import pandas as pd


# read all csv files in current directory
patternF  = '.*\.csv'
allFiles = next(os.walk('.'))[2]

matchF = re.search(patternF, allFile)
	if matchF:
		csvFiles = matchF.group()
fileList = [];

for x in csvFiles:
	fileList.append(x)

f = open('merge.csv','wt')
writer = csv.writer(f)
writer.writerow( ('date', 'text') )

for file in fileList:
	df = pd.read_csv(file)
    for data in df.itertuples():
        writer.writerow((str(data.Date),str(data.Text)))
f.close()
