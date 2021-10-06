from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile, asksaveasfile
from typing import Collection
import ruamel.yaml
import json
root =Tk()
root.geometry('500x300')

#Field name
selectfile=Label(root,text="Select file")
savefile=Label(root,text="Save file")

#pacling fileds
selectfile.grid(row=1,column=2,padx=5,pady=10)
savefile.grid(row=2,column=2,padx=5,pady=10)

#variables for storing data
selectfilevalue=StringVar
savefilevalue=StringVar

# creating entry filed
selectfileentry=Entry(root,textvariable=selectfilevalue)
savefileentry=Entry(root,textvariable=savefilevalue)

#packinf entry fields
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
    popupwindow.title("sucess")
    popupwindow.geometry("200x50")
    Label(popupwindow,text="parsing successful").grid(row=0,column=0)
    popupwindow.mainloop()
    

def clear():
    selectfileentry.delete(0,END)
    savefileentry.delete(0,END)

Button(text="Parse",command=lambda:[convert(),popup()]).grid(row=3,column=3,padx=5,pady=10)

Button(text="Browse",command=open_file).grid(row=1,column=4,pady=10,padx=5)

Button(text="Browse",command=save_file_dir).grid(row=2,column=4,padx=5,pady=10)

Button(text="cancle",command=root.destroy).grid(row=3,column=5,padx=5,pady=10)

Button(text="Clear",command=clear).grid(row=3,column=4,padx=5,pady=10)

root.title("YAML to JSON converter")
root.mainloop()
