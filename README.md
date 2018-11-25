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
## Deployment

Procedure on how to deploy on [heroku](https://www.heroku.com/) as a live system. I choosed installation through the command line because it was easier for me than the web based view.
#### Steps
* install [heroku](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) cli for windows and linux users
```
heroku login
heroku create --region eu your_appname # creates app in eu region, common regions: eu, us
heroku buildpacks:set heroku/python # set python buildpack
git push heroku master # deploy app to heroku
heroku ps:scale worker=1 # start bot dyno
heroku logs --tail # If for some reason it’s not working, check the logs
heroku ps:stop bot #stop bot dyno
```

## Built With

* [Heroku](https://www.heroku.com/) - Used as platform as a service
* [VSCode](https://code.visualstudio.com/) - Text editor used because of its vast plugins
* [TelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - Telegram service used

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/0x6f736f646f/InstagrampostsTelegramBot/blob/master/LICENSE) file for details

## Acknowledgments

* [Heroku](https://www.heroku.com/) Using their free account
* [Stackoverflow](https://stackoverflow.com/questions/40356197/python-error-r10-boot-timeout-web-process-failed-to-bind-to-port-within) Problem caused when the web process fails to bind to a port
