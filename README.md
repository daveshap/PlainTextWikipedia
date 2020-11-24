# PlainTextWikipedia

Convert Wikipedia database dumps into plain text files (JSON). This can parse literally all of Wikipedia with pretty high fidelity. 

## Instructions

1. Download all the .bz2 files from a dump: https://dumps.wikimedia.org/enwiki/ The filename should look like `enwiki-20201120-pages-articles-multistream1.xml-p1p41242.bz2`
2. Unzip all bz2 files directly to another directory, such as `WikipediaArchive`
3. Run the script `jsonify_wikipedia.py` (update the directories within and install prerequisites first)

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
