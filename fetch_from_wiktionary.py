import requests
import json

base_url = "https://de.wiktionary.org/w/api.php?action=query&list=categorymembers&cmtitle=Kategorie:Abkürzung_(Deutsch)&format=json"
data = []
continue_param = None

while True:
    url = base_url
    if continue_param is not None:
        url += '&cmcontinue=' + continue_param
    print(url)
    response = requests.get(url)
    json_data = json.loads(response.content)
    if "query" in json_data:
        for item in json_data["query"]["categorymembers"]:
            data.append(item["title"])
    
    if "continue" not in json_data:
        print(json_data)
        break
    else:
        continue_param = json_data["continue"]["cmcontinue"]

with open('german_abbreviations.txt', 'w') as file_handler:
    for item in data:
        file_handler.write("{}\n".format(item))
