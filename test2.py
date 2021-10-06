import tkinter as Tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile, asksaveasfile
from typing import Collection
import ruamel.yaml
import json


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x700")
window.configure(bg = "#b1cee9")
canvas = Canvas(
    window,
    bg = "#b1cee9",
    height = 700,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    409.5, 190.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e4e4e4",
    highlightthickness = 0)

entry0.place(
    x = 202.5, y = 156,
    width = 414.0,
    height = 67)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    409.5, 330.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e4e4e4",
    highlightthickness = 0)

entry1.place(
    x = 202.5, y = 296,
    width = 414.0,
    height = 67)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    270.0, 202.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 713, y = 126,
    width = 186,
    height = 535)

window.resizable(False, False)
window.mainloop()
