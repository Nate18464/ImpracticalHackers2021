from tkinter import *
from tkinter import ttk
import random

def generateRanPassTime():
    day = random.randint(0,5)
    timehour = random.randint(0,12)
    timemin = random.randint(0,1)
    return [day, timehour, timemine]

def intro2(*args):
    introtext["text"] = "Unknown Person: Oh sorry, I forgot to introduce myself! I'm your orientation leader, Stephanie"
    introbutton["text"] = "Nice to meet you, Stephanie"
    introbutton["command"] = intro3

def intro3(*args):
    introtext["text"] = "Stephanie: What major are you?"
    introbutton["text"] = "Computer Science"
    introbutton["command"] = intro4

def intro4(*args):
    introtext["text"] = "Stephanie: Oh that's great! Have you made your schedule yet?"
    introbutton["text"] = "No"
    introbutton["command"] = intro5

def intro5(*args):
    introtext["text"] = "Stephanie: Do you know how?"
    introbutton["text"] = "No :("
    introbutton["command"] = intro6
 
def intro6(*args):
    introtext["text"] = "Stephanie: That’s ok! I’ll walk you through it!"
    introbutton["text"] = "Thanks :)"
    introbutton["command"] = intro7
 
def intro7(*args):
    introtext["text"] = "Stephanie: Well first, you need to get your passtime. Do you know what yours is?"
    introbutton["text"] = "No, what’s that?"
    introbutton["command"] = intro8
 
def intro8(*args):
    introtext["text"] = "Stephanie: That’s the time you get to get to register your schedule. It’s completely random. Have you gotten yours yet?"
    introbutton["text"] = "No"
    introbutton["command"] = intro9

def intro9(*args):
    introframe.destroy()
    hubframe.grid()

def tutorialPass(*args):
    hubframe.grid_remove()

def notCheckedPass(*args):
    hubframe.grid_remove()
    notcheckedpassframe.grid()

def hub(*args):
    hubframe.grid()
    notcheckedpassframe.grid_remove()


root = Tk()
root.title("UC Davis Class Simulator")

introframe = ttk.Frame(root, padding="3 3 12 12")
introframe.grid(column = 0, row = 0, sticky =(N,W,E,S))
introtext = ttk.Label(introframe, text = "Unknown Person: Welcome to UC Davis!")
introtext.grid(column = 0, row = 0, columnspan = 2)
introbutton = ttk.Button(introframe, text = "Who are you?",command=intro2)
introbutton.grid(column = 0, row = 1)
for child in introframe.winfo_children(): child.grid_configure(padx = 5, pady = 5, sticky =(N,W,E,S))

hubframe = ttk.Frame(root, padding = "3 3 12 12")
hubframe.grid(column = 0, row = 0, sticky = (N,E,W,S))
hubframe.grid_remove()
hubdisplayyearlabel = ttk.Label(hubframe, text = "Year: Freshman")
hubdisplayquarterlabel = ttk.Label(hubframe, text = "Quarter: Fall")
hubsearchbutton = ttk.Button(hubframe, text = "Search for courses", command = notCheckedPass)
hubsearchbutton.grid(column = 0, row = 1)
hubpassbutton = ttk.Button(hubframe, text = "Check your pass time", command = tutorialPass)
hubpassbutton.grid(column = 0, row = 2)
hubcheckcoursebutton = ttk.Button(hubframe, text = "Check what courses you've signed up for", command = notCheckedPass)
hubcheckcoursebutton.grid(column = 0, row = 3)
hubsubmitbutton = ttk.Button(hubframe, text = "Submit schedule", command = notCheckedPass)
hubsubmitbutton.grid(column = 0, row = 4)
hubtutoriallabel = ttk.Label(hubframe, text = "Click to check your pass time!")
hubtutoriallabel.grid(column = 0, row = 5)
year = [0]
quarter = [0]
for child in hubframe.winfo_children(): child.grid_configure(padx = 5, pady = 5, sticky =(N,W,S))

notcheckedpassframe = ttk.Frame(root, padding = "3 3 12 12")
notcheckedpassframe.grid(row = 0, column = 0, sticky = (N,W,E,S))
notcheckedpassframe.grid_remove()
notcheckedpasslabel = ttk.Label(notcheckedpassframe, text = "You haven't checked your pass time yet")
notcheckedpasslabel.grid(column = 0,row = 0)
notcheckedpassbutton = ttk.Button(notcheckedpassframe, text = "Go back", command = hub)
notcheckedpassbutton.grid(column = 0, row = 1)
for child in notcheckedpassframe.winfo_children(): child.grid_configure(padx = 5, pady = 5, sticky =(N,W,S))

passtimeframe = ttk.Frame(root, padding = "3 3 12 12")
passtimelabel = ttk.Label(passtimeframe, text = "")
passtimelabel.grid(column = 0, row = 0)
passtimebutton = ttk.Button(passtimeframe, text = "Ok", command = hubfrompass)

root.mainloop()