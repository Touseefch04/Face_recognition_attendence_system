import cv2
import mysql.connector
import numpy as np
import os
import csv
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import threading

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"D:\Face Recognition app\photos\faceiner.jpg").resize((650, 730))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=48, width=650, height=730)

        img_bottom = Image.open(r"D:\Face Recognition app\photos\faceinner.jpg").resize((950, 730))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=48, width=950, height=730)

        b1_1 = Button(f_lbl, text="Face Recognition", command=self.start_video_stream, cursor="hand2", 
                      font=("times new roman", 18, "bold"), bg="red", fg="white")
        b1_1.place(x=360, y=650, width=200, height=35)

    def start_video_stream(self):
        threading.Thread(target=self.face_recognition, daemon=True).start()

    def mark_attendance(self, student_id, roll, name, department):
        """Marks attendance only ONCE per day for each student"""
        file_path = "record.csv"
        today_date = datetime.now().strftime("%d/%m/%Y")

        # Ensure file exists and create header if not present
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Roll", "Name", "Department", "Time", "Date", "Status"])  # CSV Header

        # Check if attendance is already marked today
        marked_students = set()
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            rows = list(reader)  # Read all rows into memory
            if len(rows) > 1:  # Check if file contains more than just the header
                for row in rows[1:]:  # Skip the header row
                    if row and row[0] == str(student_id) and row[5] == today_date:
                        marked_students.add(student_id)

        if student_id not in marked_students:
            now_time = datetime.now().strftime("%H:%M:%S")
            with open(file_path, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([student_id, roll, name, department, now_time, today_date, "Present"])
            print(f"✔ Attendance marked for {name} at {now_time}")
        else:
            print(f"⚠ {name} is already marked today.")

    def face_recognition(self):
        """Handles face recognition and attendance marking"""
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)

            for (x, y, w, h) in faces:
                face = gray[y:y+h, x:x+w]
                id, confidence = clf.predict(face)
                confidence = int(100 * (1 - confidence / 300))

                if confidence > 75:  # Face recognized
                    try:
                        conn = mysql.connector.connect(
                            host="localhost", port=3309, user="root", password="123456ch",
                            database="face_recognizer", auth_plugin='mysql_native_password'
                        )
                        my_cursor = conn.cursor()

                        my_cursor.execute(f"SELECT id, roll, name, dep FROM student WHERE id={id}")
                        result = my_cursor.fetchone()
                        conn.close()

                        if result:
                            student_id, roll, name, department = result
                            cv2.putText(img, f"ID: {student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Dept: {department}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                            self.mark_attendance(student_id, roll, name, department)
                        else:
                            cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

                    except mysql.connector.Error as e:
                        print(f"❌ Database Error: {e}")
                
                else:
                    cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
