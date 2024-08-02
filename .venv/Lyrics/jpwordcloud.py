import os
import re
import stopwordsiso as stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from analysisfunctions import *
masterwordlist = []
source = "/Users/reiamulette/PycharmProjects/EM624/SYS800 Project/LyricAnalysis/.venv/Lyrics/Japan/1960"
filepaths = fileList(source)
with open('filepathstoavoid.txt', 'r') as fpavoid:
    excludeFilepath = [line.strip() for line in fpavoid]

filtered_filepaths = [filepath for filepath in filepaths if all(exclude not in filepath for exclude in excludeFilepath)]
filepaths = filtered_filepaths
finalstring = []

for filename in filepaths:
    with open(filename, 'r') as file:
        file_content = file.read()
        header_delimiter = file_content.find('*****')
        onlyfilename = extract_filename(filename)
        pnglink = str('Japanese1960') + '.png' #set name

        if header_delimiter != -1:
            extracted_header = file_content[:header_delimiter].strip()
            bodycontent = file_content[header_delimiter:].strip()
            bodystring = bodycontent.replace('\n', ' ').replace('*', '').replace(",","").replace("(","").replace(")","").replace('"',"").replace("-"," ").replace("!","").replace("...","").replace("?","")
            bodystring = bodystring.lower()
            newstring = ' '.join([word for word in bodystring.split() if len(word)>3])
            newstring = removeStopwords(newstring)
            finalstring.append(newstring)

print(finalstring)
with open("Japanese1960wordlist.txt", 'w') as file:
        file.write(str(finalstring))
#wordcloudmaker(str(finalstring), str(pnglink))