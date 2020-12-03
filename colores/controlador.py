from tkinter import*
import numpy as np

class colores:
    def __init__(self,ven):
        self.ventana=ven
        self.ventana.title("colores")
        self.ventana.geometry("50x100")
        #definir color
        self.rojo=Button(ven,text='rojo',command=self.red)
        self.rojo.pack()
        self.rojo.place(x=20,y=0)

        self.azul = Button(ven, text='azul', command=self.blue)
        self.azul.pack()
        self.azul.place(x=70,y=0)

        self.verde = Button(ven, text='verde', command=self.green)
        self.verde.pack()
        self.verde.place(x=20,y=50)

        self.ama = Button(ven, text='amarillo', command=self.yellow)
        self.ama.pack()
        self.ama.place(x=70,y=50)



    def red(self):
        from color import camera
        self.ventana.config(bg="red")
        return camera([50,50,255],[10,10,60],"rojo")
    def blue(self):
        from color import camera
        self.ventana.config(bg="blue")
        return camera([255,50,50],[60,10,10],"azul")
    def green(self):
        from color import camera
        self.ventana.config(bg="green")
        return camera([50,255,50],[10,60,10],"verde")
    def yellow(self):
        from color import camera
        self.ventana.config(bg="yellow")
        return camera([50,255,255],[10,60,60], "amarillo")






#iniciador
init=Tk()
x =colores(init)
init.mainloop()