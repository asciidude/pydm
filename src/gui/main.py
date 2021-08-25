from tkinter import *
from tkinter.ttk import Progressbar
from utils.download import download
import os

class Main(Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.create_labels()
            self.create_entrys()
            self.create_download_button()
        
        def create_labels(self):
            self.download_link = Label(self.master, text='Download Link')
            self.download_link.place(x=100, y=50)

            self.download_name = Label(self.master, text='Download Name')
            self.download_name.place(x=100, y=100)

            self.download_name = Label(self.master, text='Download progress\nshown in console')
            self.download_name.place(x=100, y=145)

        def create_entrys(self):
            self.download_link_entry = Entry(self.master)
            self.download_link_entry.place(x=200, y=50)

            self.download_name_entry = Entry(self.master)
            self.download_name_entry.place(x=200, y=100)

        def create_download_button(self):
            self.download_button = Button(self.master, text='Download File')
            self.download_button.bind('<Button-1>', self.start_download)
            self.download_button.place(x=240, y=150)

        def start_download(self, _):
            download(self.download_link_entry.get(), self.download_name_entry.get())

def show_main(*args, **kwargs):
    window = Tk()
    mywin = Main(master=window)
    
    window.resizable(False, False)
    window.title(kwargs.get('title') or 'pydm - Download Manager')
    window.geometry(kwargs.get('geometry') or '425x235')
    window.iconphoto(False, PhotoImage(file=f'{os.getcwd()}/images/ico.png'))

    window.mainloop()