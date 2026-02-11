# import random module
import random

import tkinter as tk

#create subjects

celebrities = ["Virat Kohli", "Elon Musk", "Modi", "Shah Rukh Khan", "Rohit Sharma"]
actions = ["spotted dancing with", "secretly met", "fighting with", 
           "launching", "caught stealing"] 
objects = ["aliens", "robots", "a new startup", "IPL trophy", "AI system"]
places = ["in Mumbai", "in Delhi", "at NASA", "in a village", "on Mars"]
    
#start headline geneartion loop

def generate_headline():
    celeb = random.choice(celebrities)
    action = random.choice(actions)
    obj = random.choice(objects)
    place = random.choice(places)
    
    headline = f"Breaking News: {celeb} {action} {obj} {place}"
    label.config(text=headline)
    
def exit_app():
    print("\n Thanks for using the fake news headline generator")
    root.destroy()
    
#create window

root = tk.Tk()
root.title("Fake news headline generator 1")
root.geometry('700x300')

#label to display headline   

label = tk.Label(
    root, text="click the button to generate headline",
    font = ('calibri',20,'bold'),
    wraplength = 650,
    background="yellow",
                 foreground="black",
                 padx=20,
                 pady=20)

label.pack(pady=20)

# button to generate headline
generate_btn = tk.Button(root,
                         text="Generate Headline",
                         font=("Calibri", 14),
                         command=generate_headline)

generate_btn.pack(pady=20)

# exit button
exit_btn = tk.Button(root,
                     text="Exit",
                     font=("Calibri", 14),
                     command=exit_app)

exit_btn.pack(pady=10)

# run app
root.mainloop()

