from pathlib import Path
from tkinter import *       
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import webbrowser

#inputX = 150
 
root = Tk()
root.title("Chaos Mod Twitch Settings")
root.resizable(False,False)
root.geometry("800x300")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

def openBrowser():
    webbrowser.open('https://twitchapps.com/tmi/')

frm = ttk.Frame(root, padding = 20)
frm.grid()

frm.columnconfigure(tuple(range(60)), weight=1)
frm.rowconfigure(tuple(range(30)), weight=1)

## text stuff
username = Label(frm,text="Twitch Username").grid(column = 0, row = 0, sticky="nesw")#.place(x = 25,y = 40) 
token = Label(frm,text="Twitch Token").grid(column = 0, row = 1, sticky="nesw")#.place(x = 25,y = 80)
emptyLabel = Label(frm, text="Reminder to keep your token secret!").grid(column = 0, row = 2, sticky="nesw")
ttk.Button(frm, text="Where to find?", command=openBrowser).grid(column = 1, row = 1, sticky="nesw")#.place(x = 30, y = 100)
#Tokenhelp = Label (root,text="(look into tokenhelp.txt for help)").place(x = 30,y = 100) 
PathToMOD = Label(frm,text="Path to the mod").grid(column = 0, row = 3, sticky="nesw")#.place(x = 30,y = 160) 
PathToSAVE = Label(frm,text="Path to the savegame").grid(column = 0, row = 4, sticky="nesw")#.place(x = 30,y = 200) 
## input

PathToFolderLabel = Label(frm, text="")
PathToFolderLabel.grid(column = 1, row = 3, sticky="nesw")
PathToSaveLabel = Label(frm, text="")
PathToSaveLabel.grid(column = 1, row = 4, sticky="nesw")

usernameinput = ttk.Entry(frm)
usernameinput.grid(column = 3, row = 0, sticky="nesw")#.place(x = inputX,y = 40) 
Tokeninput = ttk.Entry(frm)
Tokeninput.grid(column = 3, row = 1, sticky="nesw")#.place(x = inputX,y = 80) 
#PathToModInput = ttk.Entry(frm)
#PathToModInput.grid(column = 3, row = 3)#.place(x = inputX,y = 160) 
#PathToSaveInput = ttk.Entry(frm)
#PathToSaveInput.grid(column = 3, row = 4)#.place(x = inputX,y = 200)

PathToModInput = ""
PathToSaveInput = ""

def openFileDialogForSavegame():
    global PathToSaveLabel
    global PathToSaveInput
    
    PathToSaveInput = filedialog.askopenfilename()
    
    PathToSaveLabel.config(text = PathToSaveInput)

def openFileDialogForModFolder():
    global PathToFolderLabel
    global PathToModInput
    
    PathToModInput = filedialog.askdirectory()
    
    PathToFolderLabel.config(text = PathToModInput)

Button(frm, text="Open Directory Browser", command = openFileDialogForModFolder).grid(column = 3, row = 3, sticky="nesw")
Button(frm, text="Open File Browser", command = openFileDialogForSavegame).grid(column = 3, row = 4, sticky="nesw")

Label(frm,text="Mod folder is used to send twitch votes through an xml.").grid(column = 0, row = 5, sticky="nesw")
Label(frm,text="Savegame is read only to detect a vote reset.").grid(column = 0, row = 6, sticky="nesw")

def MessageBox(title, text):
    return messagebox.showwarning(title, text)

def callback():
    #print(usernameinput.get()) # This is the text you may want to use later
    #print(Tokeninput.get())
    #print(PathToModInput.get())
    #print(PathToSaveInput.get())

    if usernameinput.get() is None or usernameinput.get() == "":
        MessageBox("Warning", "No username entered. No changes made!")
        return

    if Tokeninput.get() is None or Tokeninput.get() == "":
        MessageBox("Warning", "No oauth token entered. No changes made!")
        return

    if not Path(PathToModInput + "/effects.lua").is_file():
        MessageBox("Warning", "Couldn't find the Chaos mod in given directory. No changes made!")
        return

    if not Path(PathToSaveInput).is_file():
        MessageBox("Warning", "Couldn't find the savegame.xml at given path. No changes made!", 1)
        return
        
    with open("twitchchatsettings.txt", 'w') as settings:
        settings.write(f'{usernameinput.get()}\n{Tokeninput.get()}\n{PathToModInput}\n{PathToSaveInput}')
    
b = Button(root, text = "Save to twitchchatsettings.txt", width = 10, command = callback)
b.grid(column = 0, row = 7, sticky="nesw")

root.mainloop()
