from bs4 import BeautifulSoup
import requests
import urllib

def get_info(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    json_meta = dict()
    for meta in soup.find_all("meta"):
        json_meta[meta.get("property")] = meta.get("content")
        json_meta[meta.get("name")] = meta.get("content")

    data = dict()
    data["title"] = soup.find_all("title")[0].text

    if json_meta.get('description'):
        data["des"] = json_meta.get('description')
    elif json_meta.get('og:description'):
        data["des"] = json_meta.get('og:description')
    else:
        data["des"] = "No futher infrmation avalible"

    if json_meta.get('og:image'):
        data["image"] = json_meta.get('og:image')
    else:
        data["image"] = json_meta.get('image', "http://impactbuilders.com/images/no-image.png")

    data["link"] = url

    return data

# print json_meta.get('og:image')
# print json_meta.get('image')
# print json_meta.get('keywords')
# print json_meta.get('og:site_name')

# n = int(raw_input().strip())
# a = map(int, raw_input().strip().split(' '))