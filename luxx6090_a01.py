#Convert all text to lowercase
import os
import glob
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
#Get the directory
directory = r'C:\Users\Mark\Desktop\CP423 Text Retrival and Search engine\A01\data'

#retrives and sorts the the text files alphabetically 
files = glob.glob(os.path.join(directory, '*.txt'))

#for the files in the files path
for i in files[:2]:
    print(i)
    #read the text n the file, get that content, lower it then put it in a variable
    with open(i, 'r', encoding='utf-8') as file:
        content= file.read()
        lower_content = content.lower()
        #overwrite the file with the lowercase equivalent 
        with open(i, 'w', encoding='utf-8') as file:
            file.write(lower_content)


#Tokenize all the text using NLTK
for i in files[:1]:
    print(i)
    with open(i, 'r', encoding = 'utf-8') as file:
        content = file.read()
        words = word_tokenize(content)
        print("words", words)
        sentences = sent_tokenize(content)
        print("sentences", sentences)

#Remove all stop words
stop_words = set(stopwords.words('english'))
for i in files[:1]:
    print(i)
    with open(i, 'r', encoding = 'utf-8') as file:
        content = file.read()
        filtered = [word for word in words if word.lower() not in stop_words]
        filtered = ' '.join(filtered)
        with open(i, 'w', encoding = 'utf-8') as file:
            file.write(filtered)


def remove_special(input_text):
    pattern = r'[^a-zA-Z0-9\s]'
    processed_text = re.sub(pattern, ' ', input_text)
    return processed_text

for i in files[:1]:
    print(i)
    with open(i, 'r', encoding = 'utf-8') as file:
        file_content = file.read()
        cleaned = remove_special(file_content)
        with open(i, 'w', encoding= 'utf-8') as file:
            file.write(cleaned)
