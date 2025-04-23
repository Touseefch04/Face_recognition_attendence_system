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
class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        #variables
        self.var_att_id=StringVar()
        self.var_att_name=StringVar()
        self.var_att_roll=StringVar()
        self.var_att_date=StringVar()
        self.var_att_time=StringVar()
        self.var_att_dep=StringVar()
        self.var_att_attendance=StringVar()


         #first image
        img1 = Image.open(r"photos\3.png")
        img1 = img1.resize((400, 100))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=25, y=15, width=400, height=100)

    #background image
        img4 = Image.open(r"D:\Face Recognition app\photos\bg.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl=Label(self.root,text="Attendance Details",font=("times new roman",30,"bold"),fg="red")
        title_lbl.place(x=550,y=50,width=800,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=46,width=1530,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,text="Information",font=("comicsansns",12,"bold"),bd=2,bg="white",relief=RIDGE)
        Left_frame.place(x=5,y=5,width=760,height=580)

        

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=10,width=758,height=510)

        #LABEL AND ENTRY

        #id
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("comicsansns",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_att_id,width=20,font=("comicsansns",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        roll_label=Label(left_inside_frame,text="Roll Number:",font=("comicsansns",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_att_roll,font=("comicsansns",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #name
        name_label=Label(left_inside_frame,text="Name:",font=("comicsansns",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_att_name,font=("comicsansns",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Department
        department_label=Label(left_inside_frame,text="Department:",font=("comicsansns",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_att_dep,font=("comicsansns",12,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #time
        time_label=Label(left_inside_frame,text="Time",font=("comicsansns",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_att_time,font=("comicsansns",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #date
        date_label=Label(left_inside_frame,text="Date:",font=("comicsansns",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_att_date,font=("comicsansns",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #attendance status
        date_label=Label(left_inside_frame,text="Attendance Status:",font=("comicsansns",12,"bold"),bg="white")
        date_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_att_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=450,width=755,height=40)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=27,font=("times new roman",12,"bold"),bg="blue",fg="White")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",width=27,command=self.exportCsv,font=("times new roman",12,"bold"),bg="blue",fg="White")
        update_btn.grid(row=0,column=1)


        reset_btn=Button(btn_frame,text="Reset",width=27,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="White")
        reset_btn.grid(row=0,column=3)
        



        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=5,width=740,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=730,height=480)

        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")     
        self.AttendanceReportTable.heading("department",text="Department")      
        self.AttendanceReportTable.heading("time",text="Time")      
        self.AttendanceReportTable.heading("date",text="Date")  
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
############################################Fetch data########
    def fetchData(self,row):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in row:
            self.AttendanceReportTable.insert("",END,values=i)

    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len (mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root)
                return False
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.root)
            with open (fln,mode="w",newline="")as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)  

    #cursor focus
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_att_id.set(rows[0])
        self.var_att_roll.set(rows[1])
        self.var_att_name.set(rows[2])
        self.var_att_dep.set(rows[3])
        self.var_att_time.set(rows[4])
        self.var_att_date.set(rows[5])
        self.var_att_attendance.set(rows[6])


    #reset
    def reset_data(self):
        self.var_att_id.set("")
        self.var_att_roll.set("")
        self.var_att_name.set("")
        self.var_att_dep.set("")
        self.var_att_time.set("")
        self.var_att_date.set("")
        self.var_att_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()