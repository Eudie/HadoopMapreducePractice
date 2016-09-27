# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:07:39 2016

@author: 21163
"""

from mrjob.job import MRJob
#import re
import sys
import csv
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


#WORD_RE = re.compile(r"[\w']+")
snowball_stemmer = SnowballStemmer('english')
class MRWordFreqCount(MRJob):
 
    def mapper(self, _, line):
        fullLine = csv.reader(iter(sys.stdin.readline, ''))
        for word in fullLine: 
            #IntWord = word.lower()
            #ExtWord = snowball_stemmer.stem(IntWord)
            #if word not in stop_words:
            yield (word, 1)
 
    def combiner(self, word, counts):
        yield (word, sum(counts))
 
    def reducer(self, word, counts):
        yield (word, sum(counts))
 
if __name__ == '__main__':
    MRWordFreqCount.run()