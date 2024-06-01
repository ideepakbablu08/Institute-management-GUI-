from tkinter import *
from tkinter import messagebox,ttk
from PIL import ImageTk, Image
from tkinter import font
import tkinter.messagebox
import mysql.connector as mc

#window creation

win = Tk()
win.title("SLA - Softlogic Systems")
win.geometry('1500x700')
win.config(bd=20,relief="ridge",bg="paleturquoise")

path=r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\slapng.png"
bg = ImageTk.PhotoImage(Image.open(path))
b1=Label(win, image=bg)
b1.place(x=420,y=250)

#line

c= Canvas(win, width=2000, height=1, bg='black')
c.place(x=0,y=145)
c.create_line(0,100, 300, 100, width=2, fill='black')
#c.pack()

#image

img=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\student1.png"))
p1=Label(win, image=img,bg="paleturquoise")
p1.place(x=1090,y=240)

pic=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\social.png"))
p2=Label(win,image=pic,bg="paleturquoise")
p2.place(x=1200,y=630)

#logo
img2=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\IMG_7476.3.jpg"))
p2=Label(win, image=img2,bg="paleturquoise")
p2.place(x=0,y=0)

lb=Label(win, text='To get more info contact us:',font=("Book Antiqua",20,'bold'),bg="paleturquoise")
lb.place(x=450,y=580)
lb2=Label(win, text='📞 +91 86818 84318',font=("Calibri",18,'bold'),bg="paleturquoise")
lb2.place(x=460,y=630)
lb3=Label(win,text='📩 enquiry@softlogicsys.in',font=("Calibri",18,'bold','underline'),bg="paleturquoise")
lb3.place(x=460,y=670)
lb2=Label(win, text='☎ 44 1800 1800',font=("Calibri",18,'bold'),bg="paleturquoise")
lb2.place(x=700,y=630)
lb4=Label(win, text='Follow us:',font=("Book Antiqua",15,'bold'),bg="paleturquoise")
lb4.place(x=1200,y=620)

# logo declaration

#datascience
img11=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\python1.png"))
img12=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\ml.png"))
img13=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\dl2.png"))
img14=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\Ai_2.png"))

#web
img15=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\js.png"))
img16=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\angular_10.png"))
img17=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\node.png"))
img18=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\react.png"))

#cloud
img19=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\aws.png"))
img20=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\azsure.png"))
img21=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\devops.png"))

#programming
img22=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\c++.png"))
img23=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\java.png"))
img24=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\.net.png"))

#database
img25=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\oracle2.png"))
img26=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\mongo.png"))
img27=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\sql.png"))

#testing
img28=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\testing.png"))
img29=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\auto3.png"))

#mobile app
img30=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\android2.png"))
img31=ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\ios-png-4075.png"))



#function for dropdown

