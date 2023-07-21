from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import cv2

class Help:
   def __init__(self, root):
       self.root=root
       self.root.geometry("1530x790+8+8")
       self.root.title("Face Recogniton System")

       title_lbl=Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"),bg="white",fg="red")
       title_lbl.place(x=0,y=0, width=1530,height=45)

       img_top=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\help.jpg") 
       img_top=img_top.resize((1538,728), Image. ANTIALIAS) 
       self.photoimg_top=ImageTk.PhotoImage(img_top)

       f_lbl=Label(self.root, image=self.photoimg_top) 
       f_lbl.place(x=0,y=55,width=1530,height=720)

       dev_label=Label(f_lbl,text="Email:shrutimishra511995@gmail.com",font=("times new roman",20,"bold"),bg="white")
       dev_label.place(x=600,y=400)
       

       #frame

       #main_frame=Frame(f_lbl,bd=2)
       #main_frame.place(x=1000,y=0,width=500,height=700)

       #img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
       #img_top1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\shruti.jpeg") 
       #self.photoimg_top1=ImageTk.PhotoImage(img_top1)

       #f_lbl=Label(main_frame, image=self.photoimg_top1) 
       #f_lbl.place(x=300,y=0,width=200,height=200)



if __name__ == "__main__":
     root=Tk()
     obj=Help(root)
     root.mainloop()