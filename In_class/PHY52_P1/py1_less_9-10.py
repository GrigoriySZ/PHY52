import requests as rq  # Библиотека requests для перехода на сайты
import bs4  # Библиотека bs4 улучшаем читаемость данных в html
import random as rnd
# Подгружаем библиотку через терминал: 
# pip install requests
# pip install bs4

response = rq.get("https://nukadeti.ru/skazki")

links = []

# Код 200 говорит о том, что мы получили ответ от сервера и он передал данные
if response.status_code == 200:
    
    # Пе 
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    tags = soup.find_all("a", class_="title")
    for tag in tags:
        links.append("https://nukadeti.ru" + tag.get("href"))

def get_tale(refs: list[str]):
    ref = rnd.choice(refs)
    resp = rq.get(ref)
    soup_tale = bs4.BeautifulSoup(resp.text, "html.parser")
    header = soup_tale.find("h1")
    text = soup_tale.find("div", class_="tale-text").text
    return {"заголовок": header, "сказка": text}

print(get_tale(links))