from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
# from playsound import playsound
from threading import Thread
from tkVideoPlayer import TkinterVideo


try:
    con = mysql.connector.connect(host="localhost",user="root",password="",database="project")

    cur = con.cursor()
except:
    print("Somthing is wrong...")

w=Tk()
# w.geometry('900x500')
# w.attributes('-fullscreen', True)
w.configure(bg='#262626')
w.resizable(0,0)
wi = 1280
h = 720
w.geometry("%dx%d+0+0" % (wi, h))
print(wi , h)
w.title('Toggle Menu')

teams = {12: 'Sunrisers Hyderabad', 
4: 'Kolkata Knight Riders', 3: 'Gujarat Lions', 
8: 'Pune Warriors', 
1: 'Delhi Daredevils', 
7: 'Mumbai Indians', 5: 'Kochi Tuskers Kerala', 
0: 'Chennai Super Kings', 10: 'Rising Pune Supergiant', 
1: 'Delhi Capitals', 9: 'Royal Challengers Bangalore', 
10: 'Rising Pune Supergiants', 6: 'Kings XI Punjab', 
11: 'Rajasthan Royals', 2: 'Deccan Chargers'}

city_dct = {1 : "Hyderabad",2 : "Pune",3 : "Rajkot",4 : "Indore",5 : "Bangalore",6 : "Mumbai",7 : "Kolkata",
8 : "Delhi",9 : "Chandigarh",10 : "Kanpur",11 : "Jaipur",12 : "Chennai",13 : "Cape Town",14 : "Port Elizabeth",
15 : "Durban",16 : "Centurion",17 : "East London",18 : "Johannesburg",19 : "Kimberley",20 : "Bloemfontein",
21 : "Ahmedabad",22 : "Cuttack",23 : "Nagpur",24 : "Dharamsala",25 : "Kochi",26 : "Visakhapatnam",27 : "Raipur",
28 : "Ranchi",29 : "Abu Dhabi",30 : "Sharjah",31 : "nan",32 : "Mohali",33 : "Bengaluru",34 : "Dubai"}

img_dct = {12: 'Sunrisers Hyderabad.png', 
4: 'Kolkata Knight Riders.png', 
1: 'Delhi Capitals.png', 
7: 'Mumbai Indians.png', 
0: 'Chennai Super Kings.png', 
9: 'Royal Challengers Bangalore.png', 
6: 'Kings XI Punjab.png', 
11: 'Rajasthan Royals.png'}

