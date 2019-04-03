currentuser=open("CurrentUser.txt","r")
User=currentuser.readlines() #checking current user

from tkinter import *
import csv

class Results(Frame): #creating the frame for the results to be shown
	def __init__(self,master, student_score):
		Frame.__init__(self,master)
		self.grid()
		self.newPage(student_score)

		def newPage(self, student_score):
			Label(self, width="10", height="2").grid(row=0, column=0)
			Label(self, text="Student Results", font=('Helvetica', 8)).grid(row=2, column=0)
			#Results from the tests are stored with the username and scores in a csv file, this would have been read into here and then used to display the results.

			#feedback and results would have been imported from relative csv, then using the currentuser would show only the relevant data here in future version
root = Tk()
root.title("Results")
root.resizable(0,0) 
root.geometry("200x200") 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
