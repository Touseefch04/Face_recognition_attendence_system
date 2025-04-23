from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import CAP_ANDROID
import mysql.connector
import cv2
from datetime import datetime


class Student:
    id1=StringVar
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        #  variable
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_professor=StringVar()
       


     #first image
        img1 = Image.open(r"D:\Face Recognition app\photos\3.png")
        img1 = img1.resize((400, 100))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=25, y=15, width=400, height=100)


    #bg image

        

        img4 = Image.open(r"D:\Face Recognition app\photos\bg.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(self.root,text="Student Details",font=("times new roman",30,"bold"),fg="red")
        title_lbl.place(x=550,y=50,width=800,height=45)

        #frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=30,width=1500,height=600)

        #left side labal frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)


        img_left = Image.open(r"D:\Face Recognition app\photos\studentiner.jpg")
        img_left = img_left.resize((750, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=130)
        #currnt course
        currnt_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Currunt Course Information",font=("times new roman",12,"bold"))
        currnt_course_frame.place(x=5,y=135,width=750,height=150)
        #department
        dep_label=Label(currnt_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(currnt_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Bachelor","Master","Admistration","M.phil","Mechanical Enginering","Electrical Enginering","Civil Enginering","PHD")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        dep_label=Label(currnt_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(currnt_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Course","Information Techonlogy","Software Engineering","Computer Science","Electrical Electronics","Electrical Power","Litrature","physics","Chemistry","Botnay","Zoology","Business")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        dep_label=Label(currnt_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(currnt_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Year","2019-2023","2020-2024","2021-2025","2022-2026","2023-2027","2024-2028","2025-2029","2026-2030")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        dep_label=Label(currnt_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(currnt_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=250,width=750,height=300)

        #studentID
        studentId_label=Label(class_Student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        classDivison_label=Label(class_Student_frame,text="Student Divison:",font=("times new roman",12,"bold"),bg="white")
        classDivison_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"]=("Select Division","A","B","C","D","E")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #roll number
        Rollnumber_label=Label(class_Student_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        Rollnumber_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Rollnumber_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        Rollnumber_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"]=("Select Gender","Male","Female","Not Specified","Other")
        div_combo.current(0)
        div_combo.grid(row=2,column=1,padx=10,pady=8,sticky=W)

        #date of birth
        dateofbirth_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dateofbirth_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dateofbirth_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dateofbirth_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone number
        phone_label=Label(class_Student_frame,text="Phone Number:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Professor Name
        professorname_label=Label(class_Student_frame,text="Professor Name:",font=("times new roman",12,"bold"),bg="white")
        professorname_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        professorname_entry=ttk.Entry(class_Student_frame,textvariable=self.var_professor,width=20,font=("times new roman",12,"bold"))
        professorname_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn1.grid(row=6,column=1)

        #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=720,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="White")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="blue",fg="White",command=self.update_data)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=19,font=("times new roman",12,"bold"),bg="blue",fg="White",command=self.delete_data)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=19,font=("times new roman",12,"bold"),bg="blue",fg="White",command=self.reset_data)
        reset_btn.grid(row=0,column=3)

        #last 2 Buttons

        btn2_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn2_frame.place(x=0,y=240,width=720,height=35)

        takesample_btn=Button(btn2_frame,text="Take Photo Sample",width=39,font=("times new roman",12,"bold"),bg="blue",fg="White",command=self.generate_dataset)
        takesample_btn.grid(row=1,column=0)

        updatephoto_btn=Button(btn2_frame,text="Update Photo Sample",command=self.generate_dataset,width=39,font=("times new roman",12,"bold"),bg="blue",fg="White")
        updatephoto_btn.grid(row=1,column=1)

         #right side labal frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=710,height=580)

        img_right = Image.open(r"D:\Face Recognition app\photos\studentinner.jpeg")
        img_right = img_right.resize((750, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=750, height=130)

        #search frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=130,width=700,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll Number","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="White")
        Search_btn.grid(row=0,column=3,padx=5)

        showall_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="White")
        showall_btn.grid(row=0,column=4,padx=5)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=205,width=700,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","semester","id","name","div","roll","gender","dob","phone","email","address","professor","photo"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("professor",text="Professor")
        self.student_table.heading("photo",text="PhotoSampleStatus")

        self.student_table["show"]="headings"

       
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100) 
        self.student_table.column("address",width=100)
        self.student_table.column("professor",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #function Declaration

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                # Convert the date to the correct format (YYYY-MM-DD)
                formatted_date = datetime.strptime(self.var_dob.get(), "%d/%m/%Y").strftime('%Y-%m-%d')
            except ValueError:
                messagebox.showerror("Error", "Invalid Date Format. Please use DD/MM/YYYY", parent=self.root)
                return
            try:
                conn=mysql.connector.connect(host="localhost",port=3309,user="root",password="123456ch",database="face_recognizer",auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            formatted_date,
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_professor.get(),
                                                                                                            self.var_radio1.get()

                                                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student Details are Added Sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",port=3309,user="root",password="123456ch",database="face_recognizer",auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()

    #cursor Focus
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_professor.set(data[13]),
        self.var_radio1.set(data[14])
        
        #update  data
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                confirmed = messagebox.askyesno("Update", "Do You Want to Update This Student Detail", parent=self.root)
                if confirmed:
                    conn = mysql.connector.connect(
                    host="localhost",
                    port=3309,
                    user="root",
                    password="123456ch",
                    database="face_recognizer",
                    auth_plugin='mysql_native_password'
                )
                my_cursor = conn.cursor()
                sql = """UPDATE student SET dep=%s, course=%s, `year`=%s, semester=%s, name=%s, `div`=%s, roll=%s,
                         gender=%s, dob=%s, email=%s, phone=%s, address=%s, professor=%s, photo=%s WHERE id=%s"""
                values = (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_professor.get(),
                    self.var_radio1.get(),
                    self.var_id.get()
                )
                my_cursor.execute(sql, values)
                conn.commit()
                messagebox.showinfo("Success", "Student Detail Successfully Updated", parent=self.root)
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #delete data
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID must be Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do You Want to Delete this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",port=3309,user="root",password="123456ch",database="face_recognizer",auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Detail Deleted Sucessfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #reset data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_professor.set("")
        self.var_radio1.set("")

        
        # Generate Data set and photo sample
    def generate_dataset(self):
        def calculate_confidence_score(face):
           
            pass

        def analyze_confidence_scores(scores):
            
            pass
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
            
        else:
            try:
                conn = mysql.connector.connect(
                host="localhost",port=3309, user="root", password="123456ch", database="face_recognizer",
                auth_plugin='mysql_native_password'
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
              
                id1=self.var_id.get()
               

                my_cursor = conn.cursor()
                sql = """UPDATE student SET dep=%s, course=%s, `year`=%s, semester=%s, name=%s, `div`=%s, roll=%s,
                     gender=%s, dob=%s, email=%s, phone=%s, address=%s, professor=%s, photo=%s WHERE id=%s"""
                values = (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_professor.get(),
                self.var_radio1.get(),
                self.var_id.get()
                )
                my_cursor.execute(sql, values)
                conn.commit()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                confidence_scores = []
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                    return face_cropped

                img_id = 0
     
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    messagebox.showerror("Error", "Failed to open webcam")
                    return
                

                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        messagebox.showerror("Error", "Failed to capture frame from webcam")
                        break

                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{id1}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                        confidence_scores.append(confidence_scores)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Data Set Complete!")
                best_threshold = analyze_confidence_scores(confidence_scores)
                messagebox.showinfo("Best Threshold", f"The best confidence threshold is: {best_threshold}")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

        
        




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
