import requests
import urllib.request
import threading
import json
from rdflib import Graph
from urllib.parse import quote
import os
import time

IMG = "img/"
RDF = "rdf/"
JSON = "json/"
URL = "https://yugipedia.com/wiki/"
SUB_URL = "https://ms.yugipedia.com"
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"
    }
LIMITS = {
    "Unlimited": 3,
    "Semi-limited": 2,
    "Limited": 1,
    "Forbiden": 0
}

def str_to_utf_8(old_str):
    new_str = old_str.replace("\\'","'")
    new_str = new_str.replace("\\xc3\\xa9", "é")
    new_str = new_str.replace("\\xc3\\xba","ú")
    new_str = new_str.replace("\\xe2\\x98\\x85","★")
    new_str = new_str.replace("\\xc3\\x9c","Ü")
    new_str = new_str.replace("\\xc3\\xb1a","ñ")
    new_str = new_str.replace("\\xce\\xb1", "α")
    new_str = new_str.replace("\\xe3\\x83\\xbb","・")
    new_str = new_str.replace("\\xce\\xb2", "β")
    new_str = new_str.replace("\\xce\\xa9", "Ω")
    new_str = new_str.replace("\\xe2\\x98\\x86", "☆")
    new_str = new_str.replace("\\xc3\\xa4", "ä")
    
    return new_str

def download_img(id):
    response = requests.get(url=URL + id, headers=HEADERS)
    data = str(response.content).split('"')
    for d in data:
        if d.find(SUB_URL) != -1:
            img_url = d
            break
    response = requests.get(img_url, stream=True, headers=HEADERS)
    try:
        urllib.request.urlretrieve(img_url, IMG + id + ".png")
        print("downloaded: " + id)
    except:
        print("error: " + id)
        
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
    if result[1] != "\\n'":
        names.append(str_to_utf_8(result[1]))
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
    quote_name = quote(name.replace(' ', '_').replace('/', '-2F'))
    if quote_name.find("-2FAssault_Mode") != -1:
        quote_name = quote_name.replace('-2F','/')
        response = requests.get(url= "https://yugipedia.com/index.php?title=Special:ExportRDF/" + name + "&syntax=rdf", headers=HEADERS)
        quote_name = quote_name.replace('/','-2F')
    else:
        response = requests.get(url= "https://yugipedia.com/index.php?title=Special:ExportRDF/" + quote_name + "&syntax=rdf", headers=HEADERS)
    rdf_file = RDF + quote_name + '.rdf'
    
    with open(rdf_file, 'w', encoding='utf-8') as file:
        file.write(response.content.decode('utf-8'))
        
        return rdf_file
    
def get_card_rdf_file(name_file):
    if name_file.find("-2F") != -1 or name_file.find("%C3%B1%2C") != -1:
        name_file = name_file.replace('-2F','/').replace("%C3%B1%2C", "ña,")
        response = requests.get(url= "https://yugipedia.com/index.php?title=Special:ExportRDF/" + name_file + "&syntax=rdf", headers=HEADERS)
        name_file = name_file.replace('/','-2F').replace("ña,", "%C3%B1%2C")
    else:
        response = requests.get(url= "https://yugipedia.com/index.php?title=Special:ExportRDF/" + name_file + "&syntax=rdf", headers=HEADERS)
    rdf_file = RDF + name_file + '.rdf'
    
    with open(rdf_file, 'w', encoding='utf-8') as file:
        file.write(response.content.decode('utf-8'))
    
    return rdf_file

def read_card_rdf(rdf_file):
    try:
        g = Graph()
        g.parse(rdf_file, format="xml")
    except:
        name_file = rdf_file.split(".rdf")[0].split("/")[1]
        rdf_file = get_card_rdf_file(name_file)
        card_data = read_card_rdf(rdf_file)
        return card_data
    
    card_data = {
        "versions" : {},
        "link_arrows": []
    }

    for subj, pred, obj in g:
        try:
            subj = str(subj)
            pred = str(pred)
            obj = str(obj)
            # print(subj)
            # print(pred)
            # print(obj)
            # print("----------------------")
            
            if pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3ATCG_status":
                if obj == "http://yugipedia.com/wiki/Special:URIResolver/Illegal":
                    return
                else:
                    limit = obj.split("http://yugipedia.com/wiki/Special:URIResolver/")[1]
                    card_data["versions"]["tcg"] = LIMITS[limit]
                    
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3AOCG_status":
                if obj == "http://yugipedia.com/wiki/Special:URIResolver/Illegal":
                    return
                else:
                    limit = obj.split("http://yugipedia.com/wiki/Special:URIResolver/")[1]
                    card_data["versions"]["ocg"] = LIMITS[limit]

            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3APassword":
                card_data["card_id"] = obj
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3AEnglish_name":
                if not obj.isdigit():
                    card_data["card_name"] = obj
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3ALore":
                card_data["desc"] = obj
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3ALevel_string":
                card_data["level"] = obj
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3AATK_string":
                card_data["atk"] = obj
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3ADEF_string":
                card_data["def"] = obj
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3ACard_type":
                card_data["category"] = obj.split("http://yugipedia.com/wiki/Special:URIResolver/")[1].replace('_', ' ')
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3AAttribute":
                card_data["attr"] = obj.split("http://yugipedia.com/wiki/Special:URIResolver/")[1]
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3AProperty":
                card_data["type"] = obj
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3ALink_Arrows":
                card_data["link_arrows"].append(obj)
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3APendulum_Scale_string":
                card_data["scale"] = obj
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3APendulum_Effect":
                card_data["pendulum_effect"] = obj
            elif pred == "http://yugipedia.com/wiki/Special:URIResolver/Property-3ATypes":
                obj_list = obj.split(" / ")
                card_data["type"] = obj_list.pop(0)
                card_data["subcategory"] = []
                for o in obj_list:
                    card_data["subcategory"].append(o)
            
        except:
            pass
    
    if card_data == {"versions" : {}, "link_arrows": []}:
        with open("logs-1.txt", 'r') as file:
            lines = file.readlines()
        lines.append(rdf_file + "\n")
        with open("logs-1.txt", 'w') as file:
            file.writelines(lines)
        
    return card_data

def get_all_cards_rdf():
    names = list_all_card_names()
    threads = []
    
    for n in names:
        thread = threading.Thread(target=get_card_rdf, args=(n,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
            
def get_all_cards_rdf_1():
    names = list_all_card_names()

    for n in names:
        get_card_rdf(n)
        time.sleep(1)
        
def list_files(folder_path):
    files = os.listdir(folder_path)
    return files

def list_all_card_names():
    names = []
    with open("card names.txt", 'r', encoding='utf-8') as file:
        for line in file:
            names.append(line.strip())
    
    return names

def write_all_json_file():
    names = list_all_card_names()
    for n in names:
        try:
            print(n)
        except:
            pass
            
        t = quote(n.replace(' ', '_').replace('/','-2F')) + ".rdf"
        card_data = read_card_rdf(RDF + t)
        if card_data is not None:
            with open(JSON + t.replace(".rdf", ".json"), 'w', encoding='utf-8') as file:
                json.dump(card_data, file, indent=4)
                file.close()

def main():
    pass
    
    
            
if __name__ == '__main__':
    main()
