# The Magic 8 Ball

# Imports that I needed to use in order to make my program functional
import tkinter as tk
from tkinter import *
import logging # Allowed me to use logging callbacks
import time    # Allowed me to implement time
import random  # Allowed me to use the 'random' callback
import mod_imp # Allowed me use my personal module import



# This is my logging config 
logging.basicConfig(
    filename="log.txt", # This either makes a file called log.txt or uses log.txt if exists
    level=logging.DEBUG, # Catches errors within logging
    format="%(asctime)s - %(message)s", # This tells the config what I'm needing logged
    datefmt="%m-%d %H:%M" # Formats the timestamps inside the log
)

logger = logging.getLogger() # Used to record the logging messages



# Creates program that loops for magic 8 ball interaction with user

def magicball_interact():
    ask = ask_entry.get()   # Takes users input
    ingore_punct = mod_imp.replace_punct(ask)        # Ingores punctuation within answers
    response = random.choice(mod_imp.magicball_all())  # Gives random magic 8 ball response

    if  ingore_punct.lower() == "will i become rich":     # Instance of asking a different question // Easter Egg
        response = "Don't ask questions you don't want the answer to"
        logger.info("User asked 'will I become rich' and Magic 8 ball replied 'Don't ask questions you don't want the answer to'") # Logs special response)
    elif ask == "":                                   # Another easter egg
        response = "Sorry, mind reading is not in my capabilities. Please try again" 
        logger.info("User asked '' Magic 8 ball replied 'Sorry, mind reading is not in my capabilities. Please try again'") # Logs special response
    elif ask.lower() == "exit" or ask.lower() == "bye":  # Tells loop that if 'exit' or 'bye' is entered in lowercase to end program
        response = "Thanks for playing! Goodbye!"
        logger.info("User asked to end program! Magic 8 ball replied 'Thanks for playing! Goodbye!") # Sends info to log that you ended program
        win.destroy()         # Closes window if triggered
    else:
        response = random.choice(mod_imp.magicball_all())     # Magic 8 balls responds if no special conditions are met
        logger.info(f"User asked '{ask}' Magic 8 ball replied '{response}'") # This sends all other information to log that doesn't have special conditions
    
    response_label.config(text=response)   # Response label that converts answer to widget

    win.after(5000, clear_response) # Clears 8 ball response after 5 seconds

def clear_response():   # Creates the function in order to process clearing the response
    response_label.config(text="")


win = Tk()   # Creates the window

icon = PhotoImage(file="magicball_icon.png")  # Upload img
win.iconphoto(False, icon) # Creates icon for window only

win.geometry("400x400")  # Sets starting screen size

win.minsize(400, 400) # Min screen size
win.maxsize(400, 400) # Max screen size

center_frame =Frame(win) # Holds widgets for win
center_frame.pack(expand=True)

header_frame = Frame(center_frame) # Holder icon widget for header
header_frame.pack(anchor="center", pady= 20) # Centers and padding on y-axis

icon_header = Label(header_frame, image=icon) # Puts icon above header
icon_header.pack()

header = Label(win, text= "Magic 8 Ball", font=("Arial", 24, "bold"))  # Creates header label and sets desired parameters and style choices
header.pack(anchor="center", pady=5)

desc = Label(win, text= "How to play: Ask The Magic 8 Ball a question (press 'esc' to end or say 'exit' or 'bye'):", 
             anchor=tk.CENTER, font= ("Arial", 10), wraplength=300) # Creates desc label and sets desired parameters along with wraps text                                                                    
desc.pack(anchor="center", pady=5)                                  # theres no text cut-off

ask_entry = Entry(win)   # Creates ask_entry to hold what user asks
ask_entry.pack(anchor="center", pady=5) #Creates padding on y-axis and centers (All "center" and pady will center and create padding on y0axis)

ask_button = tk.Button(win, anchor=tk.CENTER, text="Ask", command=magicball_interact) # Creates functional button to submit the ask to program
ask_button.pack(anchor="center", pady=10)

response_label = tk.Label(win, text="", font=("Arial", 16), wraplength=300)   # Creates a place to display response from program
response_label.pack(anchor="center", pady=10)

win.bind("<Escape>", lambda event: win.destroy())  # Makes escape key functional to end program

win.bind("<Return>", lambda event: magicball_interact())  # Makes return key functional to submit response without clicking 'ask' button

win.mainloop()   # Loops main program until conditions are met to end