def createwindow(selected_option):
    
    if selected_option == 'Data Science':
        win31=Toplevel(win)
        win31.geometry('700x500')
        win31.config(bd=15,relief="ridge",bg="paleturquoise")

        o1 = Label(win31, text='Data Science',font=('times new roman',25,'bold'),bg='yellow')
        o1.pack()


        info = [
            f"Data science is considered \n"
            "to be among the hottest \n"
            "professions in the market \n"
            "nowadays.transform your \n"
            "data into meaningful statistics \n"
            "through our Data Science with \n"
            "Python Training in Chennai."
        ]
             
               
        
        F1=LabelFrame(win31,text='PYTHON',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F1.place(x=50,y=100,width=300,height=600)
        
        
        l1 = Label(F1,text=info,font=('times new rommon',15,),fg='blue',bg='white')
        l1.place(x=0,y=210)
        p1=Label(F1,image=img11,bg='white')
        p1.place(x=30,y=5)
        b1 = Label(F1, text='Duration : 3 Months ⌛',font=('Californian FB',18,'bold'))
        b1.place(x=10,y=440)
        b2 = Label(F1, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b2.place(x=10,y=490)


        info2 = [
            
            "With Softlogic, the leading \n"
            "institute for Machine Learning \n"
            "Training in Chennai, you can \n"
            "open doors to exciting career \n"
            "opportunities in areas such as \n"
            "Data Science, AI, DL, Python, \n"
            "and more."
        ]

        
        F2=LabelFrame(win31,text='MACHINE LEARNING',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F2.place(x=420,y=100,width=300,height=600)
        l2 = Label(F2,text=info2,font=('times new rommon',15,),fg='blue',bg='white')
        l2.place(x=5,y=210)
        p1=Label(F2,image=img12,bg='white')
        p1.place(x=30,y=15)
        b3 = Label(F2, text='Duration : 2 Months ⌛',font=('Californian FB',18,'bold'))
        b3.place(x=10,y=440)
        b4 = Label(F2, text='Fees : 30500/-💰',font=('Californian FB',18,'bold'))
        b4.place(x=10,y=490)


        info3 = [
            "Join our DL Training\n"
            "in Chennai for transformative\n"
            "learning experience in AI, \n"
            "ML, and Data Science.\n"
            "Softlogic’s expert-designed \n"
            "curriculum covers neural\n" 
            "networks natural language \n"
            "processing, and more."
        ]
        
        F3=LabelFrame(win31,text='DEEP LEARNING',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F3.place(x=790,y=100,width=300,height=600)
        l3 = Label(F3,text=info3,font=('times new rommon',15,),fg='blue',bg='white')
        l3.place(x=10,y=210)
        p1=Label(F3,image=img13,bg='white')
        p1.place(x=10,y=15)
        b5 = Label(F3, text='Duration : 1.5 Months ⌛',font=('Californian FB',18,'bold'))
        b5.place(x=10,y=440)
        b6 = Label(F3, text='Fees : 30500/-💰',font=('Californian FB',18,'bold'))
        b6.place(x=10,y=490)


        info4 = [
            "Discover the captivating \n"
            "realm of AI through \n"
            "Softlogic's Artificial \n"
            "Intelligence Training in \n"
            "Chennai. Our comprehensive\n"
            "Artificial Intelligence \n"
            "Course in Chennai explores\n"
            "fundamental concepts like\n"
            "ML,DL"
        ]
        
        F4=LabelFrame(win31,text='AI',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F4.place(x=1160,y=100,width=300,height=600)
        l4 = Label(F4,text=info4,font=('times new rommon',15,),fg='blue',bg='white')
        l4.place(x=10,y=210)
        p1=Label(F4,image=img14,bg='white')
        p1.place(x=10,y=15)
        b7 = Label(F4, text='Duration : 1.5 Months ⌛',font=('Californian FB',18,'bold'))
        b7.place(x=10,y=440)
        b8 = Label(F4, text='Fees : 33500/-💰',font=('Californian FB',18,'bold'))
        b8.place(x=10,y=490)

        
    elif selected_option == 'Web Desiging':
        win32=Toplevel(win)
        win32.geometry('700x500')
        win32.config(bd=15,relief="ridge",bg="paleturquoise")
        
        o2 = Label(win32, text='Web Desiging',font=('times new rommon',25,'bold'),bg='yellow')
        o2.pack()

        info = [
            "Mastery of JavaScript \n"
            "programming is vital due\n"
            "to its broad applications.\n"
            "Our JavaScript Course in \n"
            "Chennai offers comprehensive\n"
            "learning, covering core \n"
            "JavaScript, HTML, CSS, DOM\n"
            "manipulation, Node.js"
        ]
             
               
        
        F1=LabelFrame(win32,text='JAVASCRIPT',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F1.place(x=50,y=100,width=300,height=600)
        l1 = Label(F1,text=info,font=('times new rommon',15,),fg='blue',bg='white')
        l1.place(x=0,y=210)
        p1=Label(F1,image=img15,bg='white')
        p1.place(x=30,y=10)
        b1 = Label(F1, text='Duration : 3 Months ⌛',font=('Californian FB',18,'bold'))
        b1.place(x=10,y=440)
        b2 = Label(F1, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b2.place(x=10,y=490)


        info2 = [
            
            "Are you searching for the\n"
            "Best Angular JS Training \n"
            "Institute in Chennai.? \n"
            "Learn Angular JS from \n"
            "Softlogic that offers \n"
            "industry relevant practical\n"
            "training."
        ]

        
        F2=LabelFrame(win32,text='ANGULAR',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F2.place(x=420,y=100,width=300,height=600)
        l2 = Label(F2,text=info2,font=('times new rommon',15,),fg='blue',bg='white')
        l2.place(x=20,y=210)
        p1=Label(F2,image=img16,bg='white')
        p1.place(x=35,y=10)
        b3 = Label(F2, text='Duration : 1.5 Months ⌛',font=('Californian FB',18,'bold'))
        b3.place(x=10,y=440)
        b4 = Label(F2, text='Fees : 23500/-💰',font=('Californian FB',18,'bold'))
        b4.place(x=10,y=490)


        info3 = [
            "Node.js has emerged as \n"
            "the go-to tool for building\n"
            "modern web applications \n"
            "owing to its combination \n"
            "of swift performance, \n"
            "asynchronous programming,\n"
            "and a robust ecosystem. \n"
            "Softlogic’s Node.Js Course "
        ]
        
        F3=LabelFrame(win32,text='NODE JS',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F3.place(x=790,y=100,width=300,height=600)
        l3 = Label(F3,text=info3,font=('times new rommon',15,),fg='blue',bg='white')
        l3.place(x=10,y=210)
        p1=Label(F3,image=img17,bg='white')
        p1.place(x=15,y=25)
        b5 = Label(F3, text='Duration : 1 Months ⌛',font=('Californian FB',18,'bold'))
        b5.place(x=10,y=440)
        b6 = Label(F3, text='Fees : 23500/-💰',font=('Californian FB',18,'bold'))
        b6.place(x=10,y=490)


        info4 = [
            "React.js's feature-rich \n"
            "framework has entirely \n"
            "shifted the way programmer\n"
            "build interactive user \n"
            "interfaces for websites and\n"
            "applications. Softlogic’s \n"
            "React Js Training in Chennai\n"
            "will cover master React.js"
        ]
        
        F4=LabelFrame(win32,text='REACT JS',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F4.place(x=1160,y=100,width=300,height=600)
        l4 = Label(F4,text=info4,font=('times new rommon',15,),fg='blue',bg='white')
        l4.place(x=10,y=210)
        p1=Label(F4,image=img18,bg='white')
        p1.place(x=35,y=10)
        b7 = Label(F4, text='Duration : 1.5 Months ⌛',font=('Californian FB',18,'bold'))
        b7.place(x=10,y=440)
        b8 = Label(F4, text='Fees : 23500/-💰',font=('Californian FB',18,'bold'))
        b8.place(x=10,y=490)

    elif selected_option == 'Cloud Computing':
        win33=Toplevel(win)
        win33.geometry('700x500')
        win33.config(bd=15,relief="ridge",bg="paleturquoise")
        
        o3 = Label(win33, text='Cloud Computing',font=('times new roman',25,'bold'),bg='yellow')
        o3.pack()

        info = [
            "Become proficient in \n"
            "building strong cloud \n"
            "solutions with our top-rated\n"
            "AWS Course in Chennai. Learn\n"
            "about networking, scalability\n"
            "and serverless computing using\n"
            "Lambda, as well as advanced\n"
            "services like AI/ML, \n"
            "database management."
        ]
             
               
        
        F1=LabelFrame(win33,text='AWS',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F1.place(x=230,y=100,width=300,height=600)
        l1 = Label(F1,text=info,font=('times new rommon',15,),fg='blue',bg='white')
        l1.place(x=0,y=200)
        p1=Label(F1,image=img19,bg='white')
        p1.place(x=35,y=40)
        b1 = Label(F1, text='Duration : 3 Months ⌛',font=('Californian FB',18,'bold'))
        b1.place(x=10,y=440)
        b2 = Label(F1, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b2.place(x=10,y=490)


        info2 = [
            
            "Join our best Azure Training\n"
            "in Chennai to explore cloud \n"
            "computing and create scalable\n"
            "secure solutions for business \n"
            "success.Our exceptional Azure\n"
            "Course in Chennai equips you \n"
            "with essential skills in both\n"
            "Azure and AWS"
        ]

        
        F2=LabelFrame(win33,text='AZURE',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F2.place(x=600,y=100,width=300,height=600)
        l2 = Label(F2,text=info2,font=('times new rommon',15,),fg='blue',bg='white')
        l2.place(x=0,y=200)
        p1=Label(F2,image=img20,bg='white')
        p1.place(x=10,y=15)
        b3 = Label(F2, text='Duration : 2 Months ⌛',font=('Californian FB',18,'bold'))
        b3.place(x=10,y=440)
        b4 = Label(F2, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b4.place(x=10,y=490)


        info3 = [
            "Explore contemporary soft\n"
            "ware development practices\n"
            "through our DevOps Training\n"
            "in Chennai. Learn about\n"
            "automation, continuous \n"
            "integration, cloud platforms\n"
            "(AWS, Azure)Docker, \n"
            "Kubernetes and more."
        ]
        
        F3=LabelFrame(win33,text='DEVOPS',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F3.place(x=970,y=100,width=300,height=600)
        l3 = Label(F3,text=info3,font=('times new rommon',15,),fg='blue',bg='white')
        l3.place(x=10,y=200)
        p1=Label(F3,image=img21,bg='white')
        p1.place(x=10,y=25)
        b5 = Label(F3, text='Duration : 1.5 Months ⌛',font=('Californian FB',18,'bold'))
        b5.place(x=10,y=440)
        b6 = Label(F3, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b6.place(x=10,y=490)

        
    elif selected_option == 'Programming':
        win34=Toplevel(win)
        win34.geometry('700x500')
        win34.config(bd=15,relief="ridge",bg="paleturquoise")
        
        o4 = Label(win34, text='Programming',font=('times new roman',25,'bold'),bg='yellow')
        o4.pack()

        info = [
            "Data science is considered \n"
            "to be among the hottest \n"
            "professions in the market \n"
            "nowadays.transform your \n"
            "data into meaningful statistics \n"
            "through our Data Science with \n"
            "Python Training in Chennai."
        ]
             
               
        
        F1=LabelFrame(win34,text='PYTHON',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F1.place(x=50,y=100,width=300,height=600)
        l1 = Label(F1,text=info,font=('times new rommon',15,),fg='blue',bg='white')
        l1.place(x=0,y=210)
        p1=Label(F1,image=img11,bg='white')
        p1.place(x=30,y=5)
        b1 = Label(F1, text='Duration : 3 Months ⌛',font=('Californian FB',18,'bold'))
        b1.place(x=10,y=440)
        b2 = Label(F1, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b2.place(x=10,y=490)


        info2 = [
            
            "In a code-driven landscape,\n"
            "where innovation thrives on\n"
            "programming, the demand for\n"
            "proficient C and C++ \n"
            "is unparalleled. Harness \n"
            "Your Coding Potential with \n"
            "Softlogic's C and C++ \n"
            "Training in Chennai."
        ]

        
        F2=LabelFrame(win34,text='C,C++',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F2.place(x=420,y=100,width=300,height=600)
        l2 = Label(F2,text=info2,font=('times new rommon',15,),fg='blue',bg='white')
        l2.place(x=5,y=210)
        p1=Label(F2,image=img22,bg='white')
        p1.place(x=35,y=5)
        b3 = Label(F2, text='Duration : 2 Months ⌛',font=('Californian FB',18,'bold'))
        b3.place(x=10,y=440)
        b4 = Label(F2, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b4.place(x=10,y=490)


        info3 = [
            "With millions of Java \n"
            "apps in use today, Java\n"
            "programming has rapidly \n"
            "become a required talent\n"
            "for any job. Softlogic, \n"
            "one of the Best Java Training\n"
            "Institute in Chennai, is \n"
            "designed to meet all of\n"
            "the IT industry."
        ]
        
        F3=LabelFrame(win34,text='JAVA',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F3.place(x=790,y=100,width=300,height=600)
        l3 = Label(F3,text=info3,font=('times new rommon',15,),fg='blue',bg='white')
        l3.place(x=5,y=210)
        p1=Label(F3,image=img23,bg='white')
        p1.place(x=35,y=0)
        b5 = Label(F3, text='Duration : 3-6 Months ⌛',font=('Californian FB',18,'bold'))
        b5.place(x=10,y=440)
        b6 = Label(F3, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b6.place(x=10,y=490)


        info4 = [
            ".NET continues to be in\n"
            "strong demand and is being\n"
            "used extensively across \n"
            "numerous business sectors\n"
            "and application fields. \n"
            "Softlogic’s Dot Net Training\n"
            "in Chennai is designed to\n"
            "offer you the expertise to\n"
            "be a proficient ."
        ]
        
        F4=LabelFrame(win34,text='DOT NET',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F4.place(x=1160,y=100,width=300,height=600)
        l4 = Label(F4,text=info4,font=('times new rommon',15,),fg='blue',bg='white')
        l4.place(x=10,y=210)
        p1=Label(F4,image=img24,bg='white')
        p1.place(x=10,y=80)
        b7 = Label(F4, text='Duration : 3-6 Months ⌛',font=('Californian FB',18,'bold'))
        b7.place(x=10,y=440)
        b8 = Label(F4, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b8.place(x=10,y=490)

        
    elif selected_option == 'Database':
        win35=Toplevel(win)
        win35.geometry('700x500')
        win35.config(bd=15,relief="ridge",bg="paleturquoise")
        
        o5 = Label(win35, text='Database',font=('times new roman',25,'bold'),bg='yellow')
        o5.pack()

        info = [
            "Oracle SQL foundational\n"
            "tool for data management,\n"
            "analysis, application \n"
            "development, and decision\n"
            "-making in modern business\n"
            "environments. Oracle SQL\n"
            "Course by Softlogic is \n"
            "created to equip you \n"
            "with the imperative skills"
        ]
             
               
        
        F1=LabelFrame(win35,text='ORACLE SQL',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F1.place(x=230,y=100,width=300,height=600)
        l1 = Label(F1,text=info,font=('times new rommon',15,),fg='blue',bg='white')
        l1.place(x=10,y=200)
        p1=Label(F1,image=img25,bg='white')
        p1.place(x=15,y=30)
        b1 = Label(F1, text='Duration : 2 Months ⌛',font=('Californian FB',18,'bold'))
        b1.place(x=10,y=440)
        b2 = Label(F1, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b2.place(x=10,y=490)


        info2 = [
            
            "Considering the convenience\n"
            "it offers in storing, \n"
            "sustaining and extracting\n"
            "data while building \n"
            "applications in a wide\n"
            "range of programming\n"
            "languages, MongoDB is\n"
            "widely sought-after\n"
            "on a global scale."
        ]

        
        F2=LabelFrame(win35,text='MONGO DB',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F2.place(x=600,y=100,width=300,height=600)
        l2 = Label(F2,text=info2,font=('times new rommon',15,),fg='blue',bg='white')
        l2.place(x=10,y=200)
        p1=Label(F2,image=img26,bg='white')
        p1.place(x=30,y=0)
        b3 = Label(F2, text='Duration : 2 Months ⌛',font=('Californian FB',18,'bold'))
        b3.place(x=10,y=440)
        b4 = Label(F2, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b4.place(x=10,y=490)


        info3 = [
            "A proper database is\n"
            "essential for every \n"
            "business. The businesses\n"
            "evaluate data and get \n"
            "report from data. This\n"
            "implies huge demand for \n"
            "database.Microsoft SQL \n"
            "Server the best relational\n"
            "database server software."
        ]
        
        F3=LabelFrame(win35,text='SQL SERVER',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F3.place(x=970,y=100,width=300,height=600)
        l3 = Label(F3,text=info3,font=('times new rommon',15,),fg='blue',bg='white')
        l3.place(x=15,y=200)
        p1=Label(F3,image=img27,bg='white')
        p1.place(x=15,y=40)
        b5 = Label(F3, text='Duration : 1.5 Months ⌛',font=('Californian FB',18,'bold'))
        b5.place(x=10,y=440)
        b6 = Label(F3, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b6.place(x=10,y=490)

        
    elif selected_option == 'Software Testing':
        win36=Toplevel(win)
        win36.geometry('700x500')
        win36.config(bd=15,relief="ridge",bg="paleturquoise")
        
        o6 = Label(win36, text='Software Testing',font=('times new roman',25,'bold'),bg='yellow')
        o6.pack()

        info = [
            "Amidst the automation surge\n"
            "manual testing stands strong\n"
            "as a vital cornerstone in \n"
            "the world of software quality.\n"
            "Join Softlogic’s Manual \n"
            "Testing Course for a manual\n"
            "testing adventure and discover\n"
            "the hidden keys to flawless \n"
            "user experiences in software!"
        ]
             
               
        F1=LabelFrame(win36,text='MANUAL TESTING',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F1.place(x=350,y=100,width=300,height=600)
        l1 = Label(F1,text=info,font=('times new rommon',15,),fg='blue',bg='white')
        l1.place(x=0,y=210)
        p1=Label(F1,image=img28,bg='white')
        p1.place(x=20,y=20)
        b1 = Label(F1, text='Duration : 2 Months ⌛',font=('Californian FB',18,'bold'))
        b1.place(x=10,y=440)
        b2 = Label(F1, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b2.place(x=10,y=490)


        info2 = [
            
            "Enroll in our Selenium \n"
            "Training in Chennai to \n"
            "become a proficient web\n"
            "application tester. Master\n"
            "bug identification and \n"
            "resolution for reliable\n"
            "applications with our best\n"
            "Selenium Course in Chennai\n"
            "at Softlogic."
        ]

        
        F2=LabelFrame(win36,text='AUTOMATION TESTING',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F2.place(x=860,y=100,width=300,height=600)
        l2 = Label(F2,text=info2,font=('times new rommon',15,),fg='blue',bg='white')
        l2.place(x=15,y=210)
        p1=Label(F2,image=img29,bg='white')
        p1.place(x=10,y=15)
        b3 = Label(F2, text='Duration : 1 Months ⌛',font=('Californian FB',18,'bold'))
        b3.place(x=10,y=440)
        b4 = Label(F2, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b4.place(x=10,y=490)


        
        
    elif selected_option == 'Mobile App Development':
        win37=Toplevel(win)
        win37.geometry('700x300')
        win37.config(bd=15,relief="ridge",bg="paleturquoise")
        
        o7 = Label(win37, text='Mobile App Development',font=('times new roman',25,'bold'),bg='yellow')
        o7.pack()

        info = [
            "Empower yourself in the\n"
            "realm of Mobile App \n"
            "Development honing the \n"
            "skills to craftinventive\n"
            "and user-friendly mobile apps\n"
            "for diverse users through\n"
            "our Android Training\n"
            "in Chennai. Our Android \n"
            "Course in Chennai ."
        ]
             
               
        F1=LabelFrame(win37,text='ANDROID',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F1.place(x=350,y=100,width=300,height=600)
        l1 = Label(F1,text=info,font=('times new rommon',15,),fg='blue',bg='white')
        l1.place(x=5,y=210)
        p1=Label(F1,image=img30,bg='white')
        p1.place(x=30,y=0)
        b1 = Label(F1, text='Duration : 3 Months ⌛',font=('Californian FB',18,'bold'))
        b1.place(x=10,y=440)
        b2 = Label(F1, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b2.place(x=10,y=490)


        info2 = [
            
            "Apple's iOS remains one\n"
            "of the widely used mobile\n"
            "operating systems in the\n"
            "world and has a significant\n"
            "base of users. Softlogic’s iOS\n"
            "Training in Chennai will lead\n"
            "you through the core principles\n"
            "programs, and frameworks."
        ]

        
        F2=LabelFrame(win37,text=' IOS',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
        F2.place(x=860,y=100,width=300,height=600)
        l2 = Label(F2,text=info2,font=('times new rommon',15,),fg='blue',bg='white')
        l2.place(x=0,y=210)
        p1=Label(F2,image=img31,bg='white')
        p1.place(x=30,y=0)
        b3 = Label(F2, text='Duration : 2 Months ⌛',font=('Californian FB',18,'bold'))
        b3.place(x=10,y=440)
        b4 = Label(F2, text='Fees : 28500/-💰',font=('Californian FB',18,'bold'))
        b4.place(x=10,y=490)
        

def on_selected(value):
    selected_option_var.set(value)
    createwindow(selected_option_var.get())

#dropdown

selected_option_var=StringVar(win)
selected_option_var.set('COURSES OFFERED')

options=[
    'Data Science',
    'Web Desiging',
    'Cloud Computing',
    'Programming',
    'Database',
    'Software Testing',
    'Mobile App Development'
]

c = OptionMenu(win, selected_option_var, *options,command=on_selected)
c.place(x=420,y=170)

bold_font = font.Font(weight='bold')
c['font']=bold_font

#label

l1=Label(win, text='2024 Combo Offer !!! - 3 Trending courses @ 40000/-', font=("Cambria",25),bg='white')
l1.place(x=450,y=50)





# function

def clear_entries():
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    c1.delete(0, 'end')
    pass



#message for submit

def display_and_store():
    
    tkinter.messagebox.showinfo("Info","Your response has been recorded")
    pass

#database function

def putdataintomysql(*args):
    e_name = i_name.get()
    e_email = i_email.get()
    e_phone = i_phone.get()
    e_course = i_course.get()
    e_branch = i_branch.get()
    
    # database connection
    con = mc.connect(host="localhost",user="root", password="", database="dk")
    cur = con.cursor() 
    cur.execute("insert into enquiry(e_name, e_email, e_phone, e_course, e_branch) values('"+e_name+"', '"+e_email+"', '"+e_phone+"', '"+e_course+"', '"+e_branch+"')")
    con.close()
    pass


#combining functions

def combine_functions():
    display_and_store()
    putdataintomysql()

# value assignment
i_name = StringVar()
i_email = StringVar()
i_phone = StringVar()
i_course = StringVar()
i_branch = StringVar()

   
#Entry

F2=LabelFrame(win,text='ENQUIRY :',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='white')
F2.place(x=12,y=230,width=400,height=480)

l2=Label(F2,text='Your Name',font=('times new rommon',15,'bold'),bg='white')
l2.grid(row=0,column=0)
e2=Entry(F2,width=17,font='arial 15 bold',textvariable=i_name)
e2.grid(row=0,column=1,padx=30,pady=20)

l3=Label(F2,text='Email id',font=('times new rommon',15,'bold'),bg='white')
l3.grid(row=1,column=0)
e3=Entry(F2,width=17,font='arial 15 bold',textvariable=i_email)
e3.grid(row=1,column=1,padx=30,pady=20)

l4=Label(F2,text='Phone Number',font=('times new rommon',15,'bold'),bg='white')
l4.grid(row=2,column=0)
e4=Entry(F2,width=17,font='arial 15 bold',textvariable=i_phone)
e4.grid(row=2,column=1,padx=30,pady=20)

l5=Label(F2,text='Course Chosen',font=('times new rommon',15,'bold'),bg='white')
l5.grid(row=3,column=0)
e5=Entry(F2,width=17,font='arial 15 bold',textvariable=i_course)
e5.grid(row=3,column=1,padx=30,pady=20)


l6=Label(F2,text='Select Branch',font=('times new rommon',15,'bold'),bg='white')
l6.grid(row=4,column=0)
c1 = ttk.Combobox(F2,values=['KK Nagar','Navalur(OMR)'],width=25,height=8,textvariable=i_branch)
c1.grid(row=4,column=1,padx=30,pady=20)

b2=Button(F2,text='Submit',font='arial 11 bold',padx=3,pady=3,bg='skyblue',width=5, command=combine_functions)
b2.grid(row=10,column=0,padx=10,pady=30)

b2=Button(F2,text='Clear',font='arial 11 bold',padx=3,pady=3,bg='skyblue',width=5, command=clear_entries)
b2.grid(row=10,column=1,padx=10,pady=30)

#image decalaration for placements

img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\Deepak kumar\OneDrive\Desktop\Project\Hiring-Partners1.jpg"))


# function for button - win1 new window

def createnewwindow():
    win1 = Toplevel(win)
    win1.geometry('1500x800')
    win1.config(bd=20,relief="ridge",bg='paleturquoise')
    
    #bgimage
    #F3=Frame(win1)
    #F3.place(650,y=300)

    #def open_browser():
        #webbrowser.open("https://www.softlogicsys.in/reviews/")

        #linkl=Label(win1, text='Visit for Reviews', fg='blue', cursor='hand2')
        #linkl.place(x=100,y=100)
        #linkl.bind("<Button-1>", lambda e: open_browser())
        

        
    
    p4=Label(win1,image=img5)
    p4.place(x=650,y=300)

    l=Label(win1,text='PLACEMENTS',bg='white',font=('Times New Roman',35,'bold'),width=15,relief=RIDGE,bd=10)
    l.pack()
    p1=Label(win1,text='Unlimited Interviews Until You Get Placed !!👍',fg='blue',bg='white', font=('Times New Roman',25,'bold'))
    p1.place(x=80,y=100)
    
    p2=Label(win1, text='➥ Endless Interviews !!!',font=('HP Simplified',25),width=20).place(x=80,y=200)
    p21=Label(win1, text='Advance Your Career Forward',font=('Sitka Heading',15,'italic')).place(x=120,y=250)
    
    p3=Label(win1, text='➥ 100% Placement Assistance',font=('HP Simplified',25)).place(x=80,y=350)
    p31=Label(win1, text='Expert Guidance for Building a Prosperous Path',font=('Sitka Heading',15,'italic')).place(x=120,y=440)
    
    p4=Label(win1, text='➥ 90000+ Impactful Placements',font=('HP Simplified',25)).place(x=80,y=500)
    p41=Label(win1, text='85% Annual Placement Success',font=('Sitka Heading',15,'italic')).place(x=120,y=550)
    
    p5=Label(win1, text='➥ Lifetime Carrer support',font=('HP Simplified',25)).place(x=80,y=650)
    p51=Label(win1, text='Infinite Assistance for Endless Success',font=('Sitka Heading',15,'italic')).place(x=120,y=700)

    
    p6=Label(win1, text='OUR HIRING PATNERS',fg='red',bg='white', font=('Times New Roman',20,'italic','underline')).place(x=930,y=250)
    pass

def createnewwindow2():
    win2 = Toplevel(win)
    win2.geometry('1500x750') 
    win2.config(bd=20,relief="ridge",bg='paleturquoise')

    F3=LabelFrame(win2,text=' STAFF LOGIN ⚠️:',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,fg='black',bg='skyblue')
    F3.place(x=450,y=180,width=600,height=350)

    
    p2=Label(win2, image=img2,bg="paleturquoise")
    p2.place(x=0,y=10)

    #label in win2
    
    l1=Label(F3, text='USERNAME:', bg='red', fg='white', font="Calibri",  relief=SUNKEN, bd=8, width=12).place(x=90, y=70)
    l2=Label(F3, text='PASSWORD:', bg='red', fg='white', font="Calibri",  relief=SUNKEN, bd=8, width=12).place(x=90, y=140)
    
    # entry in win2
    
    username = Entry(F3, width=20, bg='white', fg='black', font="Calibri",relief=SUNKEN, bd=8)
    username.place(x=270, y=70)
    password = Entry(F3, width=20, bg='white', fg='black', font="Calibri", relief=SUNKEN, bd=8)
    password.place(x=270, y=140)
    password.config(show="*")

    #function for submit
    def open_window():    
        entered_username = username.get()
        entered_password = password.get()
        
        if entered_username == "sla" and entered_password == "123":
            win21 = Toplevel(win2)
            win21.title("SLA - Student info")
            win21.geometry('1500x1500')
            win21.config(bd=20,relief="ridge",bg="paleturquoise")

            p3=Label(win21, image=img2,bg="paleturquoise")
            p3.place(x=0,y=10)
            

            l1=Label(win21, text='STUDENT INFO', font=('times new rommon',18,'bold'), relief=SUNKEN, bd=5, bg='white',width=15)
            l1.pack()
        
            
            # function for clear

            def clear_entries2():
                e2.delete(0, 'end')
                e3.delete(0, 'end')
                c1.delete(0, 'end')
                c2.delete(0, 'end')
                c3.delete(0, 'end')
                
            def display_and_store2():
    
                tkinter.messagebox.showinfo("Info","Your response has been recorded")
            

            def putdataintomysql2(*args):
                s_name = i_name.get()
                s_course = i_course.get()
                s_trainer = i_trainer.get()
                s_time = i_time.get()
                s_compilation = i_compilation.get()

            #dbc connection
                con1 = mc.connect(host="localhost",user="root", password="", database="dk")
                cur = con1.cursor() 
                cur.execute("insert into student_info(s_name, s_course, s_trainer, s_time, s_compilation) values('"+s_name+"', '"+s_course+"', '"+s_trainer+"', '"+s_time+"', '"+s_compilation+"')")
                con1.close()

            def combine_functions2():
                display_and_store2()
                putdataintomysql2()

            # value assignment
            i_name = StringVar()
            i_course = StringVar()
            i_trainer = StringVar()
            i_time = StringVar()
            i_compilation = StringVar()
                
                
           
            
            # student info

            
            l2=Label(win21,text='Student Name',font=('times new rommon',20,'bold'),bg='white')
            l2.place(x=400,y=100)
            e2=Entry(win21,width=17,font='arial 15 bold',textvariable=i_name)
            e2.place(x=800,y=100)
            
            
            l3=Label(win21,text='Course',font=('times new rommon',20,'bold'),bg='white')
            l3.place(x=400,y=200)
            e3=Entry(win21,width=17,font='arial 15 bold',textvariable=i_course)
            e3.place(x=800,y=200)
            
            l4=Label(win21,text='Trainer',font=('times new rommon',20,'bold'),bg='white')
            l4.place(x=400,y=300)
            c1 = ttk.Combobox(win21,values=['RK','Muthu(MMK)','Esakki','Manju','Jayshree'],width=25,height=8, textvariable=i_trainer)
            c1.place(x=800,y=300)

            bold_font = font.Font(weight='bold')
            c1['font']=bold_font

            

            l5=Label(win21,text='Batch Timings',font=('times new rommon',20,'bold',),bg='white')
            l5.place(x=400,y=400)
            c2 = ttk.Combobox(win21,values=['10am - 11am','11am - 12pm','5pm - 6pm','6pm - 7pm'],width=25,height=8, textvariable=i_time)
            c2.place(x=800,y=400)

            bold_font = font.Font(weight='bold')
            c2['font']=bold_font



            l6=Label(win21,text='Course Completion',font=('times new rommon',20,'bold'),bg='white')
            l6.place(x=400,y=500)
            c3 = ttk.Combobox(win21,values=['Completed','Unfinished'],width=25,height=8, textvariable=i_compilation)
            c3.place(x=800,y=500)

            bold_font = font.Font(weight='bold')
            c3['font']=bold_font


            #buttons
            b=Button(win21, text='Move to Database', bg='red', fg='white', font="Calibri",  relief=SUNKEN, bd=5, width=15,command=combine_functions2)
            b.place(x=400,y=600)

            b2=Button(win21, text='Clear', bg='red', fg='white', font="Calibri",  relief=SUNKEN, bd=5, width=10,command=clear_entries2)
            b2.place(x=800,y=600)

        else:
            tkinter.messagebox.showerror("Invalid","Incorrect Password")
    # Button

    submit=Button(F3, text='SUBMIT', bg='red', fg='white', font="Calibri",  relief=SUNKEN, bd=5, width=10,command=open_window)
    submit.place(x=230,y=220)
        
        

    
#Button

b1=Button(win, text='Placements', font="cambria",bg='skyblue',command=createnewwindow,width=15,height=1)
b1.place(x=695,y=170)

b2=Button(win, text='Staff Login', font="cambria",bg='skyblue',width=15,height=1,command=createnewwindow2)
b2.place(x=900,y=170)





win.mainloop()
