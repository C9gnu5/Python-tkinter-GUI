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

tries = 0

def login():
    global tries
    user = searcher.verify_login(txt_login.get()) # nasa searcher_student.py yung verify_login na function
    if not txt_login.get() or txt_login.get().isspace(): # kapag blanko o white space ang sinearch ng user
        tries += 1
        login_error.config(text=f"Enter an ID-Number!\nRemaining attempts: {3-tries}")
    elif user: # kapag nag return yung function ng student object
        enclosure_frame.place_forget()
        lbl_menu.config(text=f"User:\n{user.getIdNum()}")
        frame_ng_menu.pack(side='top',fill='x')
        lbl_initial.config(text=f"Welcome {user.getName()}!\nYou can choose options on the top bar menu to:\n\n   - View your information\n   - Search other student\n   - Register a new student\n   - View the student list\n   - Log out\n   - Exit")
        initial_frame.pack(side='bottom',fill='x')
        tries = 0
    else: # kapag False ang ni-return nung function
        tries += 1
        login_error.config(text=f"ID-Number {txt_login.get()} Not Found!\nRemaining attempts: {3-tries}")
    if tries == 3:
        exit()

def my_info():
    user = searcher.search_student(txt_login.get())
    initial_frame.pack_forget()
    myinfo_frame.pack_forget()
    search_frame.pack_forget()
    add_stu_frame.pack_forget()
    view_all_frame.pack_forget()
    searchbox_clear()
    clear_form()
    lbl_stu_added.config(text=" ")
    lbl_my_info.config(text=user)
    lbl_search.config(text=" ",bg='#385756')
    myinfo_frame.pack(side='bottom',fill='x')

def search_stud():
    initial_frame.pack_forget()
    myinfo_frame.pack_forget()
    search_frame.pack_forget()
    add_stu_frame.pack_forget()
    view_all_frame.pack_forget()
    clear_form()
    lbl_stu_added.config(text=" ")
    search_frame.pack(side='bottom',fill='x')

def search():
    stud = searcher.search_student(searchbox.get())
    if stud:
        lbl_search.config(text=stud,bg='white')
    elif searchbox.get().isspace() or not searchbox.get():
        lbl_search.config(text="Please Enter a Student ID-Number!",bg='white')
    else:
        lbl_search.config(text=f"There is no {searchbox.get()} Student ID-Number!",bg='white')
    searchbox_clear()

def searchbox_clear():
    searchbox.delete(0,'end')

def register():
    initial_frame.pack_forget()
    myinfo_frame.pack_forget()
    search_frame.pack_forget()
    add_stu_frame.pack_forget()
    view_all_frame.pack_forget()
    searchbox_clear()
    lbl_search.config(text="",bg='#385756')
    add_stu_frame.pack(side='bottom',fill='x')

def add_stud():
    name,age,idnum,email,phone = name_add.get(),age_add.get(),idnum_add.get(),email_add.get(),phone_add.get()
    if name and age and idnum and email and phone:
        addstu.add_student(name,age,idnum,email,phone)
        clear_form()
        tanggal_error()
        lbl_stu_added.config(text=f"Added student {name} to the list.")
    else:
        if not name or name.isspace():
            name_error.config(text="Name Required!")
        else:
            name_error.config(text=" ")
        if not age or age.isspace():
            age_error.config(text="Age Required!")
        else:
            age_error.config(text=" ")
        if not idnum or idnum.isspace():
            idnum_error.config(text="ID-Number Required!")
        else:
            idnum_error.config(text=" ")
        if not email or email.isspace():
            email_error.config(text="Email Required!")
        else:
            email_error.config(text=" ")
        if not phone or phone.isspace():
            phone_error.config(text="Phone Required!")
        else:
            phone_error.config(text=" ")

def clear_form():
    name_add.delete(0,'end')
    age_add.delete(0,'end')
    idnum_add.delete(0,'end')
    email_add.delete(0,'end')
    phone_add.delete(0,'end')
    lbl_stu_added.config(text=f" ")
    tanggal_error()

def tanggal_error():
    name_error.config(text=" ")
    age_error.config(text=" ")
    idnum_error.config(text=" ")
    email_error.config(text=" ")
    phone_error.config(text=" ")

