#!/usr/bin/python

# Reducer to create DTM from csv as input
import sys

Total = 0
oldWord = None

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    ID, tweetWord = data_mapped
    NewWord = ID + ' | ' + tweetWord
    if oldWord and oldWord != NewWord:
        print oldWord, '\t', Total
        oldWord = NewWord
        Total = 0

    oldWord = NewWord
    Total += 1

if oldWord is not None:
    print oldWord, '\t', Total
