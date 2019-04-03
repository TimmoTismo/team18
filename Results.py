currentuser=open("CurrentUser.txt","r")
User=currentuser.readlines()

from tkinter import *
import csv

class Results(Frame):
	def __init__(self,master, student_score):
		Frame.__init__(self,master)
		self.grid()
		self.newPage(student_score)

		def newPage(self, student_score):
			Label(self, width="10", height="2").grid(row=0, column=0)
			Label(self, text="Student Results", font=('Helvetica', 8)).grid(row=2, column=0)


root = Tk()
root.title("Results")
root.resizable(0,0) 
root.geometry("200x200") 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