def print_all_stud():
    initial_frame.pack_forget()
    myinfo_frame.pack_forget()
    search_frame.pack_forget()
    add_stu_frame.pack_forget()
    view_all_frame.pack_forget()
    searchbox_clear()
    clear_form()
    lbl_stu_added.config(text=" ")
    lbl_search.config(text="",bg='#385756')
    view_all_frame.pack(side='bottom',fill='both',expand=True)

def refresh():
    lbl_all_stud.config(text=printAll.printAllStudents())
    canvas_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def mouse_scroller(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

def logout():
    initial_frame.pack_forget()
    myinfo_frame.pack_forget()
    search_frame.pack_forget()
    add_stu_frame.pack_forget()
    view_all_frame.pack_forget()
    clear_form()
    searchbox_clear()
    lbl_stu_added.config(text=" ")
    frame_ng_menu.pack_forget()
    txt_login.delete(0,'end')
    login_error.config(text=" ")
    lbl_search.config(text=" ",bg='#385756')
    enclosure_frame.place(relx=0.5,rely=0.5,width=350,height=250,anchor='center')

# Login floating frame
enclosure_frame = Frame(root,borderwidth=1,relief="solid",bg='#9bbfbf')
enclosure_frame.place(relx=0.5,rely=0.5,width=350,height=250,anchor='center')
Label(enclosure_frame,text="LOG IN",font=("Arial Rounded MT Bold",28),bg='#9bbfbf').pack(pady=(5,0))
login_error = Label(enclosure_frame,text=f"",font=("Century Gothic",10,'bold'),fg='#ff3535',bg='#9bbfbf')
login_error.place(relx=0.5,rely=0.3,anchor='center')
Label(enclosure_frame,text="Enter Student ID-Number*",font=("Arial Rounded MT Bold",16),bg='#9bbfbf').pack(padx=(4,80),pady=(40,0))
txt_login = Entry(enclosure_frame,font=("Times New Roman",14),border=1,relief='solid')
txt_login.pack(fill='x',padx=5,pady=(1,5))
Button(enclosure_frame,text="Log In",font=("Arial Rounded MT Bold",16),fg='white',background='#507c79',width=5,command=login).pack(fill='x',expand=True,padx=5,pady=3)
Button(enclosure_frame,text="Exit",font=("Arial Rounded MT Bold",16),fg='white',background='#507c79',width=5,command=exit).pack(fill='x',expand=True,padx=5,pady=3)
# Login floating frame end

# Menu sidebar frame
frame_ng_menu = Frame(root,height=100,bg='#9bbfbf')
frame_ng_menu.propagate(False) # False para hindi mag auto adjust yung size ng frame base sa mga widgets
lbl_menu = Label(frame_ng_menu,text="User:",fg='black',font=("Arial Rounded MT Bold",14),bg='#9bbfbf')
lbl_menu.pack(pady=(25, 25),padx=(5,10),anchor='w',fill='both',side='left')
Button(frame_ng_menu,text="View Your\nInformation",fg='white',bg='#507c79',command=my_info,font=('Arial Rounded MT Bold',10),height=3,width=15,anchor='center',bd=1,relief='solid').pack(pady=0,padx=3,side='left',fill='x',expand=True)
Button(frame_ng_menu,text="Search Other\nStudent",fg='white',bg='#507c79',command=search_stud,font=('Arial Rounded MT Bold',10),height=3,width=15,anchor='center',bd=1,relief='solid').pack(pady=0,padx=3,side='left',fill='x',expand=True)
Button(frame_ng_menu,text="Register a New\nStudent",fg='white',bg='#507c79',command=register,font=('Arial Rounded MT Bold',10),height=3,width=15,anchor='center',bd=1,relief='solid').pack(pady=0,padx=3,side='left',fill='x',expand=True)
Button(frame_ng_menu,text="View All\nStudent",fg='white',bg='#507c79',command=print_all_stud,font=('Arial Rounded MT Bold',10),height=3,width=15,anchor='center',bd=1,relief='solid').pack(pady=0,padx=3,side='left',fill='x',expand=True)
Button(frame_ng_menu,text="Log Out",fg='white',bg='#507c79',command=logout,font=('Arial Rounded MT Bold',10),height=3,width=15,anchor='center',bd=1,relief='solid').pack(pady=0,padx=3,side='left',fill='x',expand=True)
Button(frame_ng_menu,text="Exit",fg='white',bg='#507c79',command=exit,font=('Arial Rounded MT Bold',10),height=3,width=15,anchor='center',bd=1,relief='solid').pack(pady=0,padx=3,side='left',fill='x',expand=True)
# Menu sidebar frame end

# Initial Frame after login
initial_frame = Frame(root,height=600,bg='light grey')
initial_frame.propagate(False)
lbl_initial = Label(initial_frame,text="Welcome User",font=('Arial Nova',16),fg='black',bg='light grey',justify='left')
lbl_initial.place(relx=0.5,rely=0.5,anchor='center')
# Initial Frame after login end

# MyInfo Frame
myinfo_frame = Frame(root,height=600,bg='#385756')
myinfo_frame.propagate(False)
Label(myinfo_frame,text="Your Information",font=("Arial Rounded MT Bold",24),height=2,bg='white').place(anchor='center',relx=0.5,rely=0.15,relwidth=1.0)
lbl_my_info = Label(myinfo_frame,text="User",font=('Times New Roman',20,'bold'),justify='center',bg='white')
lbl_my_info.place(anchor='center',relx=0.5,rely=0.55,relwidth=1.0)
# MyInfo Frame end

# Search Frame
search_frame = Frame(root,height=600,bg='#385756')
search_frame.propagate(False)
Label(search_frame,text="Search a Student",fg='black',font=("Arial Rounded MT Bold",24),bg="white",height=2).place(anchor='center',relx=0.5,rely=0.15,relwidth=1.0)
searchbox = Entry(search_frame,font=("Times New Roman",14),border=1,relief='solid')
searchbox.place(relx=0.15,rely=0.3,anchor='w',relwidth=0.35)
Button(search_frame,text='Search',font=('Arial Nova',10),fg='white',bg='#507c79',command=search).place(relx=0.55,rely=0.3,anchor='w',relwidth=0.1)
Button(search_frame,text='Clear',font=('Arial Nova',10),fg='white',bg='#507c79',command=searchbox_clear).place(relx=0.68,rely=0.3,anchor='w',relwidth=0.1)
lbl_search = Label(search_frame,text=" ",font=('Times New Roman',20,'bold'),justify='center',bg='#385756')
lbl_search.place(anchor='center',relx=0.5,rely=0.6,relwidth=1.0)
# Search Frame end

# Add Stud Frame
add_stu_frame = Frame(root,height=600,bg='#385756')
add_stu_frame.propagate(False)
Label(add_stu_frame,text="Register a Student",font=("Arial Rounded MT Bold",24),height=2,bg='white').pack(side='top',fill='x',pady=(10,2))
lbl_stu_added = Label(add_stu_frame,text=" ",font=("Arial Rounded MT Bold",12),fg='#2CDD3E',bg='#385756')
lbl_stu_added.pack(pady=10)
# frame para sa horizontal alignment ng name at age at ang kanilang textbox
sec1_frame = Frame(add_stu_frame,bg='#385756') # one line name/age
sub_sec1 = Frame(sec1_frame,bg='#385756') # para sa name, textbox, at error label
Label(sub_sec1,text="Name*",font=("Arial Rounded MT Bold",10),bg='#385756',fg='white').pack(side='left',padx=(5,36))
name_add = Entry(sub_sec1,font=("Times New Roman",14),border=1,relief='solid',width=25)
name_add.pack(side='left',padx=(5,15))
name_error = Label(sub_sec1,text=" ",font=("Arial Rounded MT Bold",10),height=2,fg='#ff3535',bg='#385756',width=20,anchor='w')
name_error.pack(side='left',pady=0)

sub2_sec1 = Frame(sec1_frame,bg='#385756') # para sa age, textbox, at error label
Label(sub2_sec1,text="Age*",font=("Arial Rounded MT Bold",10),bg='#385756',fg='white').pack(side='left',padx=(5,5))
age_add = Entry(sub2_sec1,font=("Times New Roman",14),border=1,relief='solid',width=25)
age_add.pack(side='left',padx=(6,15))
age_error = Label(sub2_sec1,text=" ",font=("Arial Rounded MT Bold",10),height=2,fg='#ff3535',bg='#385756')
age_error.pack(side='left',pady=0,padx=(0,15))
sub_sec1.pack(side='left',padx=0,fill='x'),sub2_sec1.pack(side='left',padx=0,fill='x')
# frame para sa horizontal alignment ng name at age at ang kanilang textbox
sec2_frame = Frame(add_stu_frame,bg='#385756')  # one line idnum/email
sub_sec2 = Frame(sec2_frame,bg='#385756') # para sa idnum, textbox, at error label
Label(sub_sec2,text="ID-Number*",font=("Arial Rounded MT Bold",10),bg='#385756',fg='white').pack(side='left',padx=5)
idnum_add = Entry(sub_sec2,font=("Times New Roman",14),border=1,relief='solid',width=25)
idnum_add.pack(side='left',padx=(5,2))
idnum_error = Label(sub_sec2,text=" ",font=("Arial Rounded MT Bold",10),height=2,fg='#ff3535',bg='#385756',width=20)
idnum_error.pack(side='left',pady=0,)

sub2_sec2 = Frame(sec2_frame,bg='#385756') # para sa email, textbox, at error label
Label(sub2_sec2,text="Email*",font=("Arial Rounded MT Bold",10),bg='#385756',fg='white').pack(side='left',padx=(7,3))
email_add = Entry(sub2_sec2,font=("Times New Roman",14),border=1,relief='solid',width=25)
email_add.pack(side='left',padx=(5,15))
email_error = Label(sub2_sec2,text=" ",font=("Arial Rounded MT Bold",10),height=2,fg='#ff3535',bg='#385756')
email_error.pack(side='right',pady=0)
sub_sec2.pack(side='left',padx=0,fill='x'),sub2_sec2.pack(side='left',padx=0,fill='x')
# frame para sa horizontal alignment ng phone at textbox at error label
sec3_frame = Frame(add_stu_frame,bg='#385756')
Label(sec3_frame,text="Phone*",font=("Arial Rounded MT Bold",10),bg='#385756',fg='white').pack(side='left',padx=(5,38))
phone_add = Entry(sec3_frame,font=("Times New Roman",14),border=1,relief='solid',width=25)
phone_add.pack(side='left',padx=(0,15))
phone_error = Label(sec3_frame,text=" ",font=("Arial Rounded MT Bold",10),height=2,fg='#ff3535',bg='#385756')
phone_error.pack(side='left',pady=0)
# frame para sa clear at register button
sec_btn = Frame(add_stu_frame,bg='#385756')
Button(sec_btn,text="Clear",font=("Arial Rounded MT Bold",10),fg='white',background='#507c79',width=10,command=clear_form).pack(side='left',padx=8,anchor='w')
Button(sec_btn,text="Register",font=("Arial Rounded MT Bold",10),fg='white',background='#507c79',width=10,command=add_stud).pack(side='right',padx=15,anchor='e')
# packing ng mga frames sa isang linya hiwa-hiwalay pa din yan kaya lang gawing one line gamit comma
sec1_frame.pack(fill='x',pady=15,padx=20),sec2_frame.pack(fill='x',pady=15,padx=20),sec3_frame.pack(fill='x',pady=15,padx=20),sec_btn.pack(fill='x',pady=15)
# Add Stud Frame end

# View ALl Stud frame
view_all_frame = Frame(root,height=600,bg='#385756')
view_all_frame.propagate(False)
Label(view_all_frame,text="All Student List",font=("Arial Rounded MT Bold",24),height=2,bg='white').pack(fill='x',pady=(20, 10))
Button(view_all_frame,text="Refresh",font=('Arial Nova',10,'bold'),fg='white',bg='#507c79',width=20,command=refresh).pack(side='top',pady=3,padx=(5, 750))
canvas = Canvas(view_all_frame,bg='grey')
canvas.pack(side='left',fill='both',expand=True,pady=(10, 0))
canvas_frame = Frame(canvas,bg='grey')
canvas.create_window((0, 0), window=canvas_frame, anchor='nw')
lbl_all_stud = Label(canvas_frame,text=printAll.printAllStudents(),font=('Times New Roman',20,'bold'),justify='center',bg='white',width=61)
lbl_all_stud.pack(fill='both',expand=True)
scroller = Scrollbar(view_all_frame,orient='vertical',command=canvas.yview)
scroller.pack(side='right',fill='y',padx=0)
canvas_frame.update_idletasks()
canvas.config(yscrollcommand=scroller.set,scrollregion=canvas.bbox("all"))
canvas.bind_all('<MouseWheel>', mouse_scroller) # para magamit mousewheel pang scroll
# View ALl Stud frame

root.title("Python Student Info System")
root.config(bg='#385756')
root.geometry("1000x700+185+10")
root.resizable(False,False)
root.mainloop()
