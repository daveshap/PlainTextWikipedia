# PlainTextWikipedia

Convert Wikipedia database dumps into plain text files (JSON). This can parse literally all of Wikipedia with pretty high fidelity. There's a copy available on [Kaggle Datasets](https://www.kaggle.com/ltcmdrdata/plain-text-wikipedia-202011)

## QUICK START

1. Download and unzip a Wikipedia dump (see Data Sources below) make sure you get a monolithic XML file
2. Open up `wiki_to_text.py` and edit the filename to point at your XML file. Also update the savedir location
3. Run `wiki_to_text.py` - it should take about 2.5 days to run, with some variation based on your CPU and storage speed


## Key Files in this Repo

| Filename | Description |
|---|---|
| `dewiki_functions.py` | Collection of Wikipedia parsing functions, including XML file handler |
| `jsonify_simple_wikipedia.py` | Follow-up experiment focusing on the Simple English Wikipedia |
| `jsonify_wikipedia.py` | Original Wikipedia parser experiment |
| `simple_wiki_to_solr.py` | Experiment for indexing Simple English Wikipedia to SOLR |
| `simple_wikipedia_to_sqlite.py` | Experiment of storing Wikipedia in SQLITE |
| `solr_functions.py` | Collection of functions to help with using SOLR |
| `start_solr.bat` | Batch file for starting SOLR Docker container on Windows if Docker Desktop is installed |
| `test_simple_wiki.xml` | The first 50,000 lines of a Simple English Wikipedia dump for testing purposes |


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

## SOLR

SOLR is an enterprise-grade search engine. Think of it like a private Google. It's got some AI built in to make search faster and more powerful than just a database service. 

Fortunately, SOLR is ultra easy to setup today with tools like Docker Desktop:

1. Get [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Use `start_solr.bat` in this repo to launch SOLR

The same command should work in bash scripting.

## Output Types

I presently have 3 output formats:

1. Plain JSON via `jsonify_wikipedia.py`
2. Save to SQLITE via `simple_wikipedia_to_sqlite.py`
3. Index to SOLR via `simple_wiki_to_solr.py`

These are all a Work In Progress (WIP). I am working on breaking the essential functions down into individual files so they are easier for you to use in your own projects. 

## Utility Files

If you want to use my functions for your own tools, here they are!

### dewiki_functions.py

This file contains the XML parsing functions. Here's an overview of how it works:

1. The Wikipedia dumps come in giant XML files - too big to read as a whole so you have to read them line-by-line.
2. Start by calling `process_file_solr` (will add more functions in the future). Pass this function the filename of the XML dump.
3. This function will read the XML file line-by-line and build up the Wikipedia documents, saving them to SOLR. 
4. You can also call whichever functions you want, such as `dewiki` and just pass it the text blob. 

Why REGEX? Python's `re` module makes use of efficiencies available from the underlying OS. Computers have used REGEX for ages and so they are very fast at using REGEX. Because of this, REGEX is stupid fast - far faster than html2text or WikiTextParser. You're welcome to test it yourself but I've done countless experiments. Relying on REGEX is hundreds of times faster. 

### solr_functions.py

This file contains some basic SOLR request functions for python. It is still a work in progress but it will contain index and query functions. 

### sqlite_functions.py

This file doesn't exist yet, but I will split off my SQLITE functions into this file eventually.

## Legal

https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content

Wikipedia is published under [Creative Commons Attribution Share-Alike license (CC-BY-SA)](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License). 

My script is published under the MIT license but this does not confer the same privileges to the material you convert with it. 