def default_home():
    f2=Frame(w, width=wi, height=h, bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(w, text="Home", fg='white', bg='#262626')
    l2.config(font=('Comic sans MS',90))
    l2.place(x=290, y=105)

def abus():
    f1.destroy()
    f2=Frame(w, width=wi/2, height=h, bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2, text="About Software", fg='white', bg='#262626')
    l2.config(font=('Comic sans MS',40))
    l2.place(x=90, y=20)

    l2_1=Label(f2, text="-> IPL predictor is a predictor application devloped for", fg='white', bg='#262626')
    l2_1.config(font=('Comic sans MS',18))
    l2_1.place(x=10, y=140)

    l2_2=Label(f2, text="   predicting data for IPL matches and much more..", fg='white', bg='#262626')
    l2_2.config(font=('Comic sans MS',18))
    l2_2.place(x=10, y=180)

    l2_3=Label(f2, text="-> IT is illigal to use our software for betting.", fg='white', bg='#262626')
    l2_3.config(font=('Comic sans MS',18))
    l2_3.place(x=10, y=235)

    l2_4=Label(f2, text="   we do not support betting :)", fg='white', bg='#262626')
    l2_4.config(font=('Comic sans MS',18))
    l2_4.place(x=10, y=275)

    l2_5=Label(f2, text="-> This is totally free software.", fg='white', bg='#262626')
    l2_5.config(font=('Comic sans MS',18))
    l2_5.place(x=10, y=330)

    l2_6=Label(f2, text="-> If you see someone selling, its scam!", fg='white', bg='#262626')
    l2_6.config(font=('Comic sans MS',18))
    l2_6.place(x=10, y=385)
    
    l2_7=Label(f2, text="-> If you enjoy our software please consider Some ", fg='white', bg='#262626')
    l2_7.config(font=('Comic sans MS',18))
    l2_7.place(x=10, y=440)

    l2_8=Label(f2, text="   donation. It will really help to improve our services..", fg='white', bg='#262626')
    l2_8.config(font=('Comic sans MS',18))
    l2_8.place(x=10, y=480)

    l2_9=Label(f2, text="-> Fixed and Updated BY XYZ team...", fg='white', bg='#262626')
    l2_9.config(font=('Comic sans MS',18))
    l2_9.place(x=10, y=535)

    f3=Frame(w, width=wi/2, height=h, bg='#12c4c0')
    f3.place(x=wi/2,y=45)
    l3=Label(f3, text="About us", fg='#262626', bg='#12c4c0')
    l3.config(font=('Comic sans MS',40))
    l3.place(x=190, y=20)

    l3_1=Label(f3, text="-> special thanks to our devloper:", fg='black', bg='#12c4c0')
    l3_1.config(font=('Comic sans MS',18))
    l3_1.place(x=10, y=140)

    l3_2=Label(f3, text="   Gaurav(Data analiyst and frontend)|Linkdin|Github", fg='black', bg='#12c4c0')
    l3_2.config(font=('Comic sans MS',18))
    l3_2.place(x=10, y=210)

    l3_3=Label(f3, text="   Nitish(Data analiyst and backend)|Linkdin|Github", fg='black', bg='#12c4c0')
    l3_3.config(font=('Comic sans MS',18))
    l3_3.place(x=10, y=250)

    l3_4=Label(f3, text="   Saqlen(Backend and frontend)|Linkdin|Github", fg='black', bg='#12c4c0')
    l3_4.config(font=('Comic sans MS',18))
    l3_4.place(x=10, y=290)

    l3_5=Label(f3, text="   Sujal(Research and frontend)|Linkdin|Github", fg='black', bg='#12c4c0')
    l3_5.config(font=('Comic sans MS',18))
    l3_5.place(x=10, y=330)

    l3_6=Label(f3, text="-> special thanks to our tester:", fg='black', bg='#12c4c0')
    l3_6.config(font=('Comic sans MS',18))
    l3_6.place(x=10, y=400)
    
    l3_7=Label(f3, text="   Vishuvendu(College HOD) ", fg='black', bg='#12c4c0')
    l3_7.config(font=('Comic sans MS',18))
    l3_7.place(x=10, y=470)

    l3_8=Label(f3, text="   vikram swami(cricket analiyst)", fg='black', bg='#12c4c0')
    l3_8.config(font=('Comic sans MS',18))
    l3_8.place(x=10, y=510)

    # toggle_win()

def pros():
    f1.destroy()
    f2=Frame(w, width=wi, height=h, bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(w, text="Acer", fg='white', bg='#262626')
    l2.config(font=('Comic sans MS',90))
    l2.place(x=290, y=105)
    # toggle_win()

def answin(fwin):
        global teams,img1,img_dct
        f1.destroy()
        ansfrm=Frame(w, width=wi, height=h, bg='#262626')
        ansfrm.place(x=0,y=45)

        print(teams[fwin])

        img1 = ImageTk.PhotoImage(Image.open("imges/"+img_dct[fwin]))

        Button(ansfrm,image=img1,
            command=toggle_win,
            border=0,
            bg='#262626',
            activebackground='#262626').place(x=450,y=110)
        
        l2=Label(ansfrm, text=teams[fwin]+" will be win the match...", fg='white', bg='#262626')
        l2.config(font=('Comic sans MS',40))
        l2.place(x=120, y=500)
       
        # toggle_win()    

def prediction():
    global f3,teams,city_dct,log_val
    if(log_val == 1):
        f1.destroy()
        f3=Frame(w,width=wi, height=h, bg='#262626')
        f3.pack()
        f3.place(x=0,y=45)
        f3.place(anchor='center', relx=0.5, rely=0.5)
        l2=Label(f3,text="WINNER PREDICTION",foreground='#99ff66',background="#262626")
        Frame(f3,width=585,height=2,bg='#99ff66').place(x=395,y=110)  
        l2.config(font=('Comic sans MS',40))    
        l2.place(x=380, y=30)   #x=380 y=30'''

        # import finalprojectv3
        # from predictor import 
        
        # print(team1_num)

        t1sel = ""
        def sel_team1(event):
            global t1sel,teams,tmimg1
            for i,j in zip(teams,teams.keys()):
                if teams[i] == chooseanteam1.get():
                    t1sel = i
                    print("team1",t1sel)
                    tmimg1 = ImageTk.PhotoImage(Image.open("imges/"+img_dct[j]))

                    Button(f3,image=tmimg1,
                        border=0,
                        bg='#262626',
                        activebackground='#262626').place(x=50,y=150)


        tm1_lbl = Label(f3,text = "TEAM-1",width=6,height=1)
        Frame(f3,width=60,height=2,bg='#99ff66').place(x=500,y=170)   # x=500
        tm1_lbl.grid(row=5, column=30, padx=(0,10) , pady=(35,0))
        tm1_lbl.config(bg='#262626', fg='#99ff66' ,font=35)
        val1 = StringVar()
        tm1_lbl.place(x=500,y=150)
        chooseanteam1 = ttk.Combobox(f3,width=20 , textvariable=val1)
        chooseanteam1.grid(row=5, column=31, padx=(0,0) , pady=(35,10))
        chooseanteam1['values'] = ('Chennai Super Kings' ,'Delhi Capitals' ,  'Kolkata Knight Riders' 
        , 'Kings XI Punjab' ,     'Mumbai Indians' , 'Royal Challengers Bangalore' 
        ,'Rajasthan Royals','Sunrisers Hyderabad')
        chooseanteam1.place(x=630,y=150)
        # chooseanteam1.current()
        chooseanteam1.bind("<<ComboboxSelected>>",sel_team1)
        # print(chooseanteam1.get())
        t2sel=""
        def sel_team2(event):
            global t2sel,teams,tmimg2
            for i,j in zip(teams,teams.keys()):
                if teams[i] == chooseanteam2.get():
                    t2sel = i
                    print("team2",t2sel)
                    tmimg2 = ImageTk.PhotoImage(Image.open("imges/"+img_dct[j]))

                    Button(f3,image=tmimg2,
                        border=0,
                        bg='#262626',
                        activebackground='#262626').place(x=830,y=150)
            

        tm2_lbl = Label(f3,text = "TEAM-2" , width=6 , height=1)
        Frame(f3,width=60,height=2,bg='#99ff66').place(x=500,y=220)
        tm2_lbl.config(bg="#262626" , fg="#99ff66" ,font=35)
        val2 = StringVar()
        tm2_lbl.place(x=500,y=200)
        chooseanteam2 = ttk.Combobox(f3,width=20 , textvariable=val2)
        chooseanteam2.grid(row=6, column=31 , padx=(10,35) , pady=(35,10) )
        chooseanteam2['values'] = ('Chennai Super Kings' ,'Delhi Capitals' ,  'Kolkata Knight Riders' 
        , 'Kings XI Punjab' ,     'Mumbai Indians' , 'Royal Challengers Bangalore' 
        ,'Rajasthan Royals','Sunrisers Hyderabad')
        chooseanteam2.place(x=630,y=200)
        chooseanteam2.current()
        chooseanteam2.bind("<<ComboboxSelected>>", sel_team2)
        
        selct = ""
        def sel_city(event):
            global selct,city_dct
            for i in city_dct:
                if city_dct[i] == cities.get():
                    selct = i
            
            print("city",selct)
            
            
        city_lb =Label(f3,text = "CITY" , width=3, height=1)
        Frame(f3,width=35,height=2,bg='#99ff66').place(x=490,y=270)
        city_lb.grid(row=7, column=30, padx=(10,0) , pady=(35,0))
        city_lb.config(bg="#262626" , fg="#99ff66" ,font=35 )
        val3 = StringVar()
        city_lb.place(x=500,y=250)
        cities = ttk.Combobox(f3,width=20 , textvariable=val3)
        cities.grid(row=7 , column=31, padx=(20,20) , pady=(35,10))
        cities['values'] = ('Hyderabad' , 'Pune' , 'Rajkot' , 'Indore' , 'Bangalore' , 'Mumbai' , 'Kolkata' , 'Delhi' , 'Chandigarh'  ,'Kanpur','Jaipur','Chennai','Cape Town','Port Elizabeth','Durban','Centurion','East London','Johannesburg','Kimberley','Bloemfontein','Ahmedabad','Cuttack','Nagpur','Dharamsala','Kochi','Visakhapatnam','Raipur','Ranchi','Abu Dhabi','Sharjah','nan','Mohali','Bengaluru','Dubai')
        cities.place(x=630,y=250)
        cities.current()
        cities.bind("<<ComboboxSelected>>",sel_city)
        
        seltswin = ""
        def sel_tswin(event):
            global seltswin,teams
            for i in teams:
                if teams[i] == toss_win.get():
                    seltswin = i
            print("toss winner",seltswin)
                

        tswin_lb =Label(f3,text = "TOSS WIN" , width=8 , height=1)
        Frame(f3,width=78,height=2,bg='#99ff66').place(x=500,y=320)
        tswin_lb.grid(row=8, column=30, padx=(10,0) , pady=(35,0))
        tswin_lb.config(bg="#262626" , fg="#99ff66" ,font=35)
        val4 = StringVar()
        tswin_lb.place(x=500,y=300)
        toss_win = ttk.Combobox(f3,width=20 , textvariable=val4)
        toss_win.grid(row=8 , column=31 , padx=(10,35) , pady=(35,10) )
        toss_win['values'] = ('Chennai Super Kings' ,'Delhi Capitals' ,  'Kolkata Knight Riders' 
        , 'Kings XI Punjab' ,     'Mumbai Indians' , 'Royal Challengers Bangalore' 
        ,'Rajasthan Royals','Sunrisers Hyderabad')
        toss_win.place(x=630,y=300)
        toss_win.current()
        toss_win.bind("<<ComboboxSelected>>",sel_tswin)

        tsdici = ""
        def sel_tsdici(event):
            global tsdici
            if ts_dici.get() == "bat":
                tsdici = ts_dici.get()
                tsdici = 1
            elif ts_dici.get() == "field":
                tsdici = ts_dici.get()
                tsdici = 2
            print("toss diceson",tsdici)

        tsdici_lb =Label(f3,text = "TOSS DECISION" , width=13 , height=1)
        Frame(f3,width=124,height=2,bg='#99ff66').place(x=500,y=370)
        tsdici_lb.grid(row=7, column=30, padx=(10,0) , pady=(35,0))
        tsdici_lb.config(bg="#262626" , fg="#99ff66" ,font=35 )
        val5 = StringVar()
        tsdici_lb.place(x=500,y=350)
        ts_dici = ttk.Combobox(f3,width=20 , textvariable=val5)
        ts_dici.grid(row=7 , column=31, padx=(20,20) , pady=(35,10))
        ts_dici['values'] = ('bat' , 'field')
        ts_dici.place(x=630,y=350)
        ts_dici.current()
        ts_dici.bind("<<ComboboxSelected>>",sel_tsdici)

    

        def senddata():
            global t1sel,t2sel,tsdici,selct,seltswin
            # str = "ihii"
            from predictor import recdata
            
            from predictor import recdata
            fwin = recdata(t1sel,t2sel,tsdici,selct,seltswin)
            
            fans  = fwin[0]
            print(fans)

            answin(fans)
            # videowin(fans)

        b2 =Button(f3,text="PREDICT" , width="14" , height="1", bg="#262626", font= "Time 10 bold" , command=senddata)
        b2.grid(row=9 , column=32 ,padx=(10,35) , pady=(35,10))
        b2.config(bg="#262626" , fg="#99ff66")    
        b2.place(x=590,y=470)
    
    else:
        messagebox.showinfo("showinfo", "Please Login First...")


log_val = 0
def loginact():
    global con,cur,log_val
    uname = l_e1.get()
    pwd = l_e2.get()

    try:
        # qry = "select uname,pwd from user where uname=%s and pwd=%s"

        # cur.execute(qry,(uname,pwd))

        # rst = cur.fetchone()

        if(uname=="admin" and pwd=="admin"):
            print("succesfull")
            messagebox.showinfo("showinfo", "Login successfully")
            log_val = 1
            toggle_win()

        else:
            print("email or password wrong")
            messagebox.askretrycancel("Error","Wrong email or password..")
    except:
        messagebox.showinfo("showinfo", "Invalid Credentials...")


def login():
    f1.destroy()
    global l_e1,l_e2,signin_img
    signin_win=Frame(w,width=wi,height=h,bg='#262626')
    signin_win.place(x=0,y=45)
    f2=Frame(signin_win, width=700, height=400, bg='#262626')
    f2.place(x=480,y=150)

    signin_img = ImageTk.PhotoImage(Image.open("login_img.jpeg"))
    Label(signin_win,image=signin_img,border=0,bg='#262626').place(x=50,y=130)

    l2=Label(signin_win,text="Sign in",fg='white',bg='#262626')
    l2.config(font=('Microsoft YaHei UI Light',35, 'bold'))
    l2.place(x=890,y=120)

    def on_enter(e):
        l_e1.delete(0,'end')    
    def on_leave(e):
        if l_e1.get()=='':   
            l_e1.insert(0,'Username')

    l_e1=Entry(f2,width=50,fg='white',border=0,bg='#262626')
    l_e1.config(font=('Microsoft YaHei UI Light',18, ))
    l_e1.bind("<FocusIn>", on_enter)
    l_e1.bind("<FocusOut>", on_leave)
    l_e1.insert(0,'Username')
    l_e1.place(x=340,y=80)

    Frame(f2,width=295,height=2,bg='white').place(x=340,y=130)

    def on_enter(e):
        l_e2.delete(0,'end')    
    def on_leave(e):
        if l_e2.get()=='':   
            l_e2.insert(0,'Password')

    l_e2=Entry(f2,width=50,show="*" ,fg='white',border=0,bg='#262626')
    l_e2.config(font=('Microsoft YaHei UI Light',18, ))
    l_e2.bind("<FocusIn>", on_enter)
    l_e2.bind("<FocusOut>", on_leave)
    l_e2.insert(0,'Password')
    l_e2.place(x=340,y=170)

    Frame(f2,width=295,height=2,bg='white').place(x=340,y=220)

    Button(f2,width=39,pady=7,text='Sign in',bg='#12c4c0',fg='black',border=0,command=loginact).place(x=350,y=280)
    l1=Label(f2,text="Don't have an account?",fg="white",bg='#262626')
    l1.config(font=('Microsoft YaHei UI Light',12, ))
    l1.place(x=350,y=330)

    b2=Button(f2,width=6,text='Sign up',border=0,bg='#262626', font=10,fg='white',command=signup)
    b2.place(x=530,y=325)
    # toggle_win()

def signupact():
    
    global con,cur
    uname = e1.get()
    eml = e0.get()
    pwd = e2.get()
    cpwd = e3.get()

    try:
        qry = "insert into user values('"+uname+"','"+eml+"','"+pwd+"','"+cpwd+"')"

        cur.execute(qry)

        con.commit()
        messagebox.showinfo("showinfo", "Account created successfully")
        
    except:
        print("Somthing is wrong...")

def signup():
    f1.destroy()
    global e1,e0,e2,e3,signup_img
    signup_win=Frame(w,width=wi,height=h,bg='#262626')
    signup_win.place(x=0,y=45)
    f2=Frame(signup_win, width=1100, height=400, bg='#262626')
    f2.place(x=480,y=150)

    signup_img = ImageTk.PhotoImage(Image.open("login_img.jpeg"))
    Label(signup_win,image=signup_img,border=0,bg='#262626').place(x=50,y=130)

    l2=Label(signup_win,text="Sign Up",fg='white',bg='#262626')
    l2.config(font=('Microsoft YaHei UI Light',35, 'bold'))
    l2.place(x=890,y=70)

    Frame(f2,width=175,height=2,bg='white').place(x=410,y=0)


    def on_enter(e):
        e1.delete(0,'end')    
    def on_leave(e):
        if e1.get()=='':   
            e1.insert(0,'Username')

    e1=Entry(f2,width=50,fg='white',border=0,bg='#262626')
    e1.config(font=('Microsoft YaHei UI Light',15, ))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0,'Username')
    e1.place(x=300,y=70)

    Frame(f2,width=170,height=2,bg='white').place(x=300,y=110)

    def on_enter(e):
        e0.delete(0,'end')    
    def on_leave(e):
        if e0.get()=='':   
            e0.insert(0,'Email')

    e0=Entry(f2,width=50,fg='white',border=0,bg='#262626')
    e0.config(font=('Microsoft YaHei UI Light',15, ))
    e0.bind("<FocusIn>", on_enter)
    e0.bind("<FocusOut>", on_leave)
    e0.insert(0,'Email')
    e0.place(x=550,y=70)

    Frame(f2,width=170,height=2,bg='white').place(x=550,y=110)

    def on_enter(e):
        e2.delete(0,'end')    
    def on_leave(e):
        if e2.get()=='':   
            e2.insert(0,'Password')

    e2=Entry(f2,width=50,show='*' ,fg='white',border=0,bg='#262626')
    e2.config(font=('Microsoft YaHei UI Light',15, ))
    e2.bind("<FocusIn>", on_enter)
    e2.bind("<FocusOut>", on_leave)
    e2.insert(0,'Password')
    e2.place(x=300,y=180)

    Frame(f2,width=170,height=2,bg='white').place(x=300,y=220)

    def on_enter(e):
        e3.delete(0,'end')    
    def on_leave(e):
        if e3.get()=='':   
            e3.insert(0,'confirm password')

    e3=Entry(f2,width=50,show='*' ,fg='white',border=0,bg='#262626')
    e3.config(font=('Microsoft YaHei UI Light',15, ))
    e3.bind("<FocusIn>", on_enter)
    e3.bind("<FocusOut>", on_leave)
    e3.insert(0,'confirm password')
    e3.place(x=550,y=180)

    Frame(f2,width=170,height=2,bg='white').place(x=550,y=220)

    Button(f2,width=39,pady=7,text='Sign up',bg='#12c4c0',fg='black',border=0,command=signupact).place(x=380,y=280)
    l1=Label(f2,text="Already have an account?",fg="white",bg='#262626')
    l1.config(font=('Microsoft YaHei UI Light',12, ))
    l1.place(x=380,y=330)

    b2=Button(f2,width=6,text='Sign In',border=0,bg='#262626', font=10,fg='white',command=login)
    b2.place(x=580,y=325)
    # toggle_win()

def dele():
        f1.destroy()

def toggle_win():
    global f1
    f1=Frame(w,width=300,height=350,bg='#12c4c0')
    f1.place(x=0,y=0)

    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=40,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'A B O U T   U S','#0f9d9a','#12c4c0',abus)
    bttn(0,127,'P R O B L E M S','#0f9d9a','#12c4c0',pros)
    bttn(0,174,'P R E D I C T I O N','#0f9d9a','#12c4c0',prediction)
    bttn(0,221,'L O G I N','#0f9d9a','#12c4c0',login)
    bttn(0,268,'S I G N   U P','#0f9d9a','#12c4c0',signup)


    

    global img2
    img2 = ImageTk.PhotoImage(Image.open("close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)
    
# default_home()

img1 = ImageTk.PhotoImage(Image.open("open.png"))

Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626').place(x=5,y=10)

trp_img = ImageTk.PhotoImage(Image.open("thumbnail/trophy.png"))

Button(w,image=trp_img,
       border=0,
       bg='#262626',
       activebackground='#262626').place(x=300,y=110)


thum_img1 = ImageTk.PhotoImage(Image.open("thumbnail/csk.png"))

Button(w,image=thum_img1,
    border=0,
    bg='#262626',
    activebackground='#262626').place(x=150,y=40)

thum_img2 = ImageTk.PhotoImage(Image.open("thumbnail/dc.png"))

Button(w,image=thum_img2,
    border=0,
    bg='#262626',
    activebackground='#262626').place(x=150,y=190)

thum_img3 = ImageTk.PhotoImage(Image.open("thumbnail/mi.png"))

Button(w,image=thum_img3,
    border=0,
    bg='#262626',
    activebackground='#262626').place(x=150,y=350)

thum_img4 = ImageTk.PhotoImage(Image.open("thumbnail/kkr.png"))

Button(w,image=thum_img4,
    border=0,
    bg='#262626',
    activebackground='#262626').place(x=150,y=510)

thum_img5 = ImageTk.PhotoImage(Image.open("thumbnail/rr.png"))

Button(w,image=thum_img5,
    border=0,
    bg='#262626',
    activebackground='#262626').place(x=1000,y=40)

thum_img6 = ImageTk.PhotoImage(Image.open("thumbnail/srh.png"))

Button(w,image=thum_img6,
    border=0,
    bg='#262626',
    activebackground='#262626').place(x=1000,y=190)

thum_img7 = ImageTk.PhotoImage(Image.open("thumbnail/kxip.png"))

Button(w,image=thum_img7,
    border=0,
    bg='#262626',
    activebackground='#262626').place(x=1000,y=350)

thum_img8 = ImageTk.PhotoImage(Image.open("thumbnail/rcb.png"))

Button(w,image=thum_img8,
    border=0,
    bg='#262626',
    activebackground='#262626').place(x=1000,y=510)
# a=playsound('iplsound.mp3')
w.mainloop()