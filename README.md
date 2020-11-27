# PlainTextWikipedia

Convert Wikipedia database dumps into plain text files (JSON). This can parse literally all of Wikipedia with pretty high fidelity. There's a copy available on [Kaggle Datasets](https://www.kaggle.com/ltcmdrdata/plain-text-wikipedia-202011)

## Instructions

1. Download all the .bz2 files from a dump: https://dumps.wikimedia.org/enwiki/ The filename should look like `enwiki-20201120-pages-articles-multistream1.xml-p1p41242.bz2`
2. Unzip all bz2 files directly to another directory, such as `WikipediaArchive`
3. Install `REQUIREMENTS.TXT`
4. Update the source and destination directory variables in `jsonify_wikipedia.py`
5. Run the script `jsonify_wikipedia.py` 

This will deposit a ~40MB JSON files into the destination folder. Each filename is guaranteed to be completely unique as it is based on UUIDv4. 

## File Schema

Each file is a JSON object with the root element as a list. Each dictionary within the list has only 3 keys: `id`, `title` and `text`. The ID field comes from the wikipedia article ID. The title and text are the page title and plain-text parsed article respectively. An example follows. 

```json
[
 {
  "id": "17279752",
  "text": "Hawthorne Road was a cricket and football ground in Bootle in England...",
  "title": "Hawthorne Road"
 }
]
```

## Legal

https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content

Wikipedia is published under [Creative Commons Attribution Share-Alike license (CC-BY-SA)](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License). 

My script is published under the MIT license but this does not confer the same privileges to the material you convert with it. 

## Future Improvements

1. Maintain some article structure in JSON format
2. Better demarkup handling
3. Better retention of link and image context
