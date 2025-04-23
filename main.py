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
from chatbot import ChatBot
from time import strftime
from datetime import datetime
from help import Help

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        


    #first image
        img1 = Image.open(r"D:\Face Recognition app\photos\3.png")
        img1 = img1.resize((400, 100))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=25, y=15, width=400, height=100)

    #second image

        #img2 = Image.open(r"D:\Face Recognition app\photos\2.png")
        #img2 = img2.resize((500, 130), Image.LANCZOS)
        #self.photoimg2 = ImageTk.PhotoImage(img2)

        #f_lbl = Label(self.root, image=self.photoimg2)
        #f_lbl.place(x=500, y=0, width=500, height=130)

    #third image
       # img3 = Image.open(r"D:\Face Recognition app\photos\3.png")
       # img3 = img3.resize((500, 130))
       # self.photoimg3 = ImageTk.PhotoImage(img3)
 
       # f_lbl = Label(self.root, image=self.photoimg3)
       # f_lbl.place(x=1000, y=0, width=500, height=130)

    #background image
        img4 = Image.open(r"D:\Face Recognition app\photos\bg.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",20,"bold"),fg="red")
        title_lbl.place(x=425,y=50,width=1040,height=45)

        #time
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_lbl,font=('time new roman',14,'bold'),background='white',foreground='black')
        lbl.place(x=870,y=0,width=150,height=50)
        time()

        #student button
        img5 = Image.open(r"D:\Face Recognition app\photos\students.jpg")
        img5 = img5.resize((215, 215), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

         #Detect Face button
        img6 = Image.open(r"D:\Face Recognition app\photos\facial.jpeg")
        img6 = img6.resize((215, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendance button
        img7 = Image.open(r"D:\Face Recognition app\photos\attendance.jpg")
        img7 = img7.resize((215, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #help Button
        img8 = Image.open(r"D:\Face Recognition app\photos\chatbot.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.chatbot_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="ChatBot",cursor="hand2",command=self.chatbot_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #train data button
        img9 = Image.open(r"D:\Face Recognition app\photos\traindata1.png")
        img9 = img9.resize((215,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=550,width=220,height=40)

        #photos button
        img10 = Image.open(r"D:\Face Recognition app\photos\photos.jpg")
        img10 = img10.resize((215, 220), Image.LANCZOS)
        self.photoimg10= ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=550,width=220,height=40)
        
        #Developer Button
        img11 = Image.open(r"D:\Face Recognition app\photos\contactus.jpg")
        img11 = img11.resize((215, 220), Image.LANCZOS)
        self.photoimg11= ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.help_data)
        b1.place(x=800,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="Contact Us",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=550,width=220,height=40)

        #Exit Button
        img12 = Image.open(r"D:\Face Recognition app\photos\exit.jpg")
        img12 = img12.resize((215, 220), Image.LANCZOS)
        self.photoimg12= ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=550,width=220,height=40)

        #function Buttons

    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)
        
    def open_img(self):
        os.startfile("data")

    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)

    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_recognition(self.new_window)

    def attendance_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendence(self.new_window)

    def chatbot_data(self):
         self.new_window=Toplevel(self.root)
         self.app=ChatBot(self.new_window)

    def help_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Help(self.new_window)
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure You Want to Exit!",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    
        











if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
