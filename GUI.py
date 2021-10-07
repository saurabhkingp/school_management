from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile, asksaveasfile
from typing import Collection
import ruamel.yaml
import json

root =Tk()
root.geometry('500x300')
root.configure(bg = "#b1cee9")
#Field name
selectfile=Label(root,text="Select a YAML file", bg='#b1cee9')
savefile=Label(root,text="Save file to", bg='#b1cee9')

#placing fileds
selectfile.grid(row=1,column=2,padx=5,pady=10)
savefile.grid(row=2,column=2,padx=5,pady=10)

#variables for storing data
selectfilevalue=StringVar
savefilevalue=StringVar

# creating entry filed
selectfileentry=Entry(root,textvariable=selectfilevalue, bd = 0,
    bg = "#e4e4e4",
    highlightthickness = 2)
savefileentry=Entry(root,textvariable=savefilevalue, bd = 0,
    bg = "#e4e4e4",
    highlightthickness = 2)

#packing in entry fields
selectfileentry.grid(row=1,column=3)
savefileentry.grid(row=2,column=3)

def open_file():
    global filepath
    filepath=filedialog.askopenfilename( title="Select a YAML file", filetypes=[("Yaml File","*.yaml"),("","*.yml")])
    selectfileentry.insert(0,filepath)

def save_file_dir():
    global savepath
    savepath= filedialog.asksaveasfilename(title="Select the directory to save JSON file",filetypes=[("json files","*.json"),("","*.json")])
    savefileentry.insert(0,savepath)
def convert():
    in_file = filepath
    out_file = savepath
    yaml = ruamel.yaml.YAML(typ='safe')
    with open(in_file ) as i:  
        data = yaml.load(i)
    with open(out_file, 'w') as o:
        json.dump(data, o, indent=2)

def popup():
    popupwindow=Toplevel(root)
    popupwindow.title("Success")
    popupwindow.geometry("200x50")
    Label(popupwindow,text="Conversion Successful").grid(row=0,column=0)
    popupwindow.mainloop()
    

def clear():
    selectfileentry.delete(0,END)
    savefileentry.delete(0,END)

ttk.Button(text="Convert",command=lambda:[convert(),popup()]).grid(row=3,column=3,padx=5,pady=10)

ttk.Button(text="Browse",command=open_file).grid(row=1,column=5,pady=10,padx=5)

ttk.Button(text="Browse",command=save_file_dir).grid(row=2,column=5,padx=5,pady=10)

ttk.Button(text="Cancel",command=root.destroy).grid(row=3,column=5,padx=5,pady=10)

ttk.Button(text="Clear",command=clear).grid(row=3,column=4,padx=5,pady=10)

root.title("YAML to JSON converter")
root.resizable(False, False)
root.mainloop()
