#!/usr/bin/python

# Mapper to create DTM from csv as input

import sys
import csv
import re
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
snowball_stemmer = SnowballStemmer('english')

WORD_RE = re.compile(r"[\w']+")
for line in csv.reader(sys.stdin, delimiter = ','):
    data = line
    key = data[1]+data[4]
    tweet = data[2]
    for word in re.split(' |\r\n', tweet):
        #word = word.tolower()
        if word[0] not in ["#","@","<"]:
            if word[:4] != "http":
                word = word.lower()
                for FinalWord in WORD_RE.findall(word):
                    FinalWord = snowball_stemmer.stem(FinalWord)
                    if FinalWord not in stop_words:
                        print "{0}\t{1}".format(key, FinalWord)
