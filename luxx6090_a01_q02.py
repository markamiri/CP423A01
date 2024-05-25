#create doc id
import os
import glob
import nltk
from collections import defaultdict
from luxx6090_a01 import lowerize, remove_single, remove_special, remove_stop_words, tokenize, create_set
import re
directory = r'C:\Users\Mark\Desktop\CP423 Text Retrival and Search engine\A01\data'

files = glob.glob(os.path.join(directory, '*.txt'))

inverted_index = defaultdict(list)

doc_id_name = {}

file_counter = 1

for file_name in files[:2]:
    lowerize(file_name)
    tokenize(file_name)
    remove_stop_words(file_name)
    remove_special(file_name)
    remove_single(file_name)
    word_set = create_set(file_name)

    for word in word_set:
        word = str(word)
        if word in inverted_index:
            inverted_index[word].append(file_counter)
        else:
            inverted_index[word] = [file_counter]
    doc_id_name[file_counter] = file_name
    file_counter+=1

print("\nInverted Index:")
for word, i in inverted_index.items():
    print(f"{word}:{i} ")

print("\n Document ID")
for doc_id, doc_names in doc_id_name.items():
    print(f"{doc_id}:{doc_names}")

#Stop words in the second file is not removed 
#GIGA CHAD BIN 13chil is written in the 100west file, issue with output 