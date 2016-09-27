# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 10:06:42 2016

@author: 21163
"""

from mrjob.job import MRJob
import re
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
 
WORD_RE = re.compile(r"[\w']+")
snowball_stemmer = SnowballStemmer('english')
class MRWordFreqCount(MRJob):
 
    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            IntWord = word.lower()
            ExtWord = snowball_stemmer.stem(IntWord)
            if ExtWord not in stop_words:
                yield (ExtWord, 1)
 
    def combiner(self, word, counts):
        yield (word, sum(counts))
 
    def reducer(self, word, counts):
        yield (word, sum(counts))
 
if __name__ == '__main__':
    MRWordFreqCount.run()
