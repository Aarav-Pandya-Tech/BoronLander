#Dependencies
from tkinter import *
from PIL import Image, ImageTk
import time

#GUI prperties
display = Tk()
display.geometry("480x800")
display.resizable(False,False)
display.title("Boron Lander")

#The bg is set
original_image = Image.open(r"C:\Users\ScipoTech\Downloads\boronbackg.jpg")
bg_image = ImageTk.PhotoImage(original_image)

# Create the label placeholder for bg
bg_label = Label(display, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# Time is displayed
def update_time():
    time_current = time.strftime("%H:%M")
    timelabel.config(text=time_current)
    timelabel.after(1000, update_time)
timelabel = Label(display,text="", font=("Helvetica", 85, "bold","italic"), fg="#2d4259", bg="#7ae7ff")
timelabel.place(relx=0.5, y=240, anchor="center")
update_time()
display.mainloop()