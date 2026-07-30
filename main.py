#Dependencies
from tkinter import *
from PIL import Image, ImageTk
import time
import requests 
import adafruit_dht
import board
import os
from tkinter import messagebox

d = adafruit_dht.DHT22(board.D26)


api = "0db0cbf680c57180da22dc545cbfb94e" 
    
    # Coordinates example (London)
lat = 22.250093
lon = 73.185112
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"
    
def get_icon():
    try:
        response = requests.get(url)
        response.raise_for_status()
    
        weather_data = response.json().get('weather', [])
        if weather_data and isinstance(weather_data, list):
            return weather_data[0].get('icon')
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")


    except Exception as err:
        print(f"An error occurred: {err}")
def get_weatherdata():
    try:
        response = requests.get(url)
        response.raise_for_status()
    
        weather_data = response.json().get('weather', [])
        if weather_data and isinstance(weather_data, list):
            return weather_data[0].get('main')
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")


    except Exception as err:
        print(f"An error occurred: {err}")


#GUI prperties
display = Tk()
display.geometry("320x480")
display.resizable(False,False)
display.title("Boron Lander")
def force_fullscreen():
    display.attributes('-fullscreen', True)

#The bg is set
original_image = Image.open(r"/home/shariq/Desktop/BoronLander/boronbackg.jpg")#r"/home/shariq/Desktop/BoronLander/boronbackg.jpg")#change locantion
bg_image = ImageTk.PhotoImage(original_image)

# Create the label placeholder for bg
bg_label = Label(display, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

edit_image = Image.open(r"/home/shariq/Desktop/BoronLander/editbutton.jpg")#r"/home/shariq/Desktop/BoronLander/editbutton.jpg")#change location
edittk_image = ImageTk.PhotoImage(edit_image)

# Create the label placeholder for bg
edit_button = Button(display, image=edittk_image,bg="#7ae7ff",command=display.destroy,relief="flat",activebackground="#7ae7ff")
edit_button.place(x=0, y=0)
# Time is displayed
def update_time():
    time_current = time.strftime("%H:%M")
    timelabel.config(text=time_current)
    timelabel.after(1000, update_time)
timelabel = Label(display,text="", font=("Helvetica", 50, "bold","italic"), fg="#2d4259", bg="#7ae7ff")
timelabel.place(relx=0.5, y=118, anchor="center")


weather_image = Image.open(fr"/home/shariq/Desktop/BoronLander/{get_icon()}_t@4x.png")#r"/home/shariq/Desktop/BoronLander/boronbackg.jpg")#change locantion
start_x = 20
start_y = 40
crop_w = 180
crop_h = 110

# 3. Calculate bounding box: (left, upper, right, lower)
box = (start_x, start_y, start_x + crop_w, start_y + crop_h)

resized_weather_image = weather_image.crop(box)


icon_image = ImageTk.PhotoImage(resized_weather_image)

# Create the label placeholder for bg
icon_label = Label(display, image=icon_image, bg = "#7ae7ff")
icon_label.image = icon_image
icon_label.place(relx=0.5,anchor="center", y=350)



weather_label = Label(display, text=get_weatherdata(), font=("Helvetica", 10, "bold"), fg="#2d4259", bg = "#7ae7ff")
weather_label.place(relx=0.5,anchor="center", y=435)

def update_weather():
    weather_image = Image.open(fr"/home/shariq/Desktop/BoronLander/{get_icon()}_t@4x.png")#r"/home/shariq/Desktop/BoronLander/boronbackg.jpg")#change locantion
    start_x = 20
    start_y = 40
    crop_w = 180
    crop_h = 110

    # 3. Calculate bounding box: (left, upper, right, lower)
    box = (start_x, start_y, start_x + crop_w, start_y + crop_h)

    resized_weather_image = weather_image.crop(box)


    icon_image = ImageTk.PhotoImage(resized_weather_image)

    # Create the label placeholder for bg
    icon_label.config(image=icon_image)
    icon_label.image = icon_image




    weather_label.config(text=get_weatherdata())

    icon_label.after(1000,lambda: update_weather())






    



def update_t():
    try:
        temp = f"{d.temperature}°C"
    except:
        temp = "NotFound"
    t.config(text=temp)
    timelabel.after(10, update_t)
t = Label(display,text="", font=("Helvetica", 35, "bold","italic"), fg="#2d4259", bg="#7ae7ff")
t.place(x= 110, y=167)



def update_h():
    try:
        humidity = f"{d.humidity}%"
    except:
        humidity = "NotFound"
    h.config(text=humidity)
    timelabel.after(10, update_h)
h = Label(display,text="", font=("Helvetica", 35, "bold","italic"), fg="#2d4259", bg="#7ae7ff")
h.place(x=110, y=240)



def shutdown_system():
    """Ask for confirmation and shut down the system."""
    confirm = messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shut down the system?")
    if confirm:
        try:
            # Linux shutdown command (requires sudo privileges)
            exit_code = os.system("sudo shutdown now")
            if exit_code != 0:
                messagebox.showerror("Error", "Shutdown command failed. Try running the script with sudo.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

sb_image = Image.open(r"/home/shariq/Desktop/BoronLander/sb.jpg")#r"/home/shariq/Desktop/BoronLander/editbutton.jpg")#change location
sbtk_image = ImageTk.PhotoImage(sb_image)
sb_button = Button(display, image=sbtk_image,bg="#7ae7ff",command= shutdown_system,relief="flat",activebackground="#7ae7ff")
sb_button.place(relx= 1, y=0)



display.after(250, force_fullscreen)
update_t()
update_h()
update_time()
update_weather()
display.mainloop()