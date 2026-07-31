from tkinter import * 
from tkinter import filedialog as FileDialog
from fun import *
#Creamos la ventana

root = Tk()
root.title("YouTube downloader")
root.geometry("600x300")

root.maxsize(600, 300)
root.minsize(600, 300)


frm1 = Frame(
    root,
    width=150,
    height=214,
    bg="#F9E9F8",
    highlightbackground="#EEB3B3",
    highlightcolor="#EEB3B3",
    highlightthickness=1,
    bd=0
)
frm1.grid(row=0, column=0, padx=30, pady=20)

frm2 = Frame(
    root,
    width="300",
    height="214",
    bg="#F9E9F8",
    highlightbackground="#EEB3B3",
    highlightcolor="#EEB3B3",
    highlightthickness=1,
    bd=0
            )
frm2.grid(column=1, row=0, padx=50, pady=40)


btn1 = Button(frm1, text="Importar", width=15, height=2)
btn1.grid(column=0, row=0, padx=10, pady=10)

btn2 = Button(frm1, text="Descargar", width=15, height=2)
btn2.grid(column=0, row=1, padx=10, pady=10)

btn3 = Button(frm1, text="Salir", width=15, height=2)
btn3.grid(column=0, row=2, padx=10, pady=10)

root.mainloop()