import polyglot
import stopwordsiso as stopwords
import re
from wordcloud import WordCloud
import os
import matplotlib.pyplot as plt


def fileList(source):
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            if filename.endswith(('.txt')):
                matches.append(os.path.join(root, filename))
    return matches

def wordcloudmaker(text, url):  # make wordcloud
    wc = WordCloud(width=800, height=800,
                   background_color='white', collocations=False).generate_from_text(text)  # set wc parameters
    wc.to_file(url)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

def remove_punctuation_and_split(text):  # remove punctuation besides - between words
    punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=', '>', '?',
                   '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '»', '«', '“', '”', '\n']
    punct_pattern = re.compile("[" + re.escape("".join(
        punctuation)) + "]")  # referenced: https://stackoverflow.com/questions/18429143/strip-punctuation-with-regex-python
    text = re.sub(punct_pattern, "", text)
    return text

def extract_filename(filepath):
    filepath_pattern = r'\/?([^\/]+?)(?:\.[^\.\/]+)?$'
    match = re.search(filepath_pattern, filepath)
    if match:
        return match.group(1)
    else:
        return None

def removeStopwords(text): #clean text
    text = remove_punctuation_and_split(text)  # remove punctuation
    text1 = [word for word in text.split() if len(word) > 3]  # remove words less than 3 letters long.
    #stopword_list = open("stopwords_en.txt", encoding='utf8').read().splitlines()
    stopword_list = stopwords.stopwords("jp")  # Change language of stopwords
    #removeadditionalstopword = ['said','generally','have','that','which','where', 'would', 'told', 'their', 'from', 'such', 'using', 'make']
    removeadditionalstopword = ['を']
    cleanedtext = [word for word in text1 if word not in stopword_list]  # remove common words using stopwords
    cleanedtext = [word for word in text1 if word not in removeadditionalstopword] #remove additional stop word
    cleanedtext = [item for item in cleanedtext if item.isalpha()]  # remove numbers
    cleanedtext = [item.lower() for item in cleanedtext]#make everything lowercase
    cleanedtext = ' '.join(cleanedtext)
    return cleanedtext


def percent_unique(content):
    unique_lines = set()
    total_lines = 0

    if isinstance(content, str):
        content = content.splitlines()

    for line in content:
        clean_line = line.strip()  # Remove leading/trailing whitespace and newline characters
        unique_lines.add(clean_line)
        total_lines += 1
    unique_line_count = len(unique_lines)
    percentage_unique = (unique_line_count / total_lines) * 100 if total_lines > 0 else 0
    percentage_unique = round(percentage_unique,2)
    return percentage_unique, total_lines

def average(numbers):
    total = 0
    for num in numbers:
        total += num
    numberOfFiles = len(numbers)
    average = total/numberOfFiles
    average = round(average,2)
    return average

