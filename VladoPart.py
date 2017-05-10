from tkinter import *
from tkinter import font
import random
from web_scraping import date_list

from tkinter import *
from tkinter import font
import random
from web_scraping import date_list


class App():
    def __init__(self, master):
        self.myString = StringVar()
        self.myString.set("Choose Your Date")
        self.myString2 = StringVar()
        self.myString2.set("Choose Your Movie")
        self.myString3 = StringVar()
        self.myString3.set("Choose Your Month")

        self.title_font = font.Font(family="Comic Sans MS", size=17)
        self.new_font = font.Font(family="Comic Sans MS", size=23)

        self.choose_day = OptionMenu(master, self.myString, *date_list()).grid(row="2", column="2")

        self.submit_button = Label(text="Choose Date", bg="lightblue", fg="black")
        self.submit_button.bind('<Button-1>', self.continuemov)
        self.submit_button.grid(row="2", column="3")

        self.choose_movie = OptionMenu(master, self.myString2, date_list())

    def continuemov(self, master):
        self.choose_movie.grid(row="3", column="2")

        # if self.myString!="Choose Your Date":
        # self.choose_movie=OptionMenu(master,self.myString2)


if __name__ == "__main__":
    root = Tk()
    root.title("Movie Scheduler")
    my_app = App(root)

    root.mainloop()

