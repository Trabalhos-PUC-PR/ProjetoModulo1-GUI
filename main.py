# dependencies: pycryptodomex, hashlib

import tkinter as tk
from passFileManager import *

def main():
    root = tk.Tk()

    root.title("new window title!")

    windowWidth = 1200
    windowHeight = 720
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    xCenter = int(screenWidth / 2 - windowWidth / 2)
    yCenter = int(screenHeight / 2 - windowHeight / 2)

    root.geometry(f'{windowWidth}x{windowHeight}+{xCenter}+{yCenter}')
    message = tk.Label(root, text="Hello World!").pack()

    root.resizable()
    root.minsize(300, 200)
    root.maxsize(1200, 720)
    
    img = tk.PhotoImage(file='./assets/book-icon.bmp')
    root.tk.call('wm', 'iconphoto', root._w, img)


    root.mainloop()
