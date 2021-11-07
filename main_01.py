import requests
from bs4 import BeautifulSoup


def main():
    url = "https://animevost.am"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    }

    resp = requests.get(url, headers=headers).text
    soup = BeautifulSoup(resp, features="html.parser")

    name = []
    urls = []
    

    item = soup.find_all("div", class_="shortstory")
    for anime in item:
        anime2 = anime.find(class_="shortstoryHead").find_all("a")
        for anime3 in anime2:
            name.append(anime3.text)
            url = anime3.get("href")
        urls.append(url)
    global data
    data = {
        f'{name[0]}': f'{urls[0]}',
        f'{name[1]}': f'{urls[1]}',
        f'{name[2]}': f'{urls[2]}',
        f'{name[3]}': f'{urls[3]}',
        f'{name[4]}': f'{urls[4]}',
        f'{name[5]}': f'{urls[5]}',
        f'{name[6]}': f'{urls[6]}',
        f'{name[7]}': f'{urls[7]}', 
        f'{name[8]}': f'{urls[8]}',
        f'{name[9]}': f'{urls[9]}',
    } 

def returns_data() : 
    return data


if __name__ == "__main__": 
    main() 
    returns_data()