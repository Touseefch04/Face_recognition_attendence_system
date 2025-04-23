from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import CAP_ANDROID
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

mydata = []
class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        title_lbl=Label(self.root,text="Contact To Developer For Paid Work",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
         
        img1 = Image.open(r"D:\Face Recognition app\photos\helpinner.jpg")
        img1 = img1.resize((1570, 730))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=50, width=1570, height=730)

        img3 = Image.open(r"D:\Face Recognition app\photos\helpinner1.png")
        img3 = img3.resize((55, 40))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=530, y=365, width=55, height=40)

        title_lbl=Label(self.root,text="Touseefchaudary487@gmail.com",font=("times new roman",18,"bold"),bg="white",fg="red")
        title_lbl.place(x=590,y=370,width=400,height=45)

        title_lbl=Label(self.root,text="0335-1560487",font=("times new roman",18,"bold"),bg="white",fg="red")
        title_lbl.place(x=520,y=410,width=520,height=45)

        img2 = Image.open(r"D:\Face Recognition app\photos\helpiner.png")
        img2 = img2.resize((45, 45))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=630, y=410, width=45, height=45)





if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
