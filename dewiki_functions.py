import re
from html2text import html2text as htt
import wikitextparser as wtp
from solr_functions import *


def remove_simple_links(text):
    links = re.findall('''\[\[[\w\s]+\]\]''', text)
    for link in links:
        new = link.replace('[', '').replace(']', '')
        text = text.replace(link, new)
    return text


def remove_compound_links(text):
    # EX: [[autumn|autumn/fall]]
    links = re.findall('''\[\[[\w\s|]+\]\]''', text)
    for link in links:
        new = link.replace('[', '').replace(']', '').split('|')[-1]
        text = text.replace(link, new)
    return text


def remove_all_links(text):
    links = re.findall('''\[\[.*?\]\]''', text)
    for link in links:
        new = link.replace('[', '').replace(']', '').split('|')[-1]
        text = text.replace(link, new)
    return text


def remove_pictures(text):
    # EX: [[File:Earth flag PD.jpg|thumb|200px|right|Proposed flag for Earth Day on April 22.]]
    images = list()
    images += re.findall('''\[\[File:.*?jpg.*?\]\]''', text)
    images += re.findall('''\[\[File:.*?JPG.*?\]\]''', text)
    images += re.findall('''\[\[File:.*?jpeg.*?\]\]''', text)
    images += re.findall('''\[\[File:.*?JPEG.*?\]\]''', text)
    images += re.findall('''\[\[File:.*?png.*?\]\]''', text)
    images += re.findall('''\[\[File:.*?PNG.*?\]\]''', text)
    images += re.findall('''\[\[File:.*?svg.*?\]\]''', text)
    images += re.findall('''\[\[File:.*?SVG.*?\]\]''', text)
    images += re.findall('''\[\[Image:.*?\]\]''', text)
    for image in images:
        new = image.split('|')[-1]
        new = new.replace(']', '')
        new = 'IMAGE: "%s"' % new
        text = text.replace(image, new)
    return text


def remove_audio(text):
    # EX: 
    audios = list()
    audios += re.findall('''\[\[File:.*?ogg.*?\]\]''', text)
    audios += re.findall('''\[\[File:.*?OGG.*?\]\]''', text)
    audios += re.findall('''\[\[File:.*?flac.*?\]\]''', text)
    audios += re.findall('''\[\[File:.*?FLAC.*?\]\]''', text)
    for audio in audios:
        text = text.replace(audio, ' ')
    return text


def remove_citations(text):
    citations = re.findall('''\{\{.*?\}\}''', text)
    for cite in citations:
        text = text.replace(cite, ' ')
    return text


def remove_categories(text):
    categories = re.findall('''\[\[Category:.*?\]\]''', text)
    for cat in categories:
        text = text.replace(cat, ' ')
    return text


def remove_references(text):
    text = re.sub('==\s*References\s*==.*', ' ', text)
    text = re.sub('==\s*Notes\s*==.*', ' ', text)
    text = re.sub('==\s*Related pages\s*==.*', ' ', text)
    return text


def remove_urls(text):
    text = re.sub('''http://.*?\s''', ' ', text)
    text = re.sub('''https://.*?\s''', ' ', text)
    return text


def dewiki(text):
    text = remove_simple_links(text)
    text = remove_pictures(text)
    text = remove_audio(text)
    text = remove_compound_links(text)
    text = remove_references(text)
    text = remove_citations(text)
    text = remove_categories(text)
    text = remove_all_links(text)
    text = remove_urls(text)
    # TODO handle class=\"sortable wikitable\" and class=\"wikitable\"
    
    text = wtp.parse(text).plain_text()  # wiki to plaintext whatever is left
    text = htt(text)  # de-HTML text
    
    #text = re.sub('\]\]', ' ', text)  # remove any remnant brackets
    text = text.replace('\\n',' ')  # replace newlines
    text = re.sub('\s+', ' ', text)  # replace excess whitespace
    return text


def analyze_chunk(text):
    try:
        if '<redirect title="' in text:  # this is not the main article
            return None
        else:
            title = text.split('<title>')[1].split('</title>')[0]
            title = htt(title)
        serial = text.split('<id>')[1].split('</id>')[0]
        content = text.split('</text')[0].split('<text')[1].split('>', maxsplit=1)[1]
        content = dewiki(content)
        return {'title': title.strip(), 'text': content.strip(), 'id': serial.strip()}
    except Exception as oops:
        print(oops)
        return None


def process_file_solr(filename):
    article = ''
    with open(filename, 'r', encoding='utf-8') as infile:
        for line in infile:
            if '<page>' in line:
                article = ''
            elif '</page>' in line:  # end of article
                doc = analyze_chunk(article)
                if doc:
                    print(doc['title'])
                    solr_index(doc)
            else:
                article += line