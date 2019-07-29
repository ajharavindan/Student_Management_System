from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import cx_Oracle
import bs4	
import requests
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image,ImageTk
import tkinter as tk
import socket
import datetime
import os

root=Tk()
root.title("S.M.S")
root.geometry("400x400+200+200")
root.overrideredirect(True)
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
res =requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
soup=bs4.BeautifulSoup(res.text,'lxml')
quote=soup.find('img',{"class":"p-qotd"})
ps=("https://www.brainyquote.com"+quote['data-img-url'])
r=requests.get(ps)
with open("AAj ka poster.PNG ",'wb') as f:
	f.write(r.content)
size=300,300
filename="AAj ka poster.PNG"

file_parts=os.path.splitext(filename)
outfile=file_parts[0]+"300x300"+file_parts[1]
try:
	img=Image.open(filename)
	img1=img.resize(size,Image.ANTIALIAS)
	img1.save(outfile,"PNG")
except IOError as e:
	print("An exception occured")

path = "AAj ka poster300x300.PNG"
img = ImageTk.PhotoImage(Image.open(path))
canvas.create_image(0,20, anchor=NW, image=img)


try:
	city="Mumbai"
	socket.create_connection(("www.google.com",80))
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address=a1+a2+a3
	res1 =requests.get(api_address)
	wdata=requests.get(api_address).json()
	main=wdata['main']
	temp=main['temp']
	v="Temperature",temp
	p=" City "+city
except OSError:
	print("Check Network")
c=Label(root,text=p)
t = Label(root,text=v)
c.pack(pady=10)
t.pack(pady=2)
root.after(5000, root.destroy)
root.mainloop()



root = Tk()
root.title("S. M. S ")
root.geometry("400x400+200+200")

def f1():
	adSt.deiconify()
	root.withdraw()

