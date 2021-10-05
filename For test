from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import ruamel.yaml   
import json


r=Tk()
r.geometry('700x500')

def open_file():
    global filepath
    filepath=filedialog.askopenfilename( title="Select a YAML file", filetypes=[("Yaml File","*.yaml"),("","*.yml")])

def save_file_dir():
    global savepath
    savepath= filedialog.asksaveasfilename(title="Select the directory to save JSON file")

def convert():
    in_file = filepath
    out_file = savepath
    yaml = ruamel.yaml.YAML(typ='safe')
    with open(in_file ) as i:  
        data = yaml.load(i)
    with open(out_file, 'w') as o:
        json.dump(data, o, indent=2)



btn= Button( text='Open', command = open_file)
btn.pack(side= BOTTOM)

btn2= Button( text='Save to', command= save_file_dir)
btn2.pack(side= TOP)

btn3= Button( text='Click to convert', command= convert)
btn3.pack(side= RIGHT)

btn4= Button(text="Cancel",  command=r.destroy)
btn4.place(x=0, y=1)

r.title("YAML to JSON converter")
r.mainloop()
