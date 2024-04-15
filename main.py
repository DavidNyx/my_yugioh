import requests
import urllib.request
import threading
import json
from rdflib import Graph
from urllib.parse import quote
import os

IMG = "img"
URL = "https://yugipedia.com/wiki"
SUB_URL = "https://ms.yugipedia.com"
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"
    }

def download_img(id):
    response = requests.get(url=URL + "/" + id, headers=HEADERS)
    data = str(response.content).split('"')
    for d in data:
        if d.find(SUB_URL) != -1:
            img_url = d
            break
    response = requests.get(img_url, stream=True, headers=HEADERS)
    try:
        urllib.request.urlretrieve(img_url, IMG + "/" + id + ".png")
    except:
        print("error")
        
def download_img_bulk(img_list):  
    threads = []

    for i in img_list:
        thread = threading.Thread(target=download_img, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def read_json_file(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.loads(json.dumps(json.load(file)).replace("\\u25cf", "*"))
    return data

def get_cards_name(data, names):
    pivot = '</a>&#160;<span class="smwbrowse">'
    parts = data.split(pivot, 1)
    result = parts[0].rsplit(">", 1)
    names.append(result[1])
    try:
        get_cards_name(parts[1], names)
    except:
        pass

def get_all_cards_name():
    offset = 0
    names = []
    threads = []

    while offset <= 13000:
        thread = threading.Thread(target=get_limit_cards_name, args=(offset,names))
        threads.append(thread)
        thread.start()
        offset += 500

    for thread in threads:
        thread.join()
        
    return names
   
def get_limit_cards_name(offset, names):
    response = requests.get(url="https://yugipedia.com/index.php?title=Concept:CG_cards&limit=500&offset=" + str(offset) + "&from=&until=&value=#smw-result", headers=HEADERS)
    data = str(response.content)
    get_cards_name(data, names)

def get_card_rdf(name):
    quote_name = quote(name.replace(' ', '_').replace('/','-2F'))
    response = requests.get(url= "https://yugipedia.com/index.php?title=Special:ExportRDF/" + quote_name + "&syntax=rdf", headers=HEADERS)
    rdf_file = 'rdf/' + quote_name + '.rdf'
    
    with open(rdf_file, 'w', encoding='utf-8') as file:
        file.write(response.content.decode('utf-8'))
        
    return rdf_file

def read_card_rdf(rdf_file):   
    g = Graph()
    g.parse(rdf_file, format="xml")
    return g

def get_all_cards_rdf():
    names = get_all_cards_name()
    threads = []
    
    for n in names:
        if n.find('/') != -1:
            thread = threading.Thread(target=get_card_rdf, args=(n,))
            threads.append(thread)
            thread.start()
    
    for thread in threads:
        thread.join()
            
def list_files(folder_path):
    files = os.listdir(folder_path)
    return files

def main():
    # for subj, pred, obj in g:
    #     print(subj)
    #     print(pred)
    #     try:
    #         print(obj)
    #     except:
    #         print("pass")
    #     print("----------------------")
    # get_all_cards_rdf()
    names = get_all_cards_name()
    files = list_files('rdf')
    for n in names:
        quote_name = quote(n.replace(' ', '_').replace('/','-2F')) + '.rdf'
        if quote_name not in files:
            print(n)
            print(quote_name)

if __name__ == '__main__':
    main()
