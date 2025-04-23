from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from attendence import Attendence
from help import Help
from time import strftime
from datetime import datetime

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        img1 = Image.open(r"D:\Face Recognition app\photos\developerin.jpg")
        img1 = img1.resize((680, 790))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=680, height=790)


        img2 = Image.open(r"D:\Face Recognition app\photos\developer.jpg")
        img2 = img2.resize((680, 790))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=680, y=0, width=425, height=395)


        img3 = Image.open(r"D:\Face Recognition app\photos\developer.jpg")
        img3 = img3.resize((680, 790))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1105, y=3955, width=425, height=395)




if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()