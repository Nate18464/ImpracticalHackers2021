from tkinter import *
from tkinter import ttk
import random
import classClass

def generateRanPassTime():
    day = random.randint(0,4)
    timehour = random.randint(0,12)
    timemin = random.randint(0,1)
    return [day, timehour, timemin]

def strPassTime(passtimelist):
    days = ["Mon ", "Tues ", "Wed ", "Thur ", "Fri "]
    ampm = " AM"
    minutes = "00"
    time = passtimelist[1] + 5
    if time > 11:
        ampm = " PM"
        if time > 12:
            time -= 12
    if passtimelist[2] != 0:
        minutes = "30"
    passtime = days[passtimelist[0]] + str(time) + ":" + minutes + ampm
    return passtime    


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
    introtext["text"] = "Stephanie: That’s the time you can register for classes. It’s completely random. Have you gotten yours yet?"
    introbutton["text"] = "No"
    introbutton["command"] = intro9

def intro9(*args):
    introframe.destroy()
    hubframe.grid()

def tutorialPass(*args):
    ranpasstime = generateRanPassTime()
    passtime = strPassTime(ranpasstime)
    passtimelabel["text"] = passtime
    passtimelabel.grid(column = 0, row = 1, columnspan = 2)
    hubpassbutton.grid_remove()
    hubcatalogbutton["state"] = NORMAL
    hubtutoriallabel["text"] = "Great job! Now, check the course catalog!"

def hub(*args):
    hubframe.grid()

def tutorialCatalog(*args):
    hubframe.grid_remove()
    catalogframe.grid()
    for i in range(len(classClass.Allcourse)):
        catalogCourseLabels.append(ttk.Label(catalogframe, text = classClass.Allcourse[i].retstr()))
        catalogCourseLabels[i].grid(column = int(i/15), row = i%15)
    for child in catalogframe.winfo_children(): child.grid_configure(padx = 5, pady = 5, sticky =(N,W,E,S))
    hubcatalogbutton["command"] = catalog

def hubfromcatalog(*args):
    hubframe.grid()
    catalogframe.grid_remove()
    hubprogresssbutton["state"] = NORMAL
    hubtutoriallabel["text"] = "Amazing, now sign up for classes!"

def tutorialProgress(*args):
    progressframe.grid()
    hubframe.grid_remove()
    progressunitslabel["text"] = "Total Unit Requirement: " + str(units[0]) + "/180 units"
    tb = geunits[0][0] + geunits[0][1] + geunits[0][2]
    progresstblabel["text"] = "Topical Breadth: " + str(tb) + "/52 units"
    for x in range(len(genames[0])):
        gelabels.append(ttk.Label(progressframe, text = genames[0][x]+": " + str(geunits[0][x])+"/12 units (max of 20)"))
        gelabels[x].grid(column = 0, row = 3+x)

    for child in progressframe.winfo_children(): child.grid_configure(padx = 5, pady = 5, sticky =(N,W,E,S))


def hubfromtutprogress(*args):
    hubframe.grid()
    progressframe.grid_remove()
    hubsearchbutton["state"] = NORMAL

def tutorialSearch(*args):
    hubframe.grid_remove()
    searchframe.grid()

def tutorialCheckCourse(*args):
    pass

def tutorialSubmit(*args):
    pass

def catalog(*args):
    hubframe.grid_remove()
    catalogframe.grid()

root = Tk()
root.title("UC Davis Class Simulator")

introframe = ttk.Frame(root, padding="3 3 12 12")
introframe.grid(column = 0, row = 0, sticky =(N,W,E,S))
introframe.grid_remove()
introtext = ttk.Label(introframe, text = "Unknown Person: Welcome to UC Davis!")
introtext.grid(column = 0, row = 0, columnspan = 2)
introbutton = ttk.Button(introframe, text = "Who are you?",command=intro2)
introbutton.grid(column = 0, row = 1)
for child in introframe.winfo_children(): child.grid_configure(padx = 5, pady = 5, sticky =(N,W,E,S))

hubframe = ttk.Frame(root, padding = "3 3 12 12")
hubframe.grid(column = 0, row = 0, sticky = (N,E,W,S))
hubdisplayyearlabel = ttk.Label(hubframe, text = "Year: Freshman")
hubdisplayyearlabel.grid(column = 0, row = 0)
hubdisplayquarterlabel = ttk.Label(hubframe, text = "Quarter: Fall")
hubdisplayquarterlabel.grid(column = 1, row = 0)
hubpassbutton = ttk.Button(hubframe, text = "Check your pass time", command = tutorialPass)
hubpassbutton.grid(column = 0, row = 1, columnspan = 2)
hubcatalogbutton = ttk.Button(hubframe, text = "Search the catalog", command = tutorialCatalog, state = DISABLED)
hubcatalogbutton.grid(column = 0, row = 2, columnspan = 2)
hubprogresssbutton = ttk.Button(hubframe, text = "Check your progress", command = tutorialProgress, state = DISABLED)
hubprogresssbutton.grid(column = 0, row = 3, columnspan = 2)
hubsearchbutton = ttk.Button(hubframe, text = "Search for courses", command = tutorialSearch, state = DISABLED)
hubsearchbutton.grid(column = 0, row = 4, columnspan = 2)
hubcheckcoursebutton = ttk.Button(hubframe, text = "Check what courses you've signed up for", command = tutorialCheckCourse, state = DISABLED)
hubcheckcoursebutton.grid(column = 0, row = 5, columnspan = 2)
hubsubmitbutton = ttk.Button(hubframe, text = "Submit schedule", command = tutorialSubmit, state = DISABLED)
hubsubmitbutton.grid(column = 0, row = 6, columnspan = 2)
hubtutoriallabel = ttk.Label(hubframe, text = "Click to check your pass time!")
hubtutoriallabel.grid(column = 0, row = 7, columnspan = 2)
passtimelabel = ttk.Label(hubframe, text = "")
year = [0]
quarter = [0]
for child in hubframe.winfo_children(): child.grid_configure(padx = 5, pady = 5, sticky =(N,W,S))

catalogframe = ttk.Frame(root, padding="3 3 12 12")
catalogframe.grid(column = 0, row = 0, sticky = (N,W,E,S))
catalogframe.grid_remove()
catalogCourseLabels = []
catalogButton = ttk.Button(catalogframe, text = "Back to hub", command = hubfromcatalog)
catalogButton.grid(row = 16, column = 0) # will change row depending on catalog later
catalogTutorialLabel = ttk.Label(catalogframe, text = "This shows all the courses that go towards your major")
catalogTutorialLabel.grid(row = 17, column = 0, columnspan = 2)

progressframe = ttk.Frame(root, padding="3 3 12 12")
progressframe.grid(column = 0, row = 0, sticky =(N,W,E,S))
progressframe.grid_remove()
progressunitslabel = ttk.Label(progressframe, text = "Units taken: ")
progressunitslabel.grid(column = 0, row = 0)
progressreturnbutton = ttk.Button(progressframe, text = "Return to hub", command = hubfromtutprogress)
progressreturnbutton.grid(column = 1, row = 0)
progressgelabel = ttk.Label(progressframe, text = "GE Requirements:")
progressgelabel.grid(column = 0, row = 1)
progresstblabel = ttk.Label(progressframe, text = "Topical Breadth:")
progresstblabel.grid(column = 0, row = 2)
progresscllabel = ttk.Label(progressframe, text = "Core Literacies:")
progresscllabel.grid(column = 0, row = 6)
progressmajorlabel = ttk.Label(progressframe, text = "Major Requirements:")
progressmajorlabel.grid(column = 2, row = 1)
units = [0]
genames = [["Social Science", "Science and Engineering", "Arts and Humanities"], ["Writing Experience", "Oral Literacy or Writing Experience", "Visual Literacy", 
"Domestic Diversity", "American Cultures, Governance, and History", "World Cultures", "Qualitative Literacy", "Scientific Literacy"]]
geunits = [[0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
gelabels = []

searchframe = ttk.Frame(root, padding="3 3 12 12")
searchframe.grid(column = 0, row = 0, sticky =(N,W,E,S))
searchframe.grid_remove()
chooseGEbutton = ttk.Button(searchframe, text = "Choose GE Classes")
chooseGEbutton.grid(column = 0, row = 0, columnspan = 2)
chooseMajorclassbutton = ttk.Button(searchframe, text = "Choose Major Classes",command=intro2)
chooseMajorclassbutton.grid(column = 0, row = 1)
for child in searchframe.winfo_children(): child.grid_configure(padx = 5, pady = 5, sticky =(N,W,E,S))

root.mainloop()
