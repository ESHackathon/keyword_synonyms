import sys
import requests
import json

url = "http://k.episte.co/keywords/similars"


def get_synonyms(infile, outfile, n):
    with open(infile, 'r') as jsonfile:
        data = json.load(jsonfile)
    output = {}
    for k in data['keywords']:
        r = requests.get(url, params={'positive': k, 'size': n})
        output[k] = r.json()
    with open(outfile, 'w+') as out:
        json.dump(output,out)


if __name__ == "__main__":
    n = sys.argv[3]
    infile = sys.argv[1]
    outfile = sys.argv[2]
    get_synonyms(infile, outfile, n)
