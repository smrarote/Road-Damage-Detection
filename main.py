import tkinter as tk
from Windows.firstpage import FirstPage
from Windows.login import LoginPage
from Sensor.camera import Camera
from Sensor.gps import Gps
from Windows.secondpage import SecondPage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("RDD : Road Damage Detector")

    # screen size
    screen_width = root.winfo_screenwidth()//2
    screen_height = root.winfo_screenheight()//2
    root.geometry(str(screen_width) + "x" + str(screen_height))
    root.resizable(False, False)

    # login page
    LoginPage(root)


    root.mainloop()

