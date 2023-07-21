import imghdr
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        # ********** variables **************
        self.var_dept=StringVar()#bcoz calculations nhi krni h isliye stringVar mai define kra h
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        #first image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\logo.jfif")
        img=img.resize((500,130),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
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
        img3=img3.resize((1530,710),Image.ANTIALIAS)#antialias high quality image ko low qualiity image pe set krta h
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        TITLE_LBL=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="darkblue",fg="red")
        TITLE_LBL.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1480,height=600)


        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580) 
        
        img_left=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\student3.jpg")
        img_left=img_left.resize((550,130),Image.ANTIALIAS) #antialias high quality image ko low qualiity image pe set krta h
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130 )

        #current course
        Current_Course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_Course_frame.place(x=5,y=135,width=720,height=150) 


        #department
        dep_label=Label(Current_Course_frame,text="Department",font=("times new roman",13,"bold"),background="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_dept,font=("times new roman",13,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Information Technology","Electrical","Mechanical","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(Current_Course_frame,text="Course",font=("times new roman",13,"bold"),background="white")
        course_label.grid(row=0,column=2,padx=10)

        Course_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=17,state="readonly")
        Course_combo["values"]=("Select Course","FE","SE","TE","BE")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(Current_Course_frame,text="Year",font=("times new roman",13,"bold"),background="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(Current_Course_frame,text="Semester",font=("times new roman",13,"bold"),background="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class student information
        Class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=250,width=720,height=300) 

        #student id
        studentid_label=Label( Class_Student_frame,text="Student ID:",font=("times new roman",13,"bold"),background="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        studentid_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentname_label=Label( Class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),background="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        studentname_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label( Class_Student_frame,text="Class Division:",font=("times new roman",13,"bold"),background="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=17,state="readonly")
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #roll no
        roll_no_label=Label( Class_Student_frame,text="Roll No:",font=("times new roman",13,"bold"),background="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)


        roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label( Class_Student_frame,text="Gender:",font=("times new roman",13,"bold"),background="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)


       #gender_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=17,state="readonly")
        gender_combo["values"]=("Select","Male","Other","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #DOB
        DOB_label=Label( Class_Student_frame,text="DOB:",font=("times new roman",13,"bold"),background="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)


        DOB_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)




        #Email
        email_label=Label( Class_Student_frame,text="Email:",font=("times new roman",13,"bold"),background="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)


        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phono no
        phone_label=Label( Class_Student_frame,text="Phone No:",font=("times new roman",13,"bold"),background="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)


        phone_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label( Class_Student_frame,text="Address:",font=("times new roman",13,"bold"),background="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)


        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name
        teacher_label=Label( Class_Student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),background="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)


        teacher_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take A Photo Sample",value="yes")
        radionbtn1.grid(row=6,column=0)
    
        
        radionbtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)

        #button frame

        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_btn.grid(row=0,column=0)

        reset_btn=Button(btn_frame1,text="Reset Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2)





        #right label frame
        
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580) 

        img_right=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recoganation\collegeimages\students2.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS) #antialias high quality image ko low qualiity image pe set krta h
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)


# ==========================Search SYstem===============================
        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70) 
        
        
        phone_label=Label( Search_frame,text="Search by:",font=("times new roman",13,"bold"),background="pink")
        phone_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll_no","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=14,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)



        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5)
        

        #======================table frame===============================
        Table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=210,width=710,height=340) 

        Scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)

        Scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)     

        self.student_table=ttk.Treeview(Table_frame,column=("dept","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=Scroll_y.set,yscrollcommand=Scroll_y.set)
       
       
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Divison")
        self.student_table.heading("roll",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo_sample_status")

        self.student_table["show"]="headings"
        
        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
    
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
# ==================================function declarations=============================================
    def add_data(self):
        if self.var_dept.get()=="Select Department"  or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)#parent=self.root we setted this coz the error should not go on the other window and should stay on this window only.
        else:    
          
            try :
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")#we have to pass a tuple and 4 values in it coz its required when connecting with database to work with.
                my_cursor = conn.cursor()#cursor() --- is an inbuilt func which helps in executing the queries of mysql
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_dept.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.var_std_id.get(),
                                                                                    self.var_std_name.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_email.get(),
                                                                                    
                                                                                    self.var_phone.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_teacher.get(),
                                                                                    self.var_radio1.get()
                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                ))
        #"%s"-- is used to pass values in  to the query by adding it into the window        
                conn.commit()
                self.fetch_data()
                conn.close
                messagebox.showinfo("Success","Stundent details has been added Successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
#=======================================fetch database===========================================
            def  fetch_data(self) :
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")#we have to pass a tuple and 4 values in it coz its required when connecting with database to work with.
                my_cursor = conn.cursor()#cursor() --- is an inbuilt func which helps in executing the queries of mysql        
                my_cursor.execute("select * from student")
                data=my_cursor.fetch    

                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
                conn.close()    

# ===================================get cursor==============================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #update function
    def update_data(self):
        if self.var_dept.get()=="Select Department"  or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="face_recognizer")#we have to pass a tuple and 4 values in it coz its required when connecting with database to work with.
                    my_cursor = conn.cursor()
                    my_cursor.execute(("update student set dept=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s"),(

                                                                                        self.var_dept.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_std_id.get(),
                                                                                        self.var_std_name.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_radio1.get()
                                                                                                ))
                else:
                    if not Update:
                        return    
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()        
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

#delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
            
                delete=messagebox.askyesno("Stundent Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="face_recognizer")#we have to pass a tuple and 4 values in it coz its required when connecting with database to work with.
                    my_cursor = conn.cursor()
                    sql="Delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:    
                messagebox.showinfo("Delete","Successfully Deleted student details",parent=self.root)    

#reset data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
                    

    #=====================generate data set or take photo sample=========================
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department"  or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                    messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="face_recognizer")#we have to pass a tuple and 4 values in it coz its required when connecting with database to work with.
                        my_cursor = conn.cursor()
                        my_cursor.execute("select * from student")
                        myresult=my_cursor.fetchall()
                        id=0
                        for x in myresult:
                            id+=1
                        my_cursor.execute(("update student set dept=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s"),(

                                                                                            self.var_dept.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()==id+13
                                                                                                    ))
                        conn.commit()     
#commit() Method, This method sends a COMMIT statement to the MySQL server, committing the current transaction. Since by default Connector/Python does not autocommit, it is important to call this method after every transaction that modifies data for tables that use transactional storage engines
                        self.fetch_data()
                        self.reset_data()
                        conn.close()
    # =======================load predifined data on face frontal from open cv=================
                    
                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                        def face_cropped(img):
                            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            face=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #minimum neighbour=5

                        for (x,y,w,h) in face:
                            face_cropped=imghdr[y:y+h,x:x+w]
                            return face_cropped

                        cap=cv2.VideoCapture(0)
                        img_id=0
                        while True:
                            ret,my_frame=cap.read()
                            if face_cropped(my_frame) is not None:
                                img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor1(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)
                            
                            if cv2.waitKey(1)==13 or int(img_id)==100:
                                break
                        cap.release()
                        #release() is an inbuilt method of the Lock class of the threading module in Python. This method releases the lock which was earlier acquired by a thread. Once the lock is released, only then can it be acquired by another thread. This can be called from any thread, not just from the thread that acquired it
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Generating Data Set Compled!!!!")
            except Exception as es:    
                    messagebox.showinfo("Delete","Successfully Deleted student details",parent=self.root)



if __name__ == "__main__":
     root=Tk()
     obj=Student(root)
     root.mainloop()
        