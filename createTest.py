from tkinter import *
import tkinter.messagebox as tkMessageBox
import csv
import datetime

class createTest(Frame):

	def saveTest(self):
		index = self.listTest.curselection()[0]
		testType = str(self.listTest.get(index))
		strMsg = ""

		testTitle = str(self.TitleEntry.get())
		if testTitle == "":
			strMsg = strMsg + "Title can not be left blank"

		try:
			intDay = int(self.entDay.get())
			intMonth = int(self.entMonth.get())
			intYear = int(self.entYear.get())
		except:
			strMsg = strMsg + "Invalid date"


		if strMsg == "":
			with open(testTitle +'.csv', mode='w', newline="") as f:
			    test_writer = csv.writer(f)

			    test_writer.writerow([self.Q1Entry.get(), self.Q1aEntry.get(), self.Q1bEntry.get(), self.Q1cEntry.get(), self.Q1dEntry.get()])
			    test_writer.writerow([self.Q2Entry.get(), self.Q2aEntry.get(), self.Q2bEntry.get(), self.Q2cEntry.get(), self.Q2dEntry.get()])
			    test_writer.writerow([self.Q3Entry.get(), self.Q3aEntry.get(), self.Q3bEntry.get(), self.Q3cEntry.get(), self.Q3dEntry.get()])
			    test_writer.writerow([self.Q4Entry.get(), self.Q4aEntry.get(), self.Q4bEntry.get(), self.Q4cEntry.get(), self.Q4dEntry.get()])
			    test_writer.writerow([self.Q5Entry.get(), self.Q5aEntry.get(), self.Q5bEntry.get(), self.Q5cEntry.get(), self.Q5dEntry.get()])
			    test_writer.writerow([self.Q6Entry.get(), self.Q6aEntry.get(), self.Q6bEntry.get(), self.Q6cEntry.get(), self.Q6dEntry.get()])
			    test_writer.writerow([self.Q7Entry.get(), self.Q7aEntry.get(), self.Q7bEntry.get(), self.Q7cEntry.get(), self.Q7dEntry.get()])
			    test_writer.writerow([self.Q8Entry.get(), self.Q8aEntry.get(), self.Q8bEntry.get(), self.Q8cEntry.get(), self.Q8dEntry.get()])
			    test_writer.writerow([self.Q9Entry.get(), self.Q9aEntry.get(), self.Q9bEntry.get(), self.Q9cEntry.get(), self.Q9dEntry.get()])
			    test_writer.writerow([self.Q10Entry.get(), self.Q10aEntry.get(), self.Q10bEntry.get(), self.Q10cEntry.get(), self.Q10dEntry.get()])

			    test_writer.writerow([self.varQ1.get(), self.varQ2.get(), self.varQ3.get(),self.varQ4.get(),self.varQ5.get(),self.varQ6.get(),self.varQ7.get(), self.varQ8.get(), self.varQ9.get(), self.varQ10.get()])
			    test_writer.writerow([testTitle])
			    test_writer.writerow([self.testType.get()])
			    test_writer.writerow([intDay,intMonth, intYear])

			f.close()

			with open(testTitle +'Attempts.csv', mode='w', newline="") as f:

			f.close()

		else:
			tkMessageBox.showwarning("Entry Error", strMsg)

	def goBack(self):
		pass

	def createEntries(self):

		lblTitle = Label(self, text = 'Assessment Title:', font=('MS', 8,'bold'))
		lblTitle.grid(row=0, column=4, columnspan=3, sticky=W)
		self.TitleEntry = Entry(self)
		self.TitleEntry.grid(row=0,column=5,columnspan=4, padx=5, pady=25)


		lblQ1 = Label(self, text = 'Q1.', font=('MS', 8,'bold'))
		lblQ1.grid(row=1, column= 1)
		self.Q1Entry = Entry(self)
		self.Q1Entry.grid(row=1,column=2,columnspan=3)

		lblQ2 = Label(self, text = 'Q2.', font=('MS', 8,'bold'))
		lblQ2.grid(row=6, column= 1)
		self.Q2Entry = Entry(self)
		self.Q2Entry.grid(row=6,column=2,columnspan=3)

		lblQ3 = Label(self, text = 'Q3.', font=('MS', 8,'bold'))
		lblQ3.grid(row=11, column= 1)
		self.Q3Entry = Entry(self)
		self.Q3Entry.grid(row=11,column=2,columnspan=3)

		lblQ4 = Label(self, text = 'Q4.', font=('MS', 8,'bold'))
		lblQ4.grid(row=16, column= 1)
		self.Q4Entry = Entry(self)
		self.Q4Entry.grid(row=16,column=2,columnspan=3)

		lblQ5 = Label(self, text = 'Q5.', font=('MS', 8,'bold'))
		lblQ5.grid(row=1, column= 5)
		self.Q5Entry = Entry(self)
		self.Q5Entry.grid(row=1,column=6,columnspan=3)

		lblQ6 = Label(self, text = 'Q6.', font=('MS', 8,'bold'))
		lblQ6.grid(row=6, column= 5)
		self.Q6Entry = Entry(self)
		self.Q6Entry.grid(row=6,column=6,columnspan=3)

		lblQ7 = Label(self, text = 'Q7.', font=('MS', 8,'bold'))
		lblQ7.grid(row=11, column= 5)
		self.Q7Entry = Entry(self)
		self.Q7Entry.grid(row=11,column=6,columnspan=3)

		lblQ8 = Label(self, text = 'Q8.', font=('MS', 8,'bold'))
		lblQ8.grid(row=16, column= 5)
		self.Q8Entry = Entry(self)
		self.Q8Entry.grid(row=16,column=6,columnspan=3)
	
		lblQ9 = Label(self, text = 'Q9.', font=('MS', 8,'bold'))
		lblQ9.grid(row=1, column= 9)
		self.Q9Entry = Entry(self)
		self.Q9Entry.grid(row=1,column=10,columnspan=3)

		lblQ10 = Label(self, text = 'Q10.', font=('MS', 8,'bold'))
		lblQ10.grid(row=6, column= 9)
		self.Q10Entry = Entry(self)
		self.Q10Entry.grid(row=6,column=10 ,columnspan=3)

		##############################################################

		lblQ1a = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblQ1a.grid(row=2, column= 3)
		self.Q1aEntry = Entry(self)
		self.Q1aEntry.grid(row=2,column=4, padx=5, pady=5)

		lblQ1b = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblQ1b.grid(row=3, column= 3)
		self.Q1bEntry = Entry(self)
		self.Q1bEntry.grid(row=3,column=4, padx=5, pady=5)		
		
		lblQ1c = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblQ1c.grid(row=4, column= 3)
		self.Q1cEntry = Entry(self)
		self.Q1cEntry.grid(row=4,column=4, padx=5, pady=5)		

		lblQ1d = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblQ1d.grid(row=5, column= 3)
		self.Q1dEntry = Entry(self)
		self.Q1dEntry.grid(row=5,column=4, padx=5, pady=5)


		lblQ2a = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblQ2a.grid(row=7, column= 3)
		self.Q2aEntry = Entry(self)
		self.Q2aEntry.grid(row=7,column=4, padx=5, pady=5)

		lblQ2b = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblQ2b.grid(row=8, column= 3)
		self.Q2bEntry = Entry(self)
		self.Q2bEntry.grid(row=8,column=4, padx=5, pady=5)		
		
		lblQ2c = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblQ2c.grid(row=9, column= 3)
		self.Q2cEntry = Entry(self)
		self.Q2cEntry.grid(row=9,column=4, padx=5, pady=5)		

		lblQ2d = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblQ2d.grid(row=10, column= 3)
		self.Q2dEntry = Entry(self)
		self.Q2dEntry.grid(row=10,column=4, padx=5, pady=5)


		lblQ3a = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblQ3a.grid(row=12, column= 3)
		self.Q3aEntry = Entry(self)
		self.Q3aEntry.grid(row=12,column=4, padx=5, pady=5)

		lblQ3b = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblQ3b.grid(row=13, column= 3)
		self.Q3bEntry = Entry(self)
		self.Q3bEntry.grid(row=13,column=4, padx=5, pady=5)		
		
		lblQ3c = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblQ3c.grid(row=14, column= 3)
		self.Q3cEntry = Entry(self)
		self.Q3cEntry.grid(row=14,column=4, padx=5, pady=5)		

		lblQ3d = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblQ3d.grid(row=15, column= 3)
		self.Q3dEntry = Entry(self)
		self.Q3dEntry.grid(row=15,column=4, padx=5, pady=5)


		lblQ4a = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblQ4a.grid(row=17, column= 3)
		self.Q4aEntry = Entry(self)
		self.Q4aEntry.grid(row=17,column=4, padx=5, pady=5)

		lblQ4b = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblQ4b.grid(row=18, column= 3)
		self.Q4bEntry = Entry(self)
		self.Q4bEntry.grid(row=18,column=4, padx=5, pady=5)		
		
		lblQ4c = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblQ4c.grid(row=19, column= 3)
		self.Q4cEntry = Entry(self)
		self.Q4cEntry.grid(row=19,column=4, padx=5, pady=5)		

		lblQ4d = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblQ4d.grid(row=20, column= 3)
		self.Q4dEntry = Entry(self)
		self.Q4dEntry.grid(row=20,column=4, padx=5, pady=5)


		lblQ5a = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblQ5a.grid(row=2, column= 7)
		self.Q5aEntry = Entry(self)
		self.Q5aEntry.grid(row=2,column=8, padx=5, pady=5)

		lblQ5b = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblQ5b.grid(row=3, column=7)
		self.Q5bEntry = Entry(self)
		self.Q5bEntry.grid(row=3,column=8, padx=5, pady=5)		
		
		lblQ5c = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblQ5c.grid(row=4, column=7)
		self.Q5cEntry = Entry(self)
		self.Q5cEntry.grid(row=4,column=8, padx=5, pady=5)		

		lblQ5d = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblQ5d.grid(row=5, column=7)
		self.Q5dEntry = Entry(self)
		self.Q5dEntry.grid(row=5,column=8, padx=5, pady=5)

		lblQ6a = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblQ6a.grid(row=7, column= 7)
		self.Q6aEntry = Entry(self)
		self.Q6aEntry.grid(row=7,column=8, padx=5, pady=5)

		lblQ6b = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblQ6b.grid(row=8, column= 7)
		self.Q6bEntry = Entry(self)
		self.Q6bEntry.grid(row=8,column=8, padx=5, pady=5)		
		
		lblQ6c = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblQ6c.grid(row=9, column= 7)
		self.Q6cEntry = Entry(self)
		self.Q6cEntry.grid(row=9,column=8, padx=5, pady=5)		

		lblQ6d = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblQ6d.grid(row=10, column= 7)
		self.Q6dEntry = Entry(self)
		self.Q6dEntry.grid(row=10,column=8, padx=5, pady=5)

		lblQ7a = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblQ7a.grid(row=12, column= 7)
		self.Q7aEntry = Entry(self)
		self.Q7aEntry.grid(row=12,column=8, padx=5, pady=5)

		lblQ7b = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblQ7b.grid(row=13, column= 7)
		self.Q7bEntry = Entry(self)
		self.Q7bEntry.grid(row=13,column=8, padx=5, pady=5)		
		
		lblQ7c = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblQ7c.grid(row=14, column= 7)
		self.Q7cEntry = Entry(self)
		self.Q7cEntry.grid(row=14,column=8, padx=5, pady=5)		

		lblQ7d = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblQ7d.grid(row=15, column= 7)
		self.Q7dEntry = Entry(self)
		self.Q7dEntry.grid(row=15,column=8, padx=5, pady=5)


		lblQ8a = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblQ8a.grid(row=17, column= 7)
		self.Q8aEntry = Entry(self)
		self.Q8aEntry.grid(row=17,column=8, padx=5, pady=5)

		lblQ8b = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblQ8b.grid(row=18, column= 7)
		self.Q8bEntry = Entry(self)
		self.Q8bEntry.grid(row=18,column=8, padx=5, pady=5)		
		
		lblQ8c = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblQ8c.grid(row=19, column= 7)
		self.Q8cEntry = Entry(self)
		self.Q8cEntry.grid(row=19,column=8, padx=5, pady=5)		

		lblQ8d = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblQ8d.grid(row=20, column= 7)
		self.Q8dEntry = Entry(self)
		self.Q8dEntry.grid(row=20,column=8, padx=5, pady=5)


		lblQ9a = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblQ9a.grid(row=2, column= 10)
		self.Q9aEntry = Entry(self)
		self.Q9aEntry.grid(row=2,column=11, padx=5, pady=5)

		lblQ9b = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblQ9b.grid(row=3, column= 10)
		self.Q9bEntry = Entry(self)
		self.Q9bEntry.grid(row=3,column=11, padx=5, pady=5)		
		
		lblQ9c = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblQ9c.grid(row=4, column= 10)
		self.Q9cEntry = Entry(self)
		self.Q9cEntry.grid(row=4,column=11, padx=5, pady=5)		

		lblQ9d = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblQ9d.grid(row=5, column= 10)
		self.Q9dEntry = Entry(self)
		self.Q9dEntry.grid(row=5,column=11, padx=5, pady=5)


		lblQ10a = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblQ10a.grid(row=7, column= 10)
		self.Q10aEntry = Entry(self)
		self.Q10aEntry.grid(row=7,column=11, padx=5, pady=5)

		lblQ10b = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblQ10b.grid(row=8, column= 10)
		self.Q10bEntry = Entry(self)
		self.Q10bEntry.grid(row=8,column=11, padx=5, pady=5)		
		
		lblQ10c = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblQ10c.grid(row=9, column= 10)
		self.Q10cEntry = Entry(self)
		self.Q10cEntry.grid(row=9,column=11, padx=5, pady=5)		

		lblQ10d = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblQ10d.grid(row=10, column= 10)
		self.Q10dEntry = Entry(self)
		self.Q10dEntry.grid(row=10,column=11)

	def createTestSelect(self):
		lblTestSelect = Label(self, text='Select Test:', font=('MS', 8,'bold'))
		lblTestSelect.grid(row=0, column=9, columnspan=2)

		self.listTest = Listbox(self, height=2)
		self.listTest.grid(row=0, column=11, columnspan=3)

		for item in ["Summative", "Formative"]: 
			self.listTest.insert(END, item)

		self.listTest.selection_set(0)

	def createRadioButtons(self):
		lblCorrect = Label(self, text = 'Correct Answers:', font=('MS', 8,'bold'))
		lblCorrect.grid(row=11, column= 10, columnspan=3, sticky=W)

		lblA = Label(self, text = 'a)', font=('MS', 8,'bold'))
		lblA.grid(row=11, column= 12)
		
		lblB = Label(self, text = 'b)', font=('MS', 8,'bold'))
		lblB.grid(row=11, column= 13)
		
		lblC = Label(self, text = 'c)', font=('MS', 8,'bold'))
		lblC.grid(row=11, column= 14)
		
		lblD = Label(self, text = 'd)', font=('MS', 8,'bold'))
		lblD.grid(row=11, column= 15)

		lblCorrectQ1 = Label(self, text = 'Q1', font=('MS', 8,'bold'))
		lblCorrectQ1.grid(row=12, column= 11)

		lblCorrectQ2 = Label(self, text = 'Q2', font=('MS', 8,'bold'))
		lblCorrectQ2.grid(row=13, column= 11)

		lblCorrectQ3 = Label(self, text = 'Q3', font=('MS', 8,'bold'))
		lblCorrectQ3.grid(row=14, column= 11)

		lblCorrectQ4 = Label(self, text = 'Q4', font=('MS', 8,'bold'))
		lblCorrectQ4.grid(row=15, column= 11)

		lblCorrectQ5 = Label(self, text = 'Q5', font=('MS', 8,'bold'))
		lblCorrectQ5.grid(row=16, column= 11)

		lblCorrectQ6 = Label(self, text = 'Q6', font=('MS', 8,'bold'))
		lblCorrectQ6.grid(row=17, column= 11)

		lblCorrectQ7 = Label(self, text = 'Q7', font=('MS', 8,'bold'))
		lblCorrectQ7.grid(row=18, column= 11)

		lblCorrectQ8 = Label(self, text = 'Q8', font=('MS', 8,'bold'))
		lblCorrectQ8.grid(row=19, column= 11)

		lblCorrectQ9 = Label(self, text = 'Q9', font=('MS', 8,'bold'))
		lblCorrectQ9.grid(row=20, column= 11)

		lblCorrectQ10 = Label(self, text = 'Q10', font=('MS', 8,'bold'))
		lblCorrectQ10.grid(row=21, column= 11)

		self.varQ1 = IntVar()
		R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
		R1Q1.grid(row=12, column= 12)
		R2Q1 = Radiobutton(self, variable= self.varQ1, value=3)
		R2Q1.grid(row=12, column= 13)
		R3Q1 = Radiobutton(self, variable= self.varQ1, value=2)
		R3Q1.grid(row=12, column= 14)
		R4Q1 = Radiobutton(self, variable= self.varQ1, value=1)
		R4Q1.grid(row=12, column= 15)

		self.varQ2 = IntVar()
		R1Q2 = Radiobutton(self, variable=self.varQ2, value=4)
		R1Q2.grid(row=13, column= 12)
		R2Q2 = Radiobutton(self, variable= self.varQ2, value=3)
		R2Q2.grid(row=13, column= 13)
		R3Q2 = Radiobutton(self, variable= self.varQ2, value=2)
		R3Q2.grid(row=13, column= 14)
		R4Q2 = Radiobutton(self, variable= self.varQ2, value=1)
		R4Q2.grid(row=13, column= 15)

		self.varQ3 = IntVar()
		R1Q3 = Radiobutton(self, variable=self.varQ3, value=4)
		R1Q3.grid(row=14, column= 12)
		R2Q3 = Radiobutton(self, variable= self.varQ3, value=3)
		R2Q3.grid(row=14, column= 13)
		R3Q3 = Radiobutton(self, variable= self.varQ3, value=2)
		R3Q3.grid(row=14, column= 14)
		R4Q3 = Radiobutton(self, variable= self.varQ3, value=1)
		R4Q3.grid(row=14, column= 15)


		self.varQ4 = IntVar()
		R1Q4 = Radiobutton(self, variable=self.varQ4, value=4)
		R1Q4.grid(row=15, column= 12)
		R2Q4 = Radiobutton(self, variable= self.varQ4, value=3)
		R2Q4.grid(row=15, column= 13)
		R3Q4 = Radiobutton(self, variable= self.varQ4, value=2)
		R3Q4.grid(row=15, column= 14)
		R4Q4 = Radiobutton(self, variable= self.varQ4, value=1)
		R4Q4.grid(row=15, column= 15)

		self.varQ5 = IntVar()
		R1Q5 = Radiobutton(self, variable=self.varQ5, value=4)
		R1Q5.grid(row=16, column= 12)
		R2Q5 = Radiobutton(self, variable= self.varQ5, value=3)
		R2Q5.grid(row=16, column= 13)
		R3Q5 = Radiobutton(self, variable= self.varQ5, value=2)
		R3Q5.grid(row=16, column= 14)
		R4Q5 = Radiobutton(self, variable= self.varQ5, value=1)
		R4Q5.grid(row=16, column= 15)

		self.varQ6 = IntVar()
		R1Q6 = Radiobutton(self, variable=self.varQ6, value=4)
		R1Q6.grid(row=17, column= 12)
		R2Q6 = Radiobutton(self, variable= self.varQ6, value=3)
		R2Q6.grid(row=17, column= 13)
		R3Q6 = Radiobutton(self, variable= self.varQ6, value=2)
		R3Q6.grid(row=17, column= 14)
		R4Q6 = Radiobutton(self, variable= self.varQ6, value=1)
		R4Q6.grid(row=17, column= 15)

		self.varQ7 = IntVar()
		R1Q7 = Radiobutton(self, variable=self.varQ7, value=4)
		R1Q7.grid(row=18, column= 12)
		R2Q7 = Radiobutton(self, variable= self.varQ7, value=3)
		R2Q7.grid(row=18, column= 13)
		R3Q7 = Radiobutton(self, variable= self.varQ7, value=2)
		R3Q7.grid(row=18, column= 14)
		R4Q7 = Radiobutton(self, variable= self.varQ7, value=1)
		R4Q7.grid(row=18, column= 15)

		self.varQ8 = IntVar()
		R1Q8 = Radiobutton(self, variable=self.varQ8, value=4)
		R1Q8.grid(row=19, column= 12)
		R2Q8 = Radiobutton(self, variable= self.varQ8, value=3)
		R2Q8.grid(row=19, column= 13)
		R3Q8 = Radiobutton(self, variable= self.varQ8, value=2)
		R3Q8.grid(row=19, column= 14)
		R4Q8 = Radiobutton(self, variable= self.varQ8, value=1)
		R4Q8.grid(row=19, column= 15)

		self.varQ9 = IntVar()
		R1Q9 = Radiobutton(self, variable=self.varQ9, value=4)
		R1Q9.grid(row=20, column= 12)
		R2Q9 = Radiobutton(self, variable= self.varQ9, value=3)
		R2Q9.grid(row=20, column= 13)
		R3Q9 = Radiobutton(self, variable= self.varQ9, value=2)
		R3Q9.grid(row=20, column= 14)
		R4Q9 = Radiobutton(self, variable= self.varQ9, value=1)
		R4Q9.grid(row=20, column= 15)

		self.varQ10 = IntVar()
		R1Q10 = Radiobutton(self, variable=self.varQ10, value=4)
		R1Q10.grid(row=21, column= 12)
		R2Q10 = Radiobutton(self, variable= self.varQ10, value=3)
		R2Q10.grid(row=21, column= 13)
		R3Q10 = Radiobutton(self, variable= self.varQ10, value=2)
		R3Q10.grid(row=21, column= 14)
		R4Q10 = Radiobutton(self, variable= self.varQ10, value=1)
		R4Q10.grid(row=21, column= 15)

	def createButtons(self):
		butSave = Button(self, text='Save',font=('MS', 8,'bold'))
		butSave['command']=self.saveTest #Note: no () after the method
		butSave.grid(row=0, column=16, padx=5)

		butCancel = Button(self, text='Cancel',font=('MS', 8,'bold'))
		butCancel['command']=self.goBack #Note: no () after the method
		butCancel.grid(row=0, column=17, columnspan=2)

	def createDueDate(self):
		lblDate = Label(self, text = "Due Date:", font=('MS', 8,'bold'))
		lblDate.grid(row = 2, column = 13, pady = 5)

		lblDay = Label(self, text = "Day:", font=('MS', 8,'bold'))
		lblDay.grid(row = 3, column = 13, pady = 5)
		self.entDay = Entry(self, width=5)
		self.entDay.grid(row=3,column=14,columnspan=4, padx=5)

		lblMonth = Label(self, text = "Month:", font=('MS', 8,'bold'))
		lblMonth.grid(row = 4, column = 13, pady = 5)	
		self.entMonth = Entry(self, width=5)
		self.entMonth.grid(row=4,column=14,columnspan=4, padx=5)

		lblYear = Label(self, text = "Year:", font=('MS', 8,'bold'))
		lblYear.grid(row = 5, column = 13, pady = 5)	
		self.entYear = Entry(self, width=5)
		self.entYear.grid(row=5,column=14,columnspan=4, padx=5)


	def __init__(self, master):
		# Initialise Lecturer Class
		Frame.__init__(self, master)
		self.grid()
		self.createEntries()
		self.createTestSelect()
		self.createRadioButtons()
		self.createButtons()
		self.createDueDate()

root = Tk()
root.title("Create Exam")
root.resizable(0,0)
root.geometry("800x670") 
app = createTest(root)
root.mainloop()