import sys
from tkinter import *
import time
import keyboard

timestarted = time.time()
is_clock_on = False
window = Tk()
window.title("My big black clock")
window.configure(background="blue")

def tick():
    current_time_in_seconds = time.time()-timestarted
    current_time = time.gmtime(current_time_in_seconds)
    time_string = time.strftime('%M:%S', current_time) + '.' + (str(current_time_in_seconds)).split(".")[1][:3]
    clock.config(text=time_string)
    clock.after(200, tick)


clock=Label(window, font=("times", 50, "bold"), bg= "blue", fg="white")
clock.grid(row=0, column=1)
tick()

# while(True):
    # if(is_clock_on):
    #     # clock=Label(window, font=("times", 50, "bold"), bg= "blue")
    #     # clock.grid(row=0, column=1)
    #     tick()
    #     try:  # used try so that if user pressed other than the given key error will not be shown
    #         if keyboard.is_pressed('p'):  # if key 'q' is pressed 
    #             print('You just stopped the clock!')
    #             is_clock_on = False
    #     except:
    #         print("Error1")
    # else:
    #     try:  # used try so that if user pressed other than the given key error will not be shown
    #         if keyboard.is_pressed('p'):  # if key 'q' is pressed 
    #             print('You just started the clock!')
    #             is_clock_on = True
    #     except:
    #         print("Error2")

window.mainloop()
