# PlainTextWikipedia

Convert Wikipedia database dumps into plain text files (JSON). This can parse literally all of Wikipedia with pretty high fidelity. There's a copy available on [Kaggle Datasets](https://www.kaggle.com/ltcmdrdata/plain-text-wikipedia-202011)

## QUICK START

1. Download and unzip a Wikipedia dump (see Data Sources below) make sure you get a monolithic XML file
2. Open up `wiki_to_text.py` and edit the filename to point at your XML file. Also update the savedir location
3. Run `wiki_to_text.py` - it should take about 2.5 days to run, with some variation based on your CPU and storage speed


## Data Sources

There are two primary data sources you'll want to use. See the table below for the root url. 

| Name | Description | Link |
|---|---|---|
| Simplified English Wikipedia | This is only about 1GB and therefore is a great test set | [https://dumps.wikimedia.org/simplewiki/](https://dumps.wikimedia.org/simplewiki/) |
| English Wikipedia | This is all of Wikipedia, so about 80GB unpacked | [https://dumps.wikimedia.org/enwiki/](https://dumps.wikimedia.org/enwiki/)

Navigate into the latest dump. You're likley looking for the very first file in the download section. They will look something like this:

- `enwiki-20210401-pages-articles-multistream.xml.bz2 18.1 GB`
- `simplewiki-20210401-pages-articles-multistream.xml.bz2 203.5 MB`

Download and extract these to a storage directory. I usually shorten the folder name and filename. 

## Legal

https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content

Wikipedia is published under [Creative Commons Attribution Share-Alike license (CC-BY-SA)](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License). 

My script is published under the MIT license but this does not confer the same privileges to the material you convert with it. 

