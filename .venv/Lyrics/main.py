#import polyglot
import stopwordsiso
import re
import os
from analysisfunctions import fileList
from analysisfunctions import wordcloudmaker
from analysisfunctions import removeStopwords
from analysisfunctions import extract_filename
from analysisfunctions import remove_punctuation_and_split
from polyglot.text import Text, WordList
from analysisfunctions import percent_unique
from analysisfunctions import average
from icu import Locale, UnicodeString
global masterwordlist





source = ("/Users/reiamulette/PycharmProjects/EM624/SYS800 Project/LyricAnalysis/.venv/Lyrics/Japan/2000")
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
list_overall_percentage_unique = []
list_overall_total_lines = []
masterwordlist = []
for filename in filepaths:
    with open(filename, 'r') as file:
        file_content = file.read()
        header_delimiter = file_content.find('*****')
        onlyfilename = extract_filename(filename)
        pnglink = str(onlyfilename) + '.png'

        if header_delimiter != -1:
            extracted_header = file_content[:header_delimiter].strip()
            bodycontent = file_content[header_delimiter:].strip()
            cleanedtext = removeStopwords(bodycontent)

            uniquepercent = percent_unique(bodycontent)
            percentage_unique, total_lines = percent_unique(bodycontent)
            list_overall_percentage_unique.append(uniquepercent[0])
            list_overall_total_lines.append(uniquepercent[1])
            body = bodycontent.split(' ')
            for word in body:
                masterwordlist.append(word)

    print(str(onlyfilename) + ': ' + str(uniquepercent[0]) + '% Unique. Total Lines:' + str(uniquepercent[1]))
    overall_percentage_unique = average(list_overall_percentage_unique)
    overall_total_lines = average(list_overall_total_lines)

#wordcloudmaker(masterwordlist,'1960.png')
print("Overall Average Percent Unique: " + str(overall_percentage_unique) + "%")
print("Overall Average Total Lines: " + str(overall_total_lines))

