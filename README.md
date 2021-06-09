# cataas-telegram
A Telegram bot that uses [CATAAS'](https://cataas.com/#/about) API to spread peace and love (or not) thanks to cats.

## Requirements
 - Python 3
 - [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
 - requests
 - Love for animals 😻😽

## Usage
First clone this repository, then install required libraries running the command

    pip3 install -r requirements.txt

Replace inside `bot.py` file the Telebot constructor parameter with token given by the [BotFather](https://t.me/botfather) and finally run

    python3 bot.py

![](https://cataas.com/cat/says/Hello%20world!?height=250)

You can try the bot searching [@cataas_bot](https://t.me/cataas_bot) on Telegram.
## How it works
The bot makes HTTP GET method requests in order to get a json file and delive cats when user sends a Telegram bot command. This bot can send static images sending */cat* command, or */gif* to receive animated ones.

You can also generate images with some text sending a _/cat_ command with the desired text.

## Notes
While actually this bot can do few things, CATAAS offers more nice features that requires more free time in order to be implemented.
Things that I'd like to implement:
 - Receive cats with a tag (e.g. _sleeping_, _cute_, _meme_...)
 - Apply filters to images with Telegram commands
 - Customize colour and size of texts

Meow 🐱
