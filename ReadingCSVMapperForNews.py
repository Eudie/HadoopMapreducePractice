#!/usr/bin/python

# Mapper to create DTM from csv as input

import sys
import io
import re
import csv
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
snowball_stemmer = SnowballStemmer('english')

WORD_RE = re.compile(r"[\w']+")
for line in csv.reader(io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='replace')):
    data = line
    key = data[1]
    news = data[9]
    for word in re.split(' |\r\n', news):
        if word is not None or word[0] not in ["#", "@"]:
            if word[:4] != "http":
                word = word.lower()
                for FinalWord in WORD_RE.findall(word):
                    FinalWord = snowball_stemmer.stem(FinalWord)
                    if FinalWord not in stop_words:
                        print("{0}\t{1}".format(key, FinalWord))
