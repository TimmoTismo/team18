from tkinter import *
import tkinter.messagebox
import csv 

#change so reads in from a .txt or .csv file,
#instead of being hard coded in????

Answers=[]
question = []
options = [[], [], [], [], [], [], [], [], [], []]

with open('Formative.csv', 'r') as csv_file:
    csvquestions = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csvquestions:
        if line_count < 10:
            question.append(row[0])
            options[line_count].append(row[1])
            options[line_count].append(row[2])
            options[line_count].append(row[3])
            options[line_count].append(row[4])
            line_count += 1
        elif line_count == 10:
            for ans in row:
                Answers.append(int(ans))
                print(Answers)
            line_count += 1

class Formative:
    def __init__(self, master):
        self.questionnumber = 0
        self.selected = IntVar()
        self.right = 0
        self.questions = self.PrintQuestion(master, self.questionnumber) 
         #needs order to print out title, then radios, then buttons and finally result- so dont move
        self.option = self.radios(master,4)
        button = Button(master, text="Exit", command=self.Exit)
        button.pack(side=BOTTOM)#puts at bottom of tkinter window
        button = Button(master, text="Check Answer", command=self.Check)
        button.pack(side=BOTTOM)
        self.ShowQuestion(self.questionnumber)
        self.instantresult= Label(master, text='')
        self.instantresult.pack(side=BOTTOM, fill =X)

    def PrintQuestion(self, master, questionnumber):
        Question = Label(master, text=question[questionnumber])
        Question.pack(side=TOP)
        return Question


    def radios(self, master, n):
        answer = 0
        buttons = []
        while answer < n:
            Buttonn = Radiobutton(master, text="Please choose the right answer", variable=self.selected, value=answer + 1)
            buttons.append(Buttonn)
            Buttonn.pack(side=TOP, anchor="w")
            answer = answer + 1
        return buttons


    def ShowQuestion(self, questionnumber):
        answer = 0
        self.selected.set(0)
        self.questions['text'] = question[questionnumber]
        for op in options[questionnumber]:
            self.option[answer]['text'] = op
            answer = answer + 1


    def answer(self, questionnumber):
        if self.selected.get() == Answers[questionnumber]:
            return True
        return False


    def Exit(self):
        tkinter.messagebox.showinfo("Exit","Formative test attempt exited. Returning to Main Menu")
        root.destroy()
        exec(open(r"Student.py").read()) #return to menu

    def Check(self):
        if self.answer(self.questionnumber):
            self.instantresult['text'] = "You got the correct answer"
            self.right += 1
        else:
            self.instantresult['text'] = "Wrong, go back to the lectures and try again after"
        self.questionnumber = self.questionnumber + 1
        if self.questionnumber >= len(question):
            self.FinalResult()#if end of questions
        else:
            self.ShowQuestion(self.questionnumber)#if another question, then loop


    def FinalResult(self):
        score = "Score: " + str(self.right) + " out of a total of " + str(len(question))
        tkinter.messagebox.showinfo("Final Result", score)
        root.destroy()
        #show correct answers???       
        exec(open(r"Student.py").read())#goes back to menu

root = Tk()
root.title("Java Theory Test")
root.resizable(0,0) 
root.geometry("600x200") 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = Formative(root)
root.mainloop()

