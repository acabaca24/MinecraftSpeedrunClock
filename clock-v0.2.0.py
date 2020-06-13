from pynput import keyboard
from tkinter import *
import time

play_pause_keyboard_combo = [
	{keyboard.Key.ctrl, keyboard.KeyCode(char='p')},
	{keyboard.Key.ctrl, keyboard.KeyCode(char='P')}
]

restart_keyboard_combo = [
	{keyboard.Key.ctrl, keyboard.KeyCode(char='r')},
	{keyboard.Key.ctrl, keyboard.KeyCode(char='R')}
]

timestarted = 0
is_clock_on = False
is_first_time = True
window = Tk()

#--------------for tests-------------------
window.lift()
window.attributes("-topmost", True)
#--------------for tests-------------------

window.title("My big black clock")
window.configure(background="blue")
clock=Label(window, font=("times", 50, "bold"), bg= "blue", fg="white")
clock.grid(row=0, column=1)
clock_refresh_ratio = 85

current = set() #Where we store the keys pressed

def change_clock_status(next_status):
	global is_clock_on 
	is_clock_on = next_status
	if(is_clock_on):
		tick()
		print("clock start")
	else:
		print("clock stop")

def restart_clock():
	global is_clock_on
	global timestarted
	timestarted = time.time()
	change_clock_status(not is_clock_on)
	print("clock restart")

def tick(): #what makes the clock tick
    current_time_in_seconds = time.time()-timestarted
    current_time = time.gmtime(current_time_in_seconds)
    time_string = time.strftime('%M:%S', current_time) + '.' + (str(current_time_in_seconds)).split(".")[1][:3]
    clock.config(text=time_string)
    if(is_clock_on):
    	clock.after(clock_refresh_ratio, tick)

def start_stop():
	if(is_clock_on):
		change_clock_status(False)
	else:
		global is_first_time
		if(is_first_time):
			restart_clock()
			is_first_time = False
		change_clock_status(True)

def on_press(key):
	if any([key in COMBO for COMBO in play_pause_keyboard_combo + restart_keyboard_combo]):
		current.add(key)
		if any(all(k in current for k in COMBO) for COMBO in play_pause_keyboard_combo):
		    start_stop()
		elif any(all(k in current for k in COMBO) for COMBO in restart_keyboard_combo):
		    restart_clock()

def on_release(key):
	if any([key in COMBO for COMBO in play_pause_keyboard_combo + restart_keyboard_combo ]):
		current.remove(key)

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

window.mainloop()
