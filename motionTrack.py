import tkinter as tk
import cv2

application = tk.Tk()
application.title("Motion Tracker")
application.geometry("1000x600")
titleText = tk.Label(application, text="Welcome to The Turret Defense System Software!", font=("Arial", 30))
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
    
button = tk.Button(application, text="Start!", command=button_click_start, height=5, width=30, font=("Arial", 30))
button.pack()

button = tk.Button(application, text="About", command=button_click_about, height=5, width=30, font=("Arial", 30))
button.pack()

application.mainloop()

