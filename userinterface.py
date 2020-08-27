import tkinter as tk
from tkinter import ttk
from bot import *
import pyfiglet

class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.bot = None

        self.winfo_toplevel().title("MessengerBot")

        self.logincanvas = tk.Canvas(self, highlightthickness=0)
        self.logincanvas.grid(row=0)

        tk.Label(self.logincanvas, text="Email").grid(row=0)
        tk.Label(self.logincanvas, text="Password").grid(row=1)

        self.email = tk.Entry(self.logincanvas)
        self.password = tk.Entry(self.logincanvas, show="*")
        ttk.Button(self.logincanvas, text="Login", command=self.login).grid(row=1, column=2)

        self.email.grid(row=0, column=1)
        self.password.grid(row=1, column=1)

        tk.Label(self, text="Messages (each line is a separate message)").grid(row=1)
        self.text = tk.Text(self)
        self.text.insert(tk.INSERT, "Click here to change text")
        self.text.grid(row=2, column=0)

        self.idcanvas = tk.Canvas(self, highlightthickness=0)
        self.idcanvas.grid(row=3)

        tk.Label(self.idcanvas, text="Send To (id)").grid(row=0)
        self.id = tk.Entry(self.idcanvas)
        self.id.grid(row=0, column=1)
        tk.Label(self.idcanvas, text=" ").grid(row=0, column=2)

        ttk.Button(self, text="Spam Messages", command=self.sendMessage).grid(row=4, column=0)

    def login(self):
        self.bot = MessengerBot(self.email.get(), self.password.get())
        self.bot.login()
        for (name, id) in self.bot.getChatIDs():
            print("{:>50}   {:>20}".format(name, id))

    def sendMessage(self):
        message = self.text.get('1.0', tk.END).splitlines()
        for line in message:
            self.bot.sendChatMessage(chatid=self.id.get(), message=line)


if __name__ == '__main__':
    app = Application()

    hello_banner = pyfiglet.figlet_format("Hello")
    print(hello_banner)

    app.mainloop()