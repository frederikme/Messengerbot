'''

Created by Frederikme (TeetiFM)

examples of usage

/* Create instance/object */
bot = MessengerBot(email="testemail@email.com", password="testpassword")

/* Log in to messenger */
bot.login()

/* To get ids of open chats */
bot.getChatIDs()

/* To send a message */
bot.sendMessage(chatid, message)

/* To Change the name of the chat */
bot.changeChatName(chatid, name)

'''

from bot import *
import constants  # remove this import

# fill in your own email and password with
# email = "example@email.com", pwd = "password123" and textfile = "filename.txt"
email = constants.EMAIL
pwd = constants.PASSWORD
textfile = constants.TEXTFILE

if __name__ == "__main__":

    # creates instance of bot
    bot = MessengerBot(email=email, password=pwd)
    # go to login page of messenger and log in
    bot.login()

    # see which chat has which id
    for (name, id) in bot.getChatIDs():
        print("{:>50}   {:>20}".format(name, id))
    
    '''
    # opens textfile from the same directory and sends separate chat messages for each line
    file = open(textfile, "r")
    for line in file:
        # conversations have url as www.messenger.com/t/id
        bot.sendChatMessage(chatid="3719819448058542", message=line)

    # changes the name of the chat
    bot.changeChatName(chatid="3719819448058542", name="new name")
    '''
    

    
