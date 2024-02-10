import json
import time
import requests
from bs4 import BeautifulSoup

# TheHackerNews'dan haber başlıklarını çeken fonksiyon
def fetch_news():
    URL = 'https://thehackernews.com'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article', class_='post')

    news_list = []
    for article in articles:
        title = article.find('h2', class_='home-title').text.strip()
        link = article.find('a')['href'].strip()
        news_list.append({'title': title, 'link': link})

    return news_list

# Telegram API üzerinden mesaj gönderen fonksiyon
def send_message_via_telegram(chat_id, message):
    bot_token = '6554137873:AAFbATfXMqoEtJgu-zxlVyejIfuCfBaFCpM'
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'

    response = requests.get(send_text)
    return response.json()

# Yeni haberleri kontrol eden ve gerekirse gönderen fonksiyon
def check_for_new_news():
    try:
        with open('last_news.json', 'r') as file:
            last_news = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):  # Dosya yok ya da boş/yanlış ise
        last_news = []

    current_news = fetch_news()
    new_news = [news for news in current_news if news not in last_news]

    if new_news:
        for news in new_news:
            message = f"{news['title']} - {news['link']}"
            send_message_via_telegram('6693713647', message)
        with open('last_news.json', 'w') as file:
            json.dump(current_news, file)

# Her 30 dakikada bir kontrol etmek için döngü
while True:
    check_for_new_news()
    print("Haberler kontrol edildi, 30 dakika sonra tekrar kontrol edilecek.")
    time.sleep(1800)  # 1800 saniye = 30 dakika