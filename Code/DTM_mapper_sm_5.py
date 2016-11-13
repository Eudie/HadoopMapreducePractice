#!/usr/bin/python

# Mapper to create DTM from csv as input

import sys
import re
#from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
#snowball_stemmer = SnowballStemmer('english')

WORD_RE = re.compile(r"[\w']+")
for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) != 10:
        continue

    key = data[2] + ' @ ' + data[8]
    tweet = data[1]
    for word in re.split(' |\r\n', tweet):
        if word is not None or word[0] not in ["#", "@", "<"]:
            if word[:4] != "http":
                word = word.lower()
                for FinalWord in WORD_RE.findall(word):
                    #FinalWord = snowball_stemmer.stem(FinalWord)
                    if FinalWord not in stop_words:
                        to_reducer = key + ' | ' + FinalWord
                        print "{0}\t{1}".format(to_reducer, 1)
