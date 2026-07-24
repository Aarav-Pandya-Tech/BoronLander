#Dependencies
from tkinter import *
from PIL import Image, ImageTk
import time

#GUI prperties
display = Tk()
display.geometry("320x480")
display.resizable(False,False)
display.title("Boron Lander")
def force_fullscreen():
    display.attributes('-fullscreen', True)

#The bg is set
original_image = Image.open("boronbackg.jpg")
bg_image = ImageTk.PhotoImage(original_image)

# Create the label placeholder for bg
bg_label = Label(display, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

edit_image = Image.open("editbutton.jpg")
edittk_image = ImageTk.PhotoImage(edit_image)

# Create the label placeholder for bg
edit_button = Button(display, image=edittk_image,bg="#7ae7ff",command=display.destroy,relief="flat",activebackground="#7ae7ff")
edit_button.place(x=0, y=0)
# Time is displayed
def update_time():
    time_current = time.strftime("%H:%M")
    timelabel.config(text=time_current)
    timelabel.after(1000, update_time)
timelabel = Label(display,text="", font=("Helvetica", 53, "bold","italic"), fg="#2d4259", bg="#7ae7ff")
timelabel.place(relx=0.5, y=124, anchor="center")

display.after(250, force_fullscreen)
update_time()
display.mainloop()