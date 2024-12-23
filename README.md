# KotikBot или же Кошка-Бот
Программа выкладывает в ваш телеграм-канал красивые фото кошечек и котят, а под постом пишет шутейки из 2010-х.
## Как установить
Скачайте и разархвириуйте код на своем компьютере.
Python3 должен быть уже установлен. Затем используйте pip (или pip3) для установки зависимостей:
```
pip install -r requirements.txt
```
## Как запустить
Нужно зайти на ваш телеграм канал и в переменную в файле main.py 'telegram_chat_id' введите ID своего телеграм канала, к примеру:
```
telegram_chat_id = '@gisagg'
```
Далее создайте телеграм бота и получите его токен.Бота надо назначить администратором телеграмм канала.
Создайте файл .env, файл должен выглядеть так:
```
TELEGRAM_TOKEN="ij4393iungriougijnoq8unv8328nco39fdm"
```
Чтобы запустить программу, напишите в терминал:
```
python main.py
```