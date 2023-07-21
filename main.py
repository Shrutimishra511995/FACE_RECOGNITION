from msilib.schema import SelfReg
from datetime import datetime
from time import strftime
from tkinter import* 
from tkinter import ttk
from tkinter import font
from train import Train
from Attendance import Attendance
from PIL import Image,ImageTk
from student import Student
from face_recognizer import Face_Recognition 
from devloper import Developer
from help import Help
import mysql.connector
import tkinter
import os





class Face_Recognition_System:
    def __init__(self,root): #"__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class
        self.root=root       #(self,root)here root is the name of window ,we can give name other than root also but by default it is root only 
        self.root.geometry("1530x790+0+0") #The self in keyword in Python is used to all the instances in a class. By using the self keyword, one can easily access all the instances defined within a class, including its methods and attributes
        #geometry is used to fit the window screen
        self.root.title("FACE RECOGNITION SYSTEM") #tittle is used to show tittle on webpage 

        #first image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\logo.jfif")
        img=img.resize((500,130),Image.ANTIALIAS) #(command=self.open_img)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg) #Label is used to specify the container box where we can place the text or images
        f_lbl.place(x=0,y=0,width=500,height=130)
         

        #second image
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\facialrecognition.jpg")
        img1=img1.resize((500,220),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

        #third image
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\college.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #background image
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\background.jpg")
        img3=img3.resize((1550,710),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        TITLE_LBL=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",40,"bold"),bg="darkblue",fg="red")
        TITLE_LBL.place(x=0,y=0,width=1530,height=50)

        def time():      
            string=strftime('%H:%M:%S %p') #strftime() function is used to convert date and time objects to their string representation
            lbl.config(text = string) # config() method is used for performing an overwriting over label widget
            lbl.after(1000, time) #after() method calls the callback function once after a delay milliseconds (ms) within Tkinter's main loop

        lbl = Label(TITLE_LBL, background = "darkblue",foreground="yellow")
        lbl.place(x=0,y=0, width=150,height=50) 
        time()
   

        #student button
        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\students2.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg4=ImageTk.PhotoImage(img4)

        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2") #hand2 is providing us cursor
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="yellow",fg="darkblue")
        b1_1.place(x=200,y=300,width=220,height=30)


        #detect face button
        img5=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\face-600x900.png")
        img5=img5.resize((500,220),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="FACE RECOGNITION",cursor="hand2",command=self.face_data,font=("times new roman",10,"bold"),bg="yellow",fg="darkblue")
        b1_1.place(x=500,y=300,width=220,height=30)



        #attendance button
        img6=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\unnamed.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b2.place(x=800,y=100,width=220,height=220)

        b1_3=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("times new roman",10,"bold"),bg="yellow",fg="darkblue")
        b1_3.place(x=800,y=300,width=220,height=30)



        #Help button
        img7=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\download.jfif")
        img7=img7.resize((350,220),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg7=ImageTk.PhotoImage(img7)

        b2=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b2.place(x=1100,y=100,width=220,height=220)

        b1_4=Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_data,font=("times new roman",10,"bold"),bg="yellow",fg="darkblue")
        b1_4.place(x=1100,y=300,width=220,height=30)


        #train data button

        img8=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\AI-model.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg8=ImageTk.PhotoImage(img8) # To save the image in variable we use self.photoimg8

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=350,width=220,height=220)

        b2_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",10,"bold"),bg="yellow",fg="darkblue")
        b2_1.place(x=200,y=550,width=220,height=30)


        #photos button
        img9=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\student.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg9=ImageTk.PhotoImage(img9)

        b2=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b2.place(x=500,y=350,width=220,height=220)


        b2_2=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",10,"bold"),bg="yellow",fg="darkblue")
        b2_2.place(x=500,y=550,width=220,height=30)

        #developer button

        img10=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg10=ImageTk.PhotoImage(img10)

        b2=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b2.place(x=800,y=350,width=220,height=220)

        b2_3=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("times new roman",10,"bold"),bg="yellow",fg="darkblue")
        b2_3.place(x=800,y=550,width=220,height=30)

        #exit button

        img11=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\exit.png")
        img11=img11.resize((220,220),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg11=ImageTk.PhotoImage(img11)

        b2=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b2.place(x=1100,y=350,width=220,height=220)

        b2_4=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",10,"bold"),bg="yellow",fg="darkblue")
        b2_4.place(x=1100,y=550,width=220,height=30) 

    def open_img(self):
        os.startfile("data")  #os. startfile() method allows us to “start” a file with its associated program
          

                                                                                            #command=self.attendance_data
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit ??",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return  
##############################functions buttons  #####################################
       
        

    def student_details(self):
        self.new_window=Toplevel(self.root) #The Toplevel widget is used to create and display the toplevel windows which are directly managed by the window manager. The toplevel widget may or may not have the parent window on the top of them
        self.app=Student(self.new_window) 


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)



if __name__ == "__main__": #calling main function
    root=Tk()                   #Tk() fuction helps to display the root window and manages all the other components of the tkinter application
    obj=Face_Recognition_System(root) #making class object and passing root in it to join the root
    root.mainloop()                #to close main loop 