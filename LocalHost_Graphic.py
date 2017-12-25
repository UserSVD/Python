import tkinter as tk
import socket 
"""
Test check localhotst
"""
#Fenetre utilisateur
userInterf=tk.Tk()
userInterf.geometry("500x400+300+200")
userInterf.title("Local Host")
#afiche le local host
labelIntro=tk.Label(userInterf, text="LOCAL HOST").pack()
ipUser=socket.gethostbyname_ex(socket.gethostname())[2]
labelLO=tk.Label(userInterf, text=ipUser).pack()








