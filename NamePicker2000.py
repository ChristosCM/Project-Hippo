# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:22:49 2017

@author: chris
"""

import tkinter
import random
names=['Bart','Fart','Paul','Dickinson','GoldenBalls69','Hero--1','InsertNameHere','TheOneWhoShallNotBeNamed','Name9','Finalist']
def pickName():
    nameLabel.configure(text=random.choice(names))
root = tkinter.Tk()
root.title("Name Picker2000")
root.geometry("600x100")
nameLabel = tkinter.Label(root, text="", font=('Helvetica', 32))
nameLabel.pack()
pickButton = tkinter.Button(text="Pick!", command=pickName)
pickButton.pack()
root.mainloop()