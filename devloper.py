from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2

class Developer:
   def __init__(self, root):
       self.root=root
       self.root.geometry("1530x790+8+8")
       self.root.title("face Recogniton System")

       title_lbl=Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"),bg="white",fg="red")
       title_lbl.place(x=0,y=0, width=1530,height=45)

       img_top=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\developer.jpg") 
       img_top=img_top.resize((1538,728), Image. ANTIALIAS) 
       self.photoimg_top=ImageTk.PhotoImage(img_top)

       f_lbl=Label(self.root, image=self.photoimg_top) 
       f_lbl.place(x=0,y=55,width=1530,height=720)
       

       #frame

       main_frame=Frame(f_lbl,bd=2)
       main_frame.place(x=1000,y=0,width=500,height=700)

       img_top1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\shruti.jpeg") 
       img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
       self.photoimg_top1=ImageTk.PhotoImage(img_top1)


       f_lbl=Label(main_frame, image=self.photoimg_top1) 
       f_lbl.place(x=300,y=0,width=200,height=200)

       dev_label=Label(main_frame,text="Hello My Name Is Shruti",font=("times new roman",20,"bold"),bg="white")
       dev_label.place(x=0,y=5)

       #dev_label=Label(main_frame,text="I Am Full Stack Developer",font=("times new roman",18,"bold"),bg="white")
       #dev_label.place(x=1,y=40)

       img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\AI-model.jpg") 
       img2=img2.resize((500,390),Image.ANTIALIAS)
       self.photoimg2=ImageTk.PhotoImage(img2)


       f_lbl=Label(main_frame, image=self.photoimg2) 
       f_lbl.place(x=0,y=210,width=500,height=390)



       






if __name__ == "__main__":
     root=Tk()
     obj=Developer(root)
     root.mainloop()