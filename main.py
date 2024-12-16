import os
from dotenv import load_dotenv
import requests
from time import sleep
import random

load_dotenv()

def save_and_download_image(picture_url,photo_path):
            response = requests.get(picture_url)
            with open(photo_path, "wb") as file:
                file.write(response.content)
            return response
    
while True:
    telegram_token = os.getenv("TELEGRAM_TOKEN")

    chat_id = '@ehrukwskidjk'
    url = 'https://api.thecatapi.com/v1/images/search'

    params = {
        'format': 'json',
        'type': 'top',
        'amount': 100
    }
    
    
    response = requests.get(url)
    response.raise_for_status()
    image_url = response.json()[0]['url']
    save_and_download_image(image_url,'амамкотик.png')

    response = requests.get('http://shortiki.com/export/api.php',params = params)
    response.raise_for_status()
    sigma =  random.choice(response.json())
    abobe = (sigma['content'])
    
    
    file = {'photo': open('амамкотик.png', 'rb')}
    response = requests.post(f'https://api.telegram.org/bot{telegram_token}/sendPhoto?chat_id={chat_id}&caption={abobe}', files=file)
    

    sleep(10)
