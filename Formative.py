from tkinter import *


class Formative(Frame):
    def __init__(self, master): #all tkinter formatting
        import csv 
        import tkinter.messagebox
        Answers=[]
        question = []
        options = [[], [], [], [], [], [], [], [], [], []] #empty lists to be populated from csv

        with open('Formative.csv', 'r') as csv_file: #opens test csv as read
            csvquestions = csv.reader(csv_file, delimiter=',') #seperated by ,
            line_count = 0 #declares as 0
            for row in csvquestions:#for each row
                if line_count < 10:#for line as there are 10
                    question.append(row[0])#question
                    options[line_count].append(row[1])#each option in seperate rows
                    options[line_count].append(row[2])
                    options[line_count].append(row[3])
                    options[line_count].append(row[4])
                    line_count += 1 #line acount appended 
                elif line_count == 10:
                    for ans in row:
                        Answers.append(int(ans))#answer appended to list from final csv row
                    line_count += 1
        self.questionnumber = 0 #delcares as 0
        self.selected = IntVar()
        self.options=options
        tkinter=tkinter
        self.tkinter=tkinter
        self.Answers=Answers
        self.question=question
        self.right = 0
        self.questions = self.PrintQuestion(master, self.questionnumber, self.question) 
         #needs order to print out title, then radios, then buttons and finally result- so dont move
        self.option = self.radios(master,4)
       # button = Button(master, text="Exit", command=self.Exit())#runs exit when quit
      #  button.pack(side=BOTTOM)#puts at bottom of tkinter window
        button = Button(master, text="Check Answer", command=self.Check)#runs check function when quit
        button.pack(side=BOTTOM)
        self.ShowQuestion(self.questionnumber,self.question,self.options)
        self.instantresult= Label(master, text='')#text that says if question correct on the window
        self.instantresult.pack(side=BOTTOM, fill =X)#at bottom

    def PrintQuestion(self, master, questionnumber, question):
        Question = Label(master, text=question[questionnumber])
        Question.pack(side=TOP)
        return Question #current question returned based on question number

    def radios(self, master, n):
        answer = 0
        buttons = []
        while answer < n:
            Buttonn = Radiobutton(master, text="Please choose the answer", variable=self.selected, value=answer + 1)
            buttons.append(Buttonn) #depending what radio button clicked 
            Buttonn.pack(side=TOP, anchor="w")
            answer = answer + 1 
        return buttons

    def ShowQuestion(self, questionnumber, question,options):
        answer = 0
        self.selected.set(0)
        self.questions['text'] = question[questionnumber]
        for op in options[questionnumber]:
            self.option[answer]['text'] = op #used to display question options alongisde radios
            answer = answer + 1

    def answer(self, questionnumber,Answers,question):
        if self.selected.get() == Answers[questionnumber]: #if the selected button is equal to the answer for that question number
            return True
        return False

 #   def Exit(self,tkinter):
  #      tkinter.messagebox.showinfo("Exit","Formative test attempt exited. Returning to Main Menu")
   #     root.destroy() #closes test
       # exec(open(r"Student.py").read()) #return to menu

    def Check(self):
        if self.answer(self.questionnumber,self.Answers,self.question):
            self.instantresult['text'] = "You got the correct answer" #it true shows message and appends to the right
            self.right += 1
        else:
            self.instantresult['text'] = "Wrong, go back to the lectures and try again after" #if false message and no appened
        self.questionnumber = self.questionnumber + 1 #append to question number
        if self.questionnumber >= len(self.question):
            self.FinalResult(self.question,self.tkinter)#if end of questions
        else:
            self.ShowQuestion(self.questionnumber,self.question, self.options)#if another question, then loop


    def FinalResult(self,question,tkinter):
        score = "Score: " + str(self.right) + " out of a total of "+ str(len(question)) +" .To retake the test, login to the system again. Please close the test window" #message with total score - using the right from the Check function and length of all the questions
        tkinter.messagebox.showinfo("Final Result", score) #prints the message created above
        #root.destroy()#closes window
        # GET SO SHOWS CORRECT ANSWER IF CLICK FINAL TRY !!!!!!!!!!!!     
        exec(open(r"Student.py").read())#goes back to menu

root = Tk()
root.title("Formative Test") #title
root.resizable(0,0) #tkinter formatting from now on
root.geometry("600x200") 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = Formative(root)
root.mainloop()

