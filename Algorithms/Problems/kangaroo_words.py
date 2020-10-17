"""
Kangaroo words - from Peak6

"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findKangarooScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY words
#  2. STRING_ARRAY wordsToSynonyms
#  3. STRING_ARRAY wordsToAntonyms
#
import math

# Note: This is an incomplete greedy solution
# Need to use DP with backtracking to assert non-consecutive subsequence
def findJoey(word, joey):
    # Search for joey as subset (in order) of word
    word_index = word.find(joey[0])
    if word_index < 0: # check first char
        return False

    # Iterate through chars
    joey_index = 1
    consecutive_joey = True # Flag

    while joey_index < len(joey):
        word_index += 1 # inc word pointer
        if word_index >= len(word): # check bounds
            return False
        # compare chars
        if word[word_index] == joey[joey_index]:
            joey_index += 1
        else:
            consecutive_joey = False

    # print(word, word_index, joey, joey_index, consecutive_joey)
    return not consecutive_joey

def findKangarooScore(words, wordsToSynonyms, wordsToAntonyms):
    # 1) Parse input into DS (case INSENSITIVE)
    syns_of = {} # Contains synonyms of key word
    for entry in wordsToSynonyms:
        word, syn_entry = entry.split(":")
        syns = [s.lower() for s in syn_entry.split(",")]
        syns_of[word.lower()] = syns
    ants_of = {} # Contains antonyms of key word
    for entry in wordsToAntonyms:
        word, ant_entry = entry.split(":")
        ants = [a.lower() for a in ant_entry.split(",")]
        ants_of[word.lower()] = ants

    # dict joey_words where key = joey, value = list of words that contain joey
    kangaroos_of = {}
    score = 0  # Running total of scores

    # 2) Find kangaroo & anti-kangaroo words
    for word in words:
        word = word.lower()
        # Check all synonyms of word
        if word in syns_of:
            for syn in syns_of[word]:
                if findJoey(word, syn):
                    score += 1 # Add points for syn joeys
                    kangaroos_of.setdefault(syn, [])
                    kangaroos_of[syn].append(word) # add to kangaroo dict

        # Check all antonyms of word
        if word in ants_of:
            for ant in ants_of[word]:
                if findJoey(word, ant):
                    score -= 1 # Subtract points for ant joeys

    # print(kangaroos_of)
    # 3) Find kangaroo cousin pairs & calculate points
    for joey, kangaroos in kangaroos_of.items():
        # Caculate number of cousin pairs
        score += math.floor(math.factorial(len(kangaroos))/2)

    return score

if __name__ == '__main__':
