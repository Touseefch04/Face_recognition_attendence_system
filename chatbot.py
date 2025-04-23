from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("780x660+0+0")
        self.root.bind('<Return>',self.enter_func)
        

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat = Image.open(r"D:\Face Recognition app\photos\chatbotinner.jpg")
        img_chat = img_chat.resize((200, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_Lable=Label(main_frame,bd=3,relief=RAISED,anchor="nw",compound=LEFT,width=780,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
        Title_Lable.pack(side=TOP)

        #scroll Y
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=20,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        #Button frame
        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        lebel_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        lebel_1.grid(row=0,column=0,padx=5,sticky=W)


        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('time new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',15,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,command=self.clear_data,text="Clear Data",font=('arial',15,'bold'),width=8,bg='red')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.lebel_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.lebel_11.grid(row=1,column=1,padx=5,sticky=W)

        #FUNCTION declaration
     
    def enter_func(self):
        self.send.invoke()
        self.entry.set('')
    
    def clear_data(self):
        self.text.delete('1.0',END)
        self.entry.set('')


    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if(self.entry.get()==''):
            self.msg='Please Enter Some Input'
            self.lebel_11.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.lebel_11.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')
        elif(self.entry.get()=='how are you'):
            self.text.insert(END,'\n\n'+'Bot: I am Good.What About You?')
        elif(self.entry.get()=='i am also good'):
            self.text.insert(END,'\n\n'+'Bot: Great! How Can i Assist You Today?')
        elif(self.entry.get()=='problem relevent to student details'):
            self.text.insert(END,'\n\n'+'Bot: What Kind Of Problem You Facing \n\n1: Dependency Errors\n2: Database Connection Issues\n3: Incorrect or Missing Data\n4: Photo Capture and Dataset Generation\n4: UI Responsiveness\n5: Image Path Issues\n6:Data Retrieval and Search\n\n If You are Having Relevent Problem Type "student solution" ')
        elif(self.entry.get()=='student solution'):
            self.text.insert(END,'\n\n'+'Bot: Solution Is Given Below:\n1:Dependency Errors: Ensure that all required libraries\n are installed and properly configured.\n2:Database Connection Issues: Verify the correctness of \ndatabase connection details (host, username, password) \nand ensure the database server is running.\n3: Incorrect or Missing Data: Implement proper validation checks\n to ensure all required fields are filled with\n correct data before performing operations.\n4: Photo Capture and Dataset Generation: Check webcam compatibility,\n access permissions, and image processing algorithms\n for correct image capture \nand dataset generation.\n5: UI Responsiveness: Optimize image processing and webcam capture \nto maintain smooth UI responsiveness.\n6: Image Path Issues: Validate and ensure that the \nspecified image path for saving the dataset is valid\n and has write permissions.')    
        elif(self.entry.get()=='problem relevent to traindata'):
            self.text.insert(END,'\n\n'+'Bot: What Kind Of Problem You Facing \n\n 1:Missing dataset directory\n2: Unable to open images\n3: Image conversion errors\n4: Failure to save classifier\n\n If You Having Relevent Problem Type" traindata solution"')
        elif(self.entry.get()=='traindata solution'):
            self.text.insert(END,'\n\n'+'Bot: Solution Is Given Below:\n1: Dataset Directory Availability: Ensure the dataset directory is \navailable and accessible.\n2:File Permission and Format: Check file permissions and\n ensure the images are in the correct format.\n3: Image Conversion Process: Verify the image conversion process and\n handle any potential errors.\n4: Saving Classifier: Check write permissions and \nfile paths when saving the classifier.')    
        elif(self.entry.get()=='problem relevent to face recognition'):
            self.text.insert(END,'\n\n'+'Bot: What Kind of Problem You Facing\n\n1: Database Connection Error\n2: Missing Haar Cascade XML file\n3: Invalid File Paths for Images\n4: Camera not Accessible\n\n If You Having Relevent Problem Type" recognition solution" ')
        elif(self.entry.get()=='recognition solution'):
            self.text.insert(END,'\n\n'+'Bot: Solution Is Given Below:\n\n1: Database Connection Issue:Check database connection \ncredentials and network connectivity.\n2: Haar Cascade XML File Missing:Make sure the Haar Cascade XML file\n is present in the specified path.\n3: Incorrect or Inaccessible Image Paths:Verify that the file paths for images\m are correct and accessible.\n4: Camera Access Issue:Ensure that the camera is properly connected and\n accessible by the application.')
        elif(self.entry.get()=='problem relevent to attendence'):
            self.text.insert(END,'\n\n'+'Bot: What Kind Of Problem You Facing \n\n1: File Selection Error\n2: CSV Data Format Error\n3: Empty CSV Data\n4: Data Export Error\n\nIf You Having Relevent Problem Type" attendance solution"')
        elif(self.entry.get()=='attendance solution'):
            self.text.insert(END,'\n\n'+'Bot: Solution Is Given Below:\n\n1: File Selection Error: Users may face difficulties\n in selecting the desired CSV file for importing or exporting data.\n2: CSV Data Format Error: Users may encounter issues if\n the CSV file does not adhere to the expected format or structure,\n such as missing columns or incorrect data organization.\n3: Empty CSV Data: If the selected CSV file is empty or does not contain any data,\n users may face challenges in importing or exporting data.\n4: Data Export Error: Users may experience errors\n while exporting data to a CSV file,\n such as incorrect file path or insufficient permissions.')
        elif(self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: Bye! I am Always Here For You..')
        elif(self.entry.get()=='what is your name'):
            self.text.insert(END,'\n\n'+'Bot: My Name is Mr.Hacker')
        elif(self.entry.get()=='how this software work'):
            self.text.insert(END,'\n\n'+'Bot: First You Have to Enter Student Detail\nThen Take Phot Sample Of Student\nThen Train data\n Then Click on Face Recognition\n Then check Attendance in Attendance Button \n By imoorting CSV File')
        elif(self.entry.get()=='what is chatbot'):
            self.text.insert(END,'\n\n'+'Bot: A chatbot is a computer program or artificial intelligence (AI) \ntechnology that is designed to simulate human conversation and interact\n with users through text or voice-based interfaces.\n Chatbots use natural language processing (NLP) techniques\n to understand user inputs, interpret their intent,\n and provide appropriate responses or perform tasks.')
        elif(self.entry.get()=='help'):
            self.text.insert(END,'\n\n'+'Bot: Write Statment As it is:\n\nproblem relevent to student details\nproblem relevent to traindata\nproblem relevent to face recognition\nproblem relevent to attendence\n\nIf You Change Wording i Will Never Understand..!')
        elif(self.entry.get()=='who created you'):
            self.text.insert(END,'\n\n'+'Bot: Touseef Ch Created Me\nHe is Certified Expert of 11 Programming Language\nFor Software and Web Development\nContact: touseefchaudary487@gmail.com\n03351560487')
        else:
            self.text.insert(END,'\n\n'+'Bot: Sorry! I donot Understand\n Type "help" For Getting Commands..!')
        

        self.entry.set('')



if __name__=='__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()