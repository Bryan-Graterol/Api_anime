import requests
import json

def get_images_api(id):
    enpoint = f"https://api.jikan.moe/v4/anime/{id}/pictures"
    response = requests.get(enpoint)
    parse_to_json = response.json()
    dump_json = json.dumps(parse_to_json, indent=4)
    json_load = json.loads(dump_json)
    return json_load

def search_to_name(name):
    endpoint = f"https://api.jikan.moe/v4/anime?q={name}&sfw"
    response = requests.get(endpoint)
    parse_to_json = response.json()
    # Retorna el contenido JSON para que puedas trabajar con él
    return parse_to_json