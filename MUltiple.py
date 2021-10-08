from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile, asksaveasfile
from typing import Collection
from glob import glob
import os
import ruamel.yaml
import json

root =Tk()
root.geometry('500x300')
root.configure(bg = "#b1cee9")

def open_file():
    global filepath
    filepath=filedialog.askdirectory(title="Select a Directory")
    global filelist
    filelist = glob(os.path.join(filepath ,'*.yaml'))

def convert():
    yaml = ruamel.yaml.YAML(typ='safe')
    for files in filelist:
        with open(files) as i:  
            data = yaml.load(i)  
            f= files.replace('.yaml', '')
        with open(f + ".json", 'w') as o:
            json.dump(data, o, indent=2)

ttk.Button(text="Convert",command=convert).grid(row=3,column=3,padx=5,pady=10)

ttk.Button(text="open file",command=open_file).grid(row=1,column=5,pady=10,padx=5)

ttk.Button(text="Cancel",command=root.destroy).grid(row=3,column=5,padx=5,pady=10)

root.title("YAML to JSON converter")
root.mainloop()
