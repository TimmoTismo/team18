from tkinter import *
import tkinter.messagebox #imports

currentuser=open("CurrentUser.txt","r")
User=str(currentuser.readlines())

if User in open('takentest.txt').read(): #if the current user is in the file that is appended when user takes test
    tkinter.messagebox.showinfo("Final Result","Already Taken Test") # a message will be displayed saying test already taken , and not load any questions
                                                                    # this means you can only take the summative once
else:



        
        
    class Summative(Frame):
        def __init__(self, master):
            import tkinter.messagebox #imports
            import csv
            Answers=[]
            question = []
            options = [[], [], [], [], [], [], [], [], [], []] #empty lists
            saved_answers = ["","","","","","","","","",""]

            with open('summative.csv', 'r') as csv_file:
                _data = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in _data:
                    if line_count < 10:
                        question.append(row[0])
                        options[line_count].append(row[1])
                        options[line_count].append(row[2])
                        options[line_count].append(row[3])
                        options[line_count].append(row[4])
                        line_count += 1
                    elif line_count == 10:
                        for dts in row:
                            Answers.append(int(dts)) #reads from csv
                        line_count += 1

            self.questionNo = 0
            self.selected = IntVar()
            self.tkinter=tkinter
            self.options=options
            self.question=question
            self.right = 0
            self.questions = self.PrintQuestion(master, self.questionNo,self.question) 
            self.option = self.radios(master,4)
            button = Button(master, text="Save Answer", command=self.Check) #runs save answer function
            button.pack(side=BOTTOM)        
            button = Button(master, text="Previous Question", command=self.Previous) #back question
            button.pack(side=LEFT)
            button = Button(master, text="Next Question", command=self.Next) #goes to next question
            button.pack(side=RIGHT)
            self.ShowQuestion(self.questionNo,self.question,self.options)
            self.instantresult= Label(master, text='')
            self.instantresult.pack(side=BOTTOM, fill =X)

        def PrintQuestion(self, master, questionNo,question):
            Question = Label(master, text=question[questionNo])
            Question.pack(side=TOP) #loads relevant question
            return Question


        def radios(self, master, n):
            answer = 0
            buttons = []
            while answer < n:
                Buttonn = Radiobutton(master, text="Please choose the right answer", variable=self.selected, value=answer + 1)
                buttons.append(Buttonn)
                Buttonn.pack(side=TOP, anchor="w")
                answer = answer + 1
            return buttons #prints out all the potential radio buttons


        def ShowQuestion(self, questionNo,question,options):
            answer = 0
            self.selected.set(0)
            self.questions['text'] = question[questionNo]
            for op in options[questionNo]:
                self.option[answer]['text'] = op
                answer = answer + 1


        def answer(self, questionNo):
            if self.selected.get() == Answers[questionNo]: #sets true or false depending if the answer correct or not
                return True
            return False

        def Previous(self):
            if self.questionNo > 0:
                self.instantresult['text'] = ""
                self.questionNo = self.questionNo - 1;
                self.ShowQuestion(self.questionNo,self.question,self.options) #goes to last question by taking one off the current question number
               

        def Next(self):
            if self.questionNo > 8:
                self.FinalResult(self.question,self.tkinter)
            elif self.questionNo < 9:
                self.instantresult['text'] = ""
                self.questionNo = self.questionNo + 1;
                self.ShowQuestion(self.questionNo,self.question,self.options) #next question button that adds one to the question number
            
                
            
        def Check(self):
            if self.answer(self.questionNo):
                self.instantresult['text'] = "Answer saved"
                self.right += 1
            else:
                self.instantresult['text'] = "Answer saved"
            saved_answers[self.questionNo] = (self.selected.get()) #Saved students answers to an empty list
        #print(saved_answers)
                #saving answer function, if more time this would have saved to a csv file each answer against the user and then this would be used for the statisitcs 
                #and feedback.
            
            
            


        def FinalResult(self,question,tkinter):

            score = "Score: " + str(self.right) + " out of  " + str(len(question))
            tkinter.messagebox.showinfo("Final Result", score)#shows the user the score they achieved.
            currentuser=open("CurrentUser.txt","r")
            User=str(currentuser.readlines())#tracks the current user in session
            studentfile=open("takentest.txt","a") #writes that the current user has taken the test to the file.
            studentfile.write("\n"+User)#this would have been used to make sure the user only had one attempt if more time
            exec(open(r"Student.py").read()) #returns to menu
            

     
    root = Tk() #tkinter formatting

    root.resizable(0,0) 
    root.geometry("600x200")
    root.title("Summative Test")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    app = Summative(root)
    root.mainloop()
