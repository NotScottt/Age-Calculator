from tkinter import *
import datetime
from dateutil.relativedelta import relativedelta
from tkinter import messagebox

root = Tk()
root.title("Age Calculator")
root.geometry("300x300")

frame = Frame(root)
frame.pack()


day = Label(frame, text="Tag").grid(row=0)
month = Label(frame, text="Monat").grid(row=1)
year =Label(frame, text="Jahr").grid(row=2)

today = datetime.datetime.now()
current_year = today.year

entryDay    = Spinbox(frame, from_= 1, to = 31)
entryMonth  = Spinbox(frame, from_= 1, to = 12)
entryYear   = Spinbox(frame, from_= 1900, to = current_year)

entryDay.grid(row=0, column=1)
entryMonth.grid(row=1, column=1)
entryYear.grid(row=2, column=1)




def calc():
    try:
        dayInt = int(entryDay.get())
        monthInt = int(entryMonth.get())
        yearInt = int(entryYear.get())

        if int(dayInt) > 31: 
            messagebox.showerror("Fehler", "Fehler. Gib einen Wert von 1-31 ein!")
            loop = False

        elif int(monthInt) > 12:
            messagebox.showerror("Fehler", "Fehler. Gib einen Wert von 1-12 ein!") 
            loop = False
        elif int(yearInt) > current_year:
            messagebox.showerror("Fehler", "Fehler. Gib einen Wert von 1900 bis " + str(current_year) + " ein!")
        
        else:
            loop = True

    except ValueError:
        messagebox.showerror("Fehler", "Fehler. Gib einen gültigen Wert ein!")
        loop = False

    if loop:
        now = datetime.datetime.now()
        
        newWindow = Toplevel(root)
        newWindow.title("Dein Alter")
        newWindow.geometry("180x50")

        birthAge = datetime.datetime(int(yearInt), int(monthInt), int(dayInt))
        current_age = relativedelta(now, birthAge)      
        
        if current_age.years > 1:
            label = Label(newWindow, text ="Dein Alter beträgt: " + str(current_age.years) + " Jahre.")
            label.pack()
        else:
            label = Label(newWindow, text ="Dein Alter beträgt: " + str(current_age.years) + " Jahr.")
            label.pack()
        
        
        closeThis = Button(newWindow, text="Okay", command=newWindow.destroy, bg="#99f08d", width=10)
        closeThis.pack()  
    
        
berechnenButton = Button(root, text="Berechnen", bg="#99f08d", command=calc)
berechnenButton.pack()


stopButton = Button(root, text="Beenden", command=root.destroy, bg="red")
stopButton.pack(side=BOTTOM)

root.mainloop()