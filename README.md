# Instagramfinder Telegram Bot 

Help in finding instagram profile url given the username

## Getting Started

To get the project up and running on your local machine. See deployment for notes on how to deploy the project on a live system.

### Telegram
* Get started using [BotFather](http://t.me/BotFather)
* Click on /start
* type /newbot to start a new telegram bot
* Enter your bot name e.g Mulembe
* Choose your username tha ends with _bot or Bot e.g Mulembe1_bot
* Copy your API token somewhere for later use


### Windows
```
mkdir InstaFinder
cd InstaFinder
virtualenv --no-site-packages root
root\Scripts\activate
git clone https://github.com/0x6f736f646f/InstagrampostsTelegramBot
cd InstagrampostsTelegramBot
```

### Linux
```
mkdir InstaFinder
cd InstaFinder
virtualenv --no-site-packages root
.root/bin/activate
git clone https://github.com/0x6f736f646f/InstagrampostsTelegramBot
cd InstagrampostsTelegramBot
```


### Prerequisites

What is needed to run the project
```
pip install -r requirements.txt
```
Create a new file to have your api token 

#### Windows
```
notepad secret.py
```
#### Linux
```
nano secret.py
```
On the open file type **bot_api_token = 'api_token from bot father'**
save then exit

## Running on local machine

```
python bot.py
```