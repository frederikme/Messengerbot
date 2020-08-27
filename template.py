'''

Created by TeetiFM

examples of usage

/* To get ids of open chats */
bot.getChatIDs()

/* To send a message */
bot.sendMessage(chatid, message)

/* To Change the name of the chat */
bot.changeChatName(chatid, name)

'''

from bot import *
import pyfiglet
import constants  # remove this import
import time

hello_banner = pyfiglet.figlet_format("Hello")

# fill in your own email and password with
# email = "example@email.com", pwd = "password123" and textfile = "filename.txt"
email = constants.EMAIL
pwd = constants.PASSWORD
textfile = constants.TEXTFILE

if __name__ == "__main__":

    print(hello_banner)
    time.sleep(2)

    # creates instance of bot
    bot = MessengerBot(email=email, password=pwd)
    # go to login page of messenger and log in
    bot.login()

    # see which chat has which id
    for (name, id) in bot.getChatIDs():
        print("{:>50}   {:>20}".format(name, id))
    
    
    # opens textfile from the same directory and sends separate chat messages for each line
    file = open(textfile, "r")
    for line in file:
        # conversations have url as www.messenger.com/t/id
        bot.sendChatMessage(chatid="3719819448058542", message=line)

    # changes the name of the chat
    bot.changeChatName(chatid="3719819448058542", name="new name")
    

    
