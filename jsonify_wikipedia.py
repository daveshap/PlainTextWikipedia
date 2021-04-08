import re
import os
import json
from uuid import uuid4
import gc
from html2text import html2text as htt
import wikitextparser as wtp


archive_dir = 'd:/WikipediaArchive/'  # update this
dest_dir = 'D:/enwiki20201020/'  # update this
chars_per_file = 40 * 1000 * 1000  # create a consistently sized chunk (40MB each)


def remove_double_curly(text):
    while True:
        before = len(text)
        text = re.sub('{{[^{]*?}}', '', text) 
        after = len(text)
        if before == after:
            return text


def remove_double_brackets(text):
    while True:
        before = len(text)
        double_brackets = re.findall('\[\[.*?\]\]', text)
        for db in double_brackets:
            if '|' in db:
                new = db.split('|')[-1].strip(']')
                text = text.replace(db, new)
            else:
                new = db.strip('[').strip(']')
                text = text.replace(db, new)
        after = len(text)
        if before == after:
            return text    


def remove_ref_tags(text):
    while True:
        before = len(text)
        text = re.sub('&lt;ref((?!&lt;/ref).)*&lt;/ref&gt;', '', text) 
        after = len(text)
        if before == after:
            return text


def remove_headings(text):
    while True:
        before = len(text)
        text = re.sub('==(.)*==', '', text) 
        after = len(text)
        if before == after:
            return text


def dewiki(text):
    text = remove_double_curly(text)
    text = remove_double_brackets(text)
    text = remove_ref_tags(text)
    text = remove_headings(text)
    text = wtp.parse(text).plain_text()
    text = htt(text)
    text = text.replace('\\n',' ')
    text = re.sub('\[\[', ' ', text)
    text = re.sub('\]\]', ' ', text)
    text = re.sub('\s+', ' ', text)
    return text
    

def analyze_chunk(text):
    try:
        if '<redirect title="' in text:  # this is not the main article
            return None
        else:
            title = text.split('<title>')[1].split('</title>')[0]
            if ':' in title:  # this is a talk, category, or other (not a real article)
                return None
            title = htt(title).strip()
        serial = text.split('<id>')[1].split('</id>')[0]
        content = text.split('</text')[0].split('<text')[1].split('>', maxsplit=1)[1]
        content = dewiki(content)
        return {'title': title, 'text': content, 'id': serial}
    except:
        return None


def save_data(data):
    if len(data) == 0:
        return
    filename = dest_dir + str(uuid4()) + '.json'
    print('Saving:\t', filename)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=1, ensure_ascii=False)


def main(file):
    print(file)
    outdata = list()
    article = ''
    total_len = 0
    with open(archive_dir + file, 'r', encoding='utf-8') as infile:
        for line in infile:
            if '<page>' in line:
                article = ''
            elif '</page>' in line:  # end of article
                doc = analyze_chunk(article)
                if doc:
                    outdata.append(doc)
                    total_len += len(doc['text'])
                    #if len(outdata) >= articles_per_file:
                    if total_len >= chars_per_file:
                        save_data(outdata)
                        outdata = list()
                        total_len = 0
            else:
                article += line
    save_data(outdata)

    
if __name__ == '__main__':
    for file in os.listdir(archive_dir):
        if 'bz2' in file:
            continue
        main(file)
        gc.collect()
    