def f3():
	viSt.deiconify()
	root.withdraw()
	con = None
	cursor  = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from student "
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ' '
		for d in data:
			msg = msg + "Rno  " + str(d[0]) +"Name  " + str(d[1]) + "Marks  " + str(d[2]) + "\n"
		stData.insert(INSERT, msg)

	except cx_Oracle.DatabaseError as e:
		print("select issue ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f9():
	upDt.deiconify()
	root.withdraw()

def f10():
	deL.deiconify()
	root.withdraw()

def f13():
	con = None
	cursor =None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		name = []
		marks = []

		for d in data:
			n = str(d[1])
			x = int(d[2]) 
			name.append(n)  
			marks.append(x)
		print(name,marks)

	except cx_Oracle.DatabaseError as e:
		messagebox.showwarning("Failure", "Insert issues " + str(e))

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		
	fig = plt.figure("Visualize")
	plt.bar(name,marks)
	plt.show()


btnAdd = Button(root, text ="Add", font =("arial", 16, 'bold'),width = 10, command = f1)
btnView = Button(root, text ="View", font =("arial", 16, 'bold'),width = 10, command = f3)
btnUpdate = Button(root, text ="Update", font =("arial", 16, 'bold'),width = 10, command = f9)
btnDelete = Button(root, text ="Delete", font =("arial", 16, 'bold'),width = 10, command = f10)
btnGraph = Button(root, text ="Graph", font =("arial", 16, 'bold'),width = 10,command = f13)

btnAdd.pack(pady = 10)
btnView.pack(pady = 10)
btnUpdate.pack(pady = 10)
btnDelete.pack(pady = 10)
btnGraph.pack(pady = 10)

adSt = Toplevel(root)
adSt.title("Add Student ")
adSt.geometry("400x400+200+200")
adSt.withdraw()

def f2():
	root.deiconify()
	adSt.withdraw()

def f5():
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		srno = entAddRno.get()
		if srno.isdigit() and int(srno) > 0:
			rno = int(srno)
		else:
			messagebox.showerror("Mistake", "incorrect rno")
			entAddRno.focus()
			return

		sname = entAddName.get()
		if sname.isalpha():
			name = str(sname)
		else:
			messagebox.showerror("Mistake ", "Incorrect name")
			entAddName.focus()
			return

		smarks = entAddMarks.get()
		if smarks.isdigit():
			marks = int(smarks)
		else:
			messagebox.showerror("Mistake", "incorrect marks")
			entAddMarks.focus()
			return
		
		cursor = con.cursor()
		sql = "insert into student values('%d', '%s','%d')"
		args = (rno, name, marks)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + " rows inserted "
		messagebox.showinfo("Success ",msg)
	

	except cx_Oracle.DatabaseError as e:
		con.rollback()
		message.showinfo("Failure ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

lblAddRno = Label(adSt, text = "Enter rno")
entAddRno = Entry(adSt, bd = 5)
lblAddRno.pack(pady = 10)
entAddRno.pack(pady = 10)

lblAddName = Label(adSt, text = "Enter name ")
entAddName = Entry(adSt, bd = 5)
lblAddName.pack(pady = 10)
entAddName.pack(pady = 10)

lblAddMarks = Label(adSt,text = "Enter marks ")
entAddMarks = Entry(adSt, bd = 5)
lblAddMarks.pack(pady = 10)
entAddMarks.pack(pady = 10)

btnAddSave = Button(adSt , text = "Save ",command = f5)
btnAddBack = Button(adSt , text = "Back ",command = f2)


btnAddSave.pack(pady = 10)
btnAddBack.pack(pady = 10)

def f4():
	root.deiconify()
	viSt.withdraw()

viSt = Toplevel(root)
viSt.title("View student ")
viSt.geometry("400x400+200+200")
viSt.withdraw()

stData = scrolledtext.ScrolledText(viSt, width = 30, height =5)
btnViewBack = Button(viSt, text = "Back ",command = f4)
stData.pack(pady =10)
btnViewBack.pack(pady =10)

def f7():
	root.deiconify()
	upDt.withdraw()

def f6():
	try:
		con = None
		cursor = None
	
		a = entAddRno1.get().isdigit()
		b = entAddName1.get().isalpha()
		c = entAddMarks1.get().isdigit()

		if(a == False):
			messagebox.showwarning("Failure", "Please enter only positive integers ")	
			entAddRno1.delete(0,END)
			entAddRno1.focus()
		
		elif (b == False):
			messagebox.showwarning("Failure", "Please enter only alphabets ")	
			entAddName1.delete(0,END)
			entAddName1.focus()
	
		elif (c == False):
			messagebox.showwarning("Failure", "Please Enter marks in integers ")	
			entAddMarks1.delete(0,END)
			entAddMarks1.focus()
	
		try:
			con = cx_Oracle.connect("system/abc123")
			rno = int(entAddRno1.get())
			x = entAddName1.get()
			name = x.title()
			marks = int(entAddMarks1.get())
			cursor = con.cursor()
			sql = "UPDATE student SET  marks= %d, name= '%s' WHERE rno= %d"
			args = (marks,name,rno)
			cursor.execute(sql % args) 
			con.commit()
			msg = str(cursor.rowcount) + " rows updated."
			messagebox.showinfo("Success", msg)
			upDt.withdraw()
			entAddRno1.delete(0,END)
			entAddName1.delete(0,END)	
			entAddMarks1.delete(0,END)
			root.deiconify()
			
		
		except cx_Oracle.DatabaseError as e:
			messagebox.showwarning("Failure", "Insert issues " + str(e))
			con.rollback()
		finally:
			if cursor is not None:
				cursor.close()
			if con is not None:
				con.close()

	except ValueError:
		print("Please insert values wherever required.")


upDt = Toplevel(root)
upDt.title("Add Student ")
upDt.geometry("400x400+200+200")
upDt.withdraw()

lblAddRno1 = Label(upDt, text = "Enter rno")
entAddRno1 = Entry(upDt, bd = 5)
lblAddRno1.pack(pady = 10)
entAddRno1.pack(pady = 10)

lblAddName1 = Label(upDt, text = "Enter name ")
entAddName1 = Entry(upDt, bd = 5)
lblAddName1.pack(pady = 10)
entAddName1.pack(pady = 10)

lblAddMarks1 = Label(upDt,text = "Enter marks ")
entAddMarks1 = Entry(upDt, bd = 5)
lblAddMarks1.pack(pady = 10)
entAddMarks1.pack(pady = 10)

btnAddSave1 = Button(upDt , text = "Save ",command = f6)
btnAddBack1 = Button(upDt , text = "Back ",command = f7)

btnAddSave1.pack(pady = 10)
btnAddBack1.pack(pady = 10)

def f11():
	root.deiconify()
	deL.withdraw()

def f12():
	try:
		con = None
		cursor = None
		a = entAddRno2.get().isdigit()
		
		if(a == False):
			messagebox.showwarning("Failure", "Please enter only positive integers.")	
			entAddRno2.delete(0,END)
			entAddRno2.focus()
		else:
			pass
		try:
			con = cx_Oracle.connect("system/abc123")
			rno = int(entAddRno2.get())
			cursor = con.cursor()
			sql = "delete from student where rno = %d"
			args = (rno)
			cursor.execute(sql % args)
			con.commit()
			msg = str(cursor.rowcount) + " rows deleted."
			messagebox.showinfo("Success", msg)
			deL.withdraw()
			entAddRno2.delete(0,END)
			root.deiconify()
		
		except cx_Oracle.DatabaseError as e:
			messagebox.showwarning("Failure", "Insert issues " + str(e))
			entAddRno2.delete(0,END)
			entAddRno2.focus()
			con.rollback()
		finally:
			if cursor is not None:
				cursor.close()
			if con is not None:
				con.close()
	except ValueError:
		print("Please insert values wherever required.")

deL = Toplevel(root)
deL.title("Delete Student ")
deL.geometry("400x400+200+200")
deL.withdraw()

lblAddRno2 = Label(deL, text = "Enter rno")
entAddRno2 = Entry(deL, bd = 5)
lblAddRno2.pack(pady = 10)
entAddRno2.pack(pady = 10)

btnAddSave2 = Button(deL , text = "Save ",command = f12)
btnAddBack2 = Button(deL , text = "Back ",command = f11)

btnAddSave2.pack(pady = 10)
btnAddBack2.pack(pady = 10)

root.mainloop()