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
    filepath=filedialog.askdirectory( title="Select a Directory")

# open_file()
# files = os.listdir(filepath)
# print(files)
    

files = glob("filepath/*.yaml")
for file in files:
    print(files)
ttk.Button(text="open file",command=open_file).grid(row=1,column=5,pady=10,padx=5)


ttk.Button(text="Cancel",command=root.destroy).grid(row=3,column=5,padx=5,pady=10)

root.title("YAML to JSON converter")
root.resizable(False, False)
root.mainloop()    




D_Lib: debug printing for files [.*] and level [100] is turned on
D_Lib: debug printing for files [.*] and level [200] is turned on
D_Lib: debug printing for files [.*] and level [300] is turned on
13008:.../engine/vf_shex/vf_shex.cpp(91): INFO: DllCanUnloadNow returned S_OK.
