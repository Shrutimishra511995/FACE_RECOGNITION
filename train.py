from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")



        TITLE_LBL=Label(self.root,text="TRAIN DATA SET",font=("times new roman",40,"bold"),bg="darkblue",fg="red")
        TITLE_LBL.place(x=0,y=0,width=1530,height=45)


        
        img_top=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\student3.jpg")
        img_top=img_top.resize((1530,320),Image.ANTIALIAS) 
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=320)

        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="purple",fg="green")
        b1_1.place(x=0,y=375,width=1530,height=60)


        img_bottom=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\student3.jpg")
        img_bottom=img_bottom.resize((1530,320),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=450,width=1530,height=320)



    def train_classifier(self):
        data_dir=("data")#data sample is stored in data_dir(dir=directory),working directory is data
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        #path ko join kra h upar os.path.join se data_dir ko file se,file os.listdir mai chlega jo hume sara data file mai ladega list ki form mai data_dir se (LIST COMPREHENSION IS DONE)............ 

        faces=[]
        ids=[]

        for image in path:     #sara data jo path mai tha wo humne image mai lelia
            img=Image.open(image).convert("L")  # grayscale image
            imageNp=np.array(img,"uint8")#uint8 is datatype in array
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitkey(1)==13#waitkey is a function in cv2 which help in exiting by pressing enter
        ids=np.array(ids)#np(numpy)is used coz it gives 88% more accurately of conversion of image into array



        #========================Train the classifer and save ============================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !!")

        




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()