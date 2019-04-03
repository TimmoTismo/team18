from tkinter import * #relevant imports to python
import tkinter.messagebox

class LoginFrame(Frame):
    def __init__(self, master): #tkinter initialisation
        super().__init__(master)
        #would have for loop for each csv file exisiting or been created by the lecturer, create a button for each.
        #each button would load either the Formative.py or Summative.py , then set the file within this to the relevant .csv