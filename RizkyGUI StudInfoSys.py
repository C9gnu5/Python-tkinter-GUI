from student import StudentInfo
from search_student import SearchStudent
from print_all_student import PrintAllStudent
from add_student import AddStudent
from login import Login
from mainmenu import MainMenu
from tkinter import *


stu = StudentInfo()
searcher, addstu, printAll = SearchStudent(stu), AddStudent(stu), PrintAllStudent(stu)
login = Login(searcher)
me = MainMenu(searcher, addstu, printAll, login)

root = Tk()

def forgetFrames():
    instruction_frame.pack_forget()
    myinfo_frame.pack_forget()
    search_frame.pack_forget()
    add_stu_frame.pack_forget()
    view_all_frame.pack_forget()

def login():
    global attempt
    user = searcher.verify_login(login_usr.get()) # nasa searcher_student.py yung verify_login na function
    if user: # kapag nag return yung function ng student object
        enclosure_frame.place_forget()
        menu_lbl_usr.config(text=f"ID: {user.getIdNum()}")
        menu_frame.pack(side='left',fill='y')
        inst_lbl.config(text=f"Welcome {user.getName()}!\nYou can choose options on the sidebar menu to:\n\n   - View your information\n   - Search other student\n   - Register a new student\n   - View the student list\n   - Log out\n   - Exit")
        instruction_frame.pack(side='left',fill='y')
        attempt = 0
    elif not login_usr.get() or login_usr.get().isspace(): # kapag blanko o white space ang sinearch ng user
        attempt += 1
        login_lbl_err.config(text=f"Please Enter a Student ID-Number!\nRemaining attempts: {3-attempt}")
    else: # kapag False ang ni-return nung function
        attempt += 1
        login_lbl_err.config(text=f"Student ID-Number Not Found!\nRemaining attempts: {3-attempt}")
    if attempt == 3: exit()

def myinfoFrame():
    user = searcher.search_student(login_usr.get())
    forgetFrames(),txt_s_clear(),clear_reg()
    lbl_conf_add.config(text="Please fill out ALL the textboxes to register a student",fg='black'),my_lbl.config(text=user),s_lbl.config(text=" ",bg='light grey')
    myinfo_frame.pack(side='left',fill='y')

def searchFrame():
    forgetFrames(),clear_reg()
    lbl_conf_add.config(text="Please fill out ALL the textboxes to register a student",fg='black')
    search_frame.pack(side='left',fill='y')
def searchStudent():
    stud = searcher.search_student(txt_s.get())
    if stud: s_lbl.config(text=stud,bg='white')
    elif not txt_s.get() or txt_s.get().isspace(): s_lbl.config(text="Please Enter a Student ID-Number!",bg='white')
    else: s_lbl.config(text=f"Student ID-Number '{txt_s.get()}' Not Found!",bg='white')
    txt_s_clear()
def txt_s_clear():
    txt_s.delete(0,'end')

def addStuFrame():
    forgetFrames()
    txt_s_clear()
    s_lbl.config(text="",bg='light grey')
    add_stu_frame.pack(side='left',fill='y')
def reg_stud():
    name,age,idnum,email,phone = txt_n.get(),txt_a.get(),txt_i.get(),txt_e.get(),txt_p.get()
    if name and age and idnum and email and phone:
        addstu.add_student(name,age,idnum,email,phone)
        clear_reg()
        clear_err()
        lbl_conf_add.pack(anchor='center',pady=70)
        lbl_conf_add.config(text=f"Added student {name} to the list.",fg='green')
    else:
        lbl_conf_add.pack_forget()
        if not name or name.isspace(): en.pack(pady=0)
        else: en.pack_forget()
        if not age or age.isspace(): ea.pack(pady=0)
        else: ea.pack_forget()
        if not idnum or idnum.isspace(): ei.pack(pady=0)
        else: ei.pack_forget()
        if not email or email.isspace(): ee.pack(pady=0)
        else: ee.pack_forget()
        if not phone or phone.isspace(): ep.pack(pady=0)
        else: ep.pack_forget()
