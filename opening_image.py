from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image

r = Tk()
r.title("opening Image")


def open_img():
    global img
    r.filename = filedialog.askopenfilename(initialdir=r"C:\Users", title="Select", filetype=(("jpg files", "*.jpg"), ("all files", "*.*")))
    Label(r, text=r.filename).pack()
    img = ImageTk.PhotoImage(Image.open(r.filename))
    Label(image=img).pack()


Button(r, text="open file", command=open_img).pack()

r.mainloop()
