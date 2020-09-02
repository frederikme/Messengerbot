# Messengerbot
Simple bot for messenger using selenium (simple user interface included) written in python3

## Make sure python and pip are installed
Pip should be included with python by default.<br />
Dowload python: https://www.python.org/downloads/

## Usage of a virtual environment recommended
### install virtualenv
```
pip3 install virtualenv 
```
### Create virtual environment
```
virtualenv venv
```
### Activate virtual environment
```
source venv/bin/activate
```
### To deactivate or leave the virtual environment
```
deactivate
```
## Install dependencies (preferably in the venv)
```
pip3 install -r requirements.txt
```
## Make your adjustments in the template.py file
The template.py file gives much more freedom and features than the graphical user interface (GUI). </br>
```
# Create instance of messengerbot 
bot = MessengerBot(email=email, password=pwd)

# Open https://www.messenger.com and login
bot.login()

# Get names and ids of your chats and log them to terminal/cmd 
bot.getChatIDs()

# Send a message
bot.sendMessage(chatid, message)

# Change the name of the chat 
bot.changeChatName(chatid, name)
```
## Run the userinterface.py file for a GUI
![alt tag](https://user-images.githubusercontent.com/60892381/91411771-1a511700-e849-11ea-8e62-03d464ab8cf5.png)