def clear_reg():
    txt_n.delete(0,'end'),txt_a.delete(0,'end'),txt_i.delete(0,'end'),txt_e.delete(0,'end'),txt_p.delete(0,'end'),clear_err()
def clear_err():
    en.pack_forget(),ea.pack_forget(),ei.pack_forget(),ee.pack_forget(),ep.pack_forget()
    lbl_conf_add.pack(anchor='center',pady=70)
    lbl_conf_add.config(text="Please fill out ALL the textboxes to register a student",fg='black')

def viewAllFrame():
    forgetFrames(),txt_s_clear(),clear_reg()
    lbl_conf_add.config(text="Please fill out ALL the textboxes to register a student",fg='black'),s_lbl.config(text="",bg='light grey')
    view_all_frame.pack(side='left',fill='y')
def v_refresh():
    v_lbl.config(text=printAll.printAllStudents()),v_frame.update_idletasks(),v_canva.config(scrollregion=v_canva.bbox("all"))
def mouse_scroll(event):
    v_canva.yview_scroll(-1 * (event.delta // 120), "units")

def logout():
    forgetFrames(),clear_reg(),txt_s_clear()
    lbl_conf_add.config(text="Please fill out ALL the textboxes to register a student",fg='black'),menu_frame.pack_forget(),login_usr.delete(0,'end'),login_lbl_err.config(text=" "),s_lbl.config(text=" ",bg='light grey')
    enclosure_frame.place(relx=0.5,rely=0.5,width=350,height=300,anchor='center')

# Login floating frame
enclosure_frame = Frame(root,borderwidth=1,relief="solid",bg='light grey')
enclosure_frame.place(relx=0.5,rely=0.5,width=350,height=300,anchor='center')
Label(enclosure_frame,text="LOG IN",font=("Arial Rounded MT Bold",30),foreground='#c9184a',bg='light grey').pack(pady=(20,0))
login_lbl_err = Label(enclosure_frame,text=f"",font=("Century Gothic",10,'bold'),fg='red',bg='light grey')
login_lbl_err.place(relx=0.5,rely=0.35,anchor='center')
Label(enclosure_frame,text="Enter Student ID-Number*",font=("Arial Rounded MT Bold",16),bg='light grey').pack(padx=(0,80),pady=(60,0))
login_usr = Entry(enclosure_frame,font=("Times New Roman",14),border=1,relief='solid')
login_usr.pack(fill='x',padx=5)
btn_frame = Frame(enclosure_frame,bg='light grey')
btn_frame.pack(side='bottom',fill='x',pady=(5,40))
Button(btn_frame,text="Exit",font=("Arial Rounded MT Bold",16),fg='white',background='#a4133c',width=5,command=exit).pack(side='left',fill='x',expand=True,padx=5)
Button(btn_frame,text="Log In",font=("Arial Rounded MT Bold",16),fg='white',background='#a4133c',width=5,command=login).pack(side='left',fill='x',expand=True,padx=5)
attempt = 0

# Menu sidebar frame
menu_frame = Frame(root,width=300,bg='#ff4d6d')
menu_frame.propagate(False) # False para hindi mag auto adjust yung size ng frame base sa mga widgets
menu_lbl_usr = Label(menu_frame,text="ID:",fg='black',font=("Arial Rounded MT Bold",14),bg='#ff4d6d')
menu_lbl_usr.pack(pady=(25, 25),anchor='w',fill='both')
btns = [("View Your Information",myinfoFrame),("Search Other Student",searchFrame),("Register a New Student",addStuFrame),("View All Student",viewAllFrame),("Log Out",logout),("Exit",exit)]
for i in range(len(btns)):
    Button(menu_frame,text=btns[i][0],fg='white',bg='#a4133c',bd=0,command=btns[i][1],font=("Arial Rounded MT Bold",12),height=3,anchor='e').pack(pady=0,fill='x')

# Initial Frame after login
instruction_frame = Frame(root,width=700,bg='white')
instruction_frame.propagate(False)
inst_lbl = Label(instruction_frame,text="Welcome User",font=('Arial Nova',16),fg='black',bg='white',justify='left')
inst_lbl.place(relx=0.5,rely=0.5,anchor='center')

# MyInfo Frame
myinfo_frame = Frame(root,width=700,bg='#ffccd5')
myinfo_frame.propagate(False)
Label(myinfo_frame,text="Your Information",font=("Arial Rounded MT Bold",24),height=2,bg='white').place(anchor='center',relx=0.5,rely=0.2,relwidth=1.0)
my_lbl = Label(myinfo_frame,text="User",font=('Times New Roman',20,'bold'),justify='center',bg='white')
my_lbl.place(anchor='center',relx=0.5,rely=0.55)

# Search Frame
search_frame = Frame(root,width=700,bg='#ffccd5')
search_frame.propagate(False)
Label(search_frame,text="Search a Student",fg='black',font=("Arial Rounded MT Bold",24),bg="white",height=2).place(anchor='center',relx=0.5,rely=0.2,relwidth=1.0)
txt_s = Entry(search_frame,font=("Times New Roman",14),border=1,relief='solid')
txt_s.place(relx=0.15,rely=0.3,anchor='w',relwidth=0.35)
Button(search_frame,text='Search',font=('Arial Nova',10),fg='white',bg='#a4133c',command=searchStudent).place(relx=0.55,rely=0.3,anchor='w',relwidth=0.1)
Button(search_frame,text='Clear',font=('Arial Nova',10),fg='white',bg='#a4133c',command=txt_s_clear).place(relx=0.68,rely=0.3,anchor='w',relwidth=0.1)
s_lbl = Label(search_frame,text="",font=('Times New Roman',20,'bold'),justify='center',bg='light grey')
s_lbl.place(anchor='center',relx=0.5,rely=0.6)

# Add Stud Frame
add_stu_frame = Frame(root,width=700,bg='#ffccd5')
add_stu_frame.propagate(False)
Label(add_stu_frame,text="Register a Student",font=("Arial Rounded MT Bold",24),height=2,bg='white').pack(side='top',fill='x',pady=(10,2))
# frame para sa mga error
err_frame = Frame(add_stu_frame,bg='#ffccd5',height=180)
en,ea,ei,ee,ep = Label(err_frame,text="Name Required!",font=("Arial Rounded MT Bold",10),height=2,fg='red',bg='#ffccd5'),Label(err_frame,text="Age Required!",font=("Arial Rounded MT Bold",10),height=2,fg='red',bg='#ffccd5'),Label(err_frame,text="ID-Number Required!",font=("Arial Rounded MT Bold",10),height=2,fg='red',bg='#ffccd5'),Label(err_frame,text="Email Required!",font=("Arial Rounded MT Bold",10),height=2,fg='red',bg='#ffccd5'),Label(err_frame,text="Phone Required!",font=("Arial Rounded MT Bold",10),height=2,fg='red',bg='#ffccd5')
# frame para sa horizontal alignment ng name at age at ang kanilang textbox
sec1_frame = Frame(add_stu_frame,bg='#ffccd5')
Label(sec1_frame,text="Name*",font=("Arial Rounded MT Bold",10),bg='#ffccd5').pack(side='left',padx=(5,36))
txt_n = Entry(sec1_frame,font=("Times New Roman",14),border=1,relief='solid')
txt_n.pack(side='left',padx=(5,15),expand=True,fill='x')
Label(sec1_frame,text="Age*",font=("Arial Rounded MT Bold",10),bg='#ffccd5').pack(side='left',padx=(15,5))
txt_a = Entry(sec1_frame,font=("Times New Roman",14),border=1,relief='solid')
txt_a.pack(side='left',padx=(5,15),expand=True,fill='x')
# frame para sa horizontal alignment ng phone at textbox
sec2_frame = Frame(add_stu_frame,bg='#ffccd5')
Label(sec2_frame,text="ID-Number*",font=("Arial Rounded MT Bold",10),bg='#ffccd5').pack(side='left',padx=5)
txt_i = Entry(sec2_frame,font=("Times New Roman",14),border=1,relief='solid')
txt_i.pack(side='left',padx=(5,15),expand=True,fill='x')
Label(sec2_frame,text="Email*",font=("Arial Rounded MT Bold",10),bg='#ffccd5').pack(side='left',padx=(7,3))
txt_e = Entry(sec2_frame,font=("Times New Roman",14),border=1,relief='solid')
txt_e.pack(side='left',padx=(5,15),expand=True,fill='x')
# frame para sa horizontal alignment ng phone at textbox
sec3_frame = Frame(add_stu_frame,bg='#ffccd5')
Label(sec3_frame,text="Phone*",font=("Arial Rounded MT Bold",10),bg='#ffccd5').pack(side='left',padx=(5,38))
txt_p = Entry(sec3_frame,font=("Times New Roman",14),border=1,relief='solid',width=28)
txt_p.pack(side='left',padx=0,anchor='w',expand=True)
# frame para sa clear at register button
sec_btn = Frame(add_stu_frame,bg='#ffccd5') 
Button(sec_btn,text="Clear",font=("Arial Rounded MT Bold",10),fg='white',background='#a4133c',width=10,command=clear_reg).pack(side='left',padx=8,anchor='w')
Button(sec_btn,text="Register",font=("Arial Rounded MT Bold",10),fg='white',background='#a4133c',width=10,command=reg_stud).pack(side='right',padx=15,anchor='e')
# packing ng mga frames sa isang linya hiwa-hiwalay pa din yan kaya lang gawing one line gamit comma
err_frame.pack(pady=0,fill='x'),sec_btn.pack(side='bottom',fill='x',pady=(15,120)),sec3_frame.pack(side='bottom',fill='x',pady=15),sec2_frame.pack(side='bottom',fill='x',pady=15),sec1_frame.pack(side='bottom',fill='x',pady=15)

lbl_conf_add = Label(err_frame,text="Please fill out ALL the textboxes to register a student.",font=("Arial Rounded MT Bold",12),fg='black',bg='#ffccd5')
lbl_conf_add.pack(anchor='center',pady=70)

# View ALl Stud frame
view_all_frame = Frame(root,width=700,bg='#ffccd5')
view_all_frame.propagate(False)
Label(view_all_frame,text="All Student List",font=("Arial Rounded MT Bold",24),height=2,bg='white').pack(fill='x',pady=(20, 10))
Button(view_all_frame,text="Refresh",font=('Arial Nova',10,'bold'),fg='white',bg='#a4133c',width=20,command=v_refresh).pack(side='top',pady=3,padx=(10, 600))
v_canva = Canvas(view_all_frame,bg='light grey')
v_canva.pack(side='left',fill='both',expand=True,pady=(10, 0))
v_frame = Frame(v_canva,bg='light grey')
v_canva.create_window((0, 0), window=v_frame, anchor='nw')
v_lbl = Label(v_frame,text=printAll.printAllStudents(),font=('Times New Roman',17,'bold'),justify='center',bg='white')
v_lbl.pack()
scroller = Scrollbar(view_all_frame,orient='vertical',command=v_canva.yview)
scroller.pack(side='right',fill='y')
v_frame.update_idletasks()
v_canva.config(yscrollcommand=scroller.set,scrollregion=v_canva.bbox("all"))
v_canva.bind_all('<MouseWheel>', mouse_scroll) # para magamit mousewheel pang scroll

root.title("Python Student Info System")
root.config(bg='#590d22')
root.geometry("1000x600+185+60")
root.resizable(False,False)
root.mainloop()