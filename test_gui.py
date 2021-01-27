from tkinter import *
import tkinter.messagebox
#pack:   side=TOP/RIGHT/BOTTOM/LEFT;   fill=X/Y
#label:   sticky=N/E/S/W

def leftClick(event):
	print('leftClick')
	return None

def scrollClick(event):
	print('scrollClick')
	return None

def rightCLick(event):
	print('rightCLick')
	return None

def Hello():
	print('Hi')
	return None

def doStuff():
	print('do something')
	return None

def printInfo():
	print('entered data: \n Name:',entry1.get(),'\n Password:',entry2.get(),'\n check:',checklog.get())
	response.config(text='you tried to log in!')
	return None

#blank window
root = Tk()

#drop down menu
myMenu = Menu(root)
root.config(menu=myMenu)
subMenu1 = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label='File', menu=subMenu1)
subMenu1.add_command(label='New Project', command=doStuff)
subMenu1.add_command(label='Open Project', command=doStuff)
subMenu1.add_separator()
subMenu1.add_command(label='Exit', command=doStuff)
subMenu2 = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label='Edit', menu=subMenu2)
subMenu2.add_command(label='Tool', command=doStuff)
subMenu2.add_separator()
subMenu2.add_command(label='Forward', command=doStuff)
subMenu2.add_command(label='Backward', command=doStuff)

#toolbar
toolbar = Frame(root, bg='blue')
insertButton1 = Button(toolbar, text='Insert Image', command=doStuff)
insertButton2 = Button(toolbar, text='Print Image', command=doStuff)
insertButton1.pack(side=LEFT, padx=3, pady=3)
insertButton2.pack(side=LEFT, padx=3, pady=3)
toolbar.pack(side=TOP, fill=X)

#statusbar
statusbar = Frame(root)
statusbar.pack(side=BOTTOM, fill=X)
status = Label(statusbar, text='Status: It\'s working', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

#content: frame1 (text & buttons)
frame1= Frame(root, width=400, height=200)
frame1.pack_propagate(0) #window size not dependent on content width
#frame1.grid_propagate(0)
frame1.pack()
label1 = Label(frame1, text='this is a template for a simple gui', fg="blue", bg="white")
label2 = Label(frame1, text='more text', fg="black", bg="yellow")
label1.pack()
label2.pack()
button1 = Button(frame1, text='print Hello', command=Hello)
button2 = Button(frame1, text='button distinguishes mouse clicks')
button1.pack()
button2.pack()
button2.bind('<Button-1>', leftClick)
button2.bind('<Button-2>', scrollClick)
button2.bind('<Button-3>', rightCLick)

#content: frame2 (login)
frame2= Frame(root, width=400, height=200)
#frame2.pack_propagate(0)
frame2.grid_propagate(0)
frame2.pack()
label5 = Label(frame2, text='Name')
label6 = Label(frame2, text='Password')
entry1 = Entry(frame2)
entry2 = Entry(frame2)
checklog = IntVar()
check = Checkbutton(frame2, text='check', variable=checklog)
submitb = Button(frame2, text='submit', command=printInfo)
label5.grid(row=0,column=0, sticky=E) #NESW
label6.grid(row=1,column=0, sticky=E)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
check.grid(row=3,columnspan=2)
submitb.grid(row=4,columnspan=2)
response = Label(frame2, text=' ')
response.grid(row=5,columnspan=2)

#content: frame3 (canvas)
frame3 = Frame(root, width=400, height=200)
frame3.pack_propagate(0)
#frame3.grid_propagate(0)
frame3.pack()
canvas = Canvas(frame3)
canvas.pack()
blackline = canvas.create_line(0,0,200,50)
redline = canvas.create_line(0,100,200,50,fill='red')
greenbox = canvas.create_rectangle(25,25,130,60,fill='green')
#canvas.delete(blackline)
#canvas.delete(ALL)

#content: frame4 (image)
frame4 = Frame(root)
frame4.pack()
photo1 = PhotoImage(file='rubiks.png')
label0 = Label(frame4, image=photo1, width='200', height='200', bg='red')
label0.pack()

#messages
tkinter.messagebox.showinfo('Window Title', 'some information ...')
answer = tkinter.messagebox.askquestion('Question Title', 'important Question, say y/n')

if answer=='yes':
	print('you said yes')
else:
	print('you said no')

#keep window open
root.mainloop()