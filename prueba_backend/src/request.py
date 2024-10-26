import requests
import json

def get_images_api(id):
    enpoint = f"https://api.jikan.moe/v4/anime/{id}/pictures"
    response = requests.get(enpoint)
    parse_to_json = response.json()
    dump_json = json.dumps(parse_to_json, indent=4)
    json_load = json.loads(dump_json)
    return json_load

def conver_to_html(array):
    images = []
    for item in array["data"]:
        #jpg_url = item["jpg"]["image_url"]
        webp_url = item["webp"]["image_url"]
        
        #print(f"JPG Image URL: {jpg_url}")
        #print(f"WEBP Image URL: {webp_url}")
        images.append(webp_url)
        
        # Crear el contenido HTML
        html_content = "<html><body>\n"
        for url in images:
            html_content += f'<img src="{url}" style="width:200px; height:auto; margin:10px;">\n'
        html_content += "</body></html>"
        
        # Guardar el HTML en un archivo
        with open("images.html", "w") as file:
            file.write(html_content)

    return print("Archivo HTML generado: images.html")

def search_to_name(name):
    endpoint = f"https://api.jikan.moe/v4/anime?q={name}&sfw"
    response = requests.get(endpoint)
    parse_to_json = response.json()
    
    # Retorna el contenido JSON para que puedas trabajar con él
    return parse_to_json