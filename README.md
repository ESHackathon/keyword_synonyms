### keyword_synonoyms

This library uses the [keyword2svec API](http://18.212.76.171/episte/) ([code here](https://github.com/dperezrada/evidence-tools/tree/master/nlp/keywords2vec)) to fetch synonmys for a specified set of keywords

##Usage

`keywords.py` takes the input file (in JSON format) and the desired number of synonyms for each keyword as command line arguments

`python keywords.py input.json 5`

This will produce a file named `output.json` containing the synonyms returned for each keyword