import os
import re
from adjustheader import adjustheader

source = "/Users/reiamulette/PycharmProjects/EM624/SYS800 Project/LyricAnalysis/.venv/Lyrics"

def fileList(source):
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            if filename.endswith(('.txt')):
                matches.append(os.path.join(root, filename))
    return matches

def removeStopwords(text): #clean text
    text = remove_punctuation_and_split(text)  # remove punctuation
    text1 = [word for word in text.split() if len(word) > 3]  # remove words less than 3 letters long.
    stopword_list = open("stopwords_en.txt", encoding='utf8').read().splitlines()
    removeadditionalstopword = ['said','generally','have','that','which','where', 'would', 'told', 'their', 'from', 'such', 'using']
    cleanedtext = [word for word in text1 if word not in stopword_list]  # remove common words using stopwords
    cleanedtext = [word for word in text1 if word not in removeadditionalstopword] #remove additional stop word
    cleanedtext = [item for item in cleanedtext if item.isalpha()]  # remove numbers
    cleanedtext = [item.lower() for item in cleanedtext]#make everything lowercase
    cleanedtext = ' '.join(cleanedtext)
    return cleanedtext



filepaths = fileList(source)
excludeFilepath = []
with open('filepathstoavoid.txt', 'r') as fpavoid:
    excludeFilepath = [line.strip() for line in fpavoid]

filtered_filepaths = [filepath for filepath in filepaths if all(exclude not in filepath for exclude in excludeFilepath)]
filepaths = filtered_filepaths

with open('filestoavoid.txt', 'r') as favoid:
    avoidFiles = [line.strip() for line in favoid]

for filename in filepaths:
    if filename in avoidFiles:
        print("\nAvoided File:" + filename + "\n")
        filepaths.remove(filename)

for filename in filepaths:
    with open(filename, 'r') as file:

        old_pattern = r'^(?P<Artist>[^-]+) - (?P<SongTitle>[^(]+) \((?P<Year>\d{4})\)\\\\(?P<Category>.+)$'
        '''new_pattern = [
            r'^Artist:\s*(?P<Artist>.+)$',
            r'^Song Title:\s*(?P<SongTitle>.+)$',
            r'^Year:\s*(?P<Year>\d{4})$',
            r'^Category:\s*(?P<Category>.+)$'
            
        ]
        '''
        adjustheader(file_content, filename, old_pattern)

