#Convert all text to lowercase
import os
import glob
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
#Get the directory
directory = r'C:\Users\Mark\Desktop\CP423 Text Retrival and Search engine\A01\data'

#retrives and sorts the the text files alphabetically 
files = glob.glob(os.path.join(directory, '*.txt'))

def lowerize(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content= file.read()
        lower_content = content.lower()
        #overwrite the file with the lowercase equivalent 
        with open(i, 'w', encoding='utf-8') as file:
            file.write(lower_content)

#Tokenize all the text using NLTK
def tokenize(input_file_path):
    with open(input_file_path, 'r', encoding = 'utf-8') as file:
        content = file.read()
        words = word_tokenize(content)
        print("words", words)
        sentences = sent_tokenize(content)
        print("sentences", sentences)

#Remove all stop words
stop_words = set(stopwords.words('english'))

def remove_stop_words(input_file_path):
    with open(input_file_path, 'r', encoding = 'utf-8') as file:
        content = file.read()
        words = word_tokenize(content)
        filtered = [word for word in words if word.lower() not in stop_words]
        filtered = ' '.join(filtered)
        with open(i, 'w', encoding = 'utf-8') as file:
            file.write(filtered)

def remove_special(input_file_path):
    with open(input_file_path, 'r', encoding = 'utf-8') as file:
        content = file.read()
        pattern = r'[^a-zA-Z0-9\s]'
        processed_text = re.sub(pattern, ' ', content)
        with open(input_file_path, 'w', encoding = 'utf-8') as file:
            file.write(processed_text)

def remove_single(input_file_path):
    """create a hashmap, create a counter for every character key pair value and then 
    then go back into the text, if the word is in the singlely word remove it"""

    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read() 
        remove_single_content = ' '.join([word for word in content.split() if len(word)>1])
        with open(input_file_path, 'w', encoding = 'utf-8') as file:
            file.write(remove_single_content)

def create_set(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content= file.read()
        lower_set = content.lower()
        words = word_tokenize(lower_set)
        content = set(words)
        return content

for i in files[:1]:
    lowerize(i)
    tokenize(i)
    remove_stop_words(i)
    remove_special(i)
    remove_single(i)
    create_set(i)
    
            