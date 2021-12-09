import tkinter as tk
from tkinter.constants import TRUE

fen = tk.Tk()
fen.title("Pendu")

""" fen.configure(bg="grey") """
fen.geometry("1500x900")

frame1 = tk.Frame(fen,width=750,height=900,bg='red')
frame1.grid(row=0,column=0)


frame2 = tk.Frame(fen,width=750,height=900,bg='blue')
frame2.grid(row=0, column=1)

""" 
value = tk.StringVar() 
entree = tk.Entry(frame2, width=10)
entree.pack()   """

fen.mainloop()