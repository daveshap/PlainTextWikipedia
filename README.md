# PlainTextWikipedia
Convert Wikipedia database dumps into plaintext files

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
