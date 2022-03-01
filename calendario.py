from tkinter import *
from tkcalendar import*

root= Tk()
root.title("CALENDARIO")
root.geometry("500x350")
root.config(bg= "gray")


cal = Calendar(root, select= "day", year = 2022, month= 3, day=1)
cal.pack(pady = 20, fill= "both", expand= "yes")

def Fecha():
    Label.config(text= " Fecha de hoy: " +  cal.get_date())

Button = Button(root, text= "Fecha", command= Fecha )
Button.pack(pady=20)

Label = Label(root,text="")
Label.pack(pady=20)







root.mainloop()