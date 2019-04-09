import sys
import requests
import json

url = "http://k.episte.co/keywords/similars"

def get_synonyms(infile, n):
    with open(infile, 'r') as jsonfile:
        data = json.load(jsonfile)
    output = {}
    for k in data['keywords']:
        r = requests.get(url, params={'positive': k, 'size': n})
        output[k] = r.json()
    print(json.dumps(output))
    # with open('output.json', 'w+') as outfile:
    #     outfile.write(json.dumps(output))


if __name__ == "__main__":
    n = sys.argv[2]
    infile = sys.argv[1]
    get_synonyms(infile, n)
