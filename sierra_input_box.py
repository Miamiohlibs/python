#testing box from https://likegeeks.com/python-gui-examples-tkinter-tutorial/
from tkinter import *


def windo():
	window = Tk()
	 
	window.title("Sierra input box")
	 
	lbl = Label(window, text="Hello")
	 
	lbl.grid(column=0, row=0)
	
	window.geometry('350x200')
	 
	window.mainloop()
	
