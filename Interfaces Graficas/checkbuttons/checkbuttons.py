from tkinter import*

root=Tk()

root.title('Ejemplo')

#creamos las varibales para c/u de los checkbuttons
playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

#Ahora creamos la función para evaluar el si el check correspondiente esta seleccionado o no
def opcionesViaje():
    opcionEscogida=''  #Esta varibale va alamacenar el texto que aparecera al final de la GUI----> Has escogido 'montana', 'playa etc'
    if playa.get()==1:
        opcionEscogida+=' Playa'

    if montana.get()==1:
        opcionEscogida+=' Montana'

    if turismoRural.get()==1:
        opcionEscogida+=' turismoRural'
    
    #El texto al final del programa debe almacenar lo que contenga esa variable y se incrementara de acuerdo a lo que el usuario haya seleccionado---->montana, playa etc
    textoFinal.config(text=opcionEscogida)



#foto=PhotoImage(file="avion.png")
#Label(root, image=foto).pack()

#Creamos un frame para que los checkbuttons pertenezcan a esta y la label sea aparte
frame = Frame(root)
frame.pack()

Label(frame, text='Elige destinos', width=50).pack()

#Clase 'Checkbutoon'
Checkbutton(frame, text='Playa',variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text='Montaña',variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text='Turismo rural',variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()



root.mainloop()

#min 10























#CHECKBUTTONS

#Botones de selección para preguntas de respuesta múltiple
