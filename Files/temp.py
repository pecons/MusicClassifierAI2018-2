import tkinter as tk
from tkinter import messagebox
window = tk.Tk()

#Propiedades de la Ventana
  
window.title("UIS Music Gender Classifier")
window.geometry('400x400')
window.maxsize(width=400,height=400)
frame1 = tk.Frame(window, bg='yellow green')
frame1.pack(fill='both', expand='yes')
#-------------------------#

#Widgets

lbl0 = tk.Label(frame1, text="Bienvenidos",
                bg='yellow green',
                fg='white',
                font=("Arial Bold",40))
lbl0.place(x=60,y=100)

#lbl1 = tk.Label(frame1, text="Hecho por : -Henry Iván Peña Contreras 2150606\n \t -Diego Fernando Medina Blanco 2150606\n \t  -William Giovanny Palomino 2150606",
#                bg='yellow green',
#                fg='snow4',
#                font=("Verdana",8))
#lbl1.place(x=40,y=550)
def create_new_window():
    window.destroy()
    window1 = tk.Tk()
    window1.title("Identificar Género de Canción")
    window1.geometry('800x600')
    window1.maxsize(width=800,height=600)
    frame2 = tk.Frame(window1, bg='yellow green')
    frame2.pack(fill='both', expand='yes')

btn0 = tk.Button(frame1, text="Identificar Género Canción",
                 bg='pale goldenrod',
                 fg='dim gray',
                 font=("Verdana",10),
                 command=create_new_window)
btn0.place(x=100,y=300)

def click_credits():       
    tk.messagebox.showinfo("Créditos","Hecho por : -Henry Iván Peña Contreras 2150606\n \t -Diego Fernando Medina Blanco 2150606\n \t  -William Giovanny Palomino 2150606 \n\n Universidad Industrial de Santander\n\t\t 2019")
    
    
btn1 = tk.Button(frame1, text="Créditos",
                 bg='pale goldenrod',
                 fg='dim gray',
                 font=("Verdana",10),
                 command=click_credits)
btn1.place(x=160,y=350)


window.mainloop()
