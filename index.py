
from tkinter import Tk, Button



reiz = Tk()
reiz.title("Vehiculos")
reiz.resizable(1, 1)
reiz.iconbitmap('Imagen.jpg')
reiz.geometry("800x600")
reiz.config(bg="cyan")

def hacer_algo():
    print("¡Hiciste clic en el botón!")

boton = Button(reiz, text="Haz clic aquí", command=hacer_algo)
boton.pack()


reiz.mainloop()
