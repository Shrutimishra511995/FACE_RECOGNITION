from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import BaseCascadeClassifier
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")


        tittle_lb1=Label(self.root,text="FACE RECOGNITION",font=("times new roman",40,"bold"),bg="darkblue",fg="red")
        tittle_lb1.place(x=0,y=0,width=1530,height=50)


        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\detect.jfif")
        img2=img2.resize((650,700),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=55,width=650,height=700)
        

        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\developer.jpg")
        img3=img3.resize((950,700),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=650,y=55,width=950,height=700)

        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="yellow",fg="darkblue")
        b1_1.place(x=365,y=620,width=200,height=40)

        #=========================attendance====================

    def mark_attendence(self,i,r,n,d):
        with open("Shruti.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))   
                name_list.append(entry[0])
            if((i not in name_list)and(r not in name_list)and(n not in name_list)and(d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%n/%y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")

                   

        #================face recognition=======================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf): #
            gray_image=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB) #cvtcolor Converts an image from one color space to another
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors) #Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles

            coord=[]
#below for loop need to understand
            for(x,y,w,h) in features:
                cv2.rectangle(img[x,y],(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300))) #predict() function enables us to predict the labels of the data values on the basis of the trained model. The predict() function accepts only a single argument which is usually the data to be tested

                conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="face_recognizer")#we have to pass a tuple and 4 values in it coz its required when connecting with database to work with.
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dept from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone() #fetchone() Method. This method retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available. By default, the returned tuple consists of data returned by the MySQL server, converted to Python objects
                i="+".join(i)





                if confidence>77: #Confidence interval for a mean is a range of values that is likely to contain a population mean with a certain level of confidence
                    cv2.putText(img,f"Student_id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    #(x,y-75) is used to fit the student id , we need it on the top of rectangle thats why we used minus sign
                    #0.8 is the font scale
                    #(255,255,255) is the color given to font 
                    #3 is the thickness of font
        
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.markattendence(i,r.n.d)
                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)    
                coord=[x,y,w,h]
                
                return coord
        def recognize(img,clf,faceCascade): #clf is classifier
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"faces",clf) 
            return img

        facecascade=cv2.CascadeClassifier("classifier.xml")

        clf=cv2.face.LBPHFaceRecognizer_create() #A real time face-detection application using LBPH. The application is developed in python using libraries such as OpenCV for computer vision. The application can register a face and perform detection for all the faces registered
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
                                      
            img=recognize(img,clf,facecascade)
            cv2.imshow("welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()

                        

         
if __name__ == "__main__":
     root=Tk()
     obj=Face_Recognition(root)
     root.mainloop()