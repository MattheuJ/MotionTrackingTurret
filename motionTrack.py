import tkinter as tk
import cv2

application = tk.Tk()
application.title("Motion Tracker")
application.geometry("1000x600")
application.configure(bg='#2b2b2b')  

titleText = tk.Label(application, text="Welcome to The Turret Defense System Software!", 
                    font=("Arial", 30), bg='#2b2b2b', fg='white')  
titleText.pack()

def button_click_start():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release
    cv2.destroyAllWindows

def button_click_about():
    print("Welcome to The Turret Defense System Software! This software is designed to track the motion of an enemy and configure the turret accordingly. Made by Mattheu Jimenez for CIS 5")

button = tk.Button(application, text="Start!", command=button_click_start, 
                  height=4, width=30, font=("Arial", 30),
                  bg='#4a4a4a', fg='white') 
button.pack()

button = tk.Button(application, text="About", command=button_click_about, 
                  height=4, width=30, font=("Arial", 30),
                  bg='#4a4a4a', fg='white')  
button.pack()

application.mainloop()

