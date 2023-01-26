import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import os
import subprocess
import webbrowser
import time
from time import sleep

window = tk.Tk()
window.title("sddtk 1.0.0")
window.geometry("400x340")

usn = tk.Label(text="Username (Leave empty for anonymous login)")
usnentry = tk.Entry(width=50)

appid = tk.Label(text="Steam AppID")
appident = tk.Entry(width=50)

depid = tk.Label(text="Depot ID")
depident = tk.Entry(width=50)

manid = tk.Label(text="Manifest ID")
manident = tk.Entry(width=50)

ossel = tk.Label(text="Operating system")
osselent = ttk.Combobox(state="readonly", values=["Windows", "Linux (Bash)"], width=50)

pwd = tk.Label(text="Enter password in DepotDownloader terminal window,")
pwd2 = tk.Label(text="which pops up after download button clicked.")
pwd3 = tk.Label(text="Leave empty for anonymous login.")

def handle_dl(event):
    index = osselent.current()
    if(index == 0):
        subprocess.run(["dotnet", "DepotDownloader.dll", "-app", appident.get(), "-depot", depident.get(), "-manifest", manident.get(), "-username", usnentry.get()])
    elif(index == 1):
        subprocess.run(["./depotdownloader", "-app", appident.get(), "-depot", depident.get(), "-manifest", manident.get(), "-username", usnentry.get()])
    else:
        messagebox.showerror("Error", "Please select OS!")
    dlbutton.configure(state=DISABLED)
    dlbutton.configure(state=NORMAL)

def handle_sdb(event):
    url = "https://steamdb.info/instantsearch/"
    webbrowser.open(url)
    sdbbutton.configure(state=DISABLED)
    sdbbutton.configure(state=NORMAL)

dlbutton = tk.Button(text="Download", width=40)
sdbbutton = tk.Button(text="SteamDB", width=40)

dlbutton.bind("<Button-1>", handle_dl)
sdbbutton.bind("<Button-1>", handle_sdb)

usn.pack()
usnentry.pack()
appid.pack()
appident.pack()
depid.pack()
depident.pack()
manid.pack()
manident.pack()
ossel.pack()
osselent.pack()
dlbutton.pack(pady=12)
sdbbutton.pack()
pwd.pack()
pwd2.pack()
pwd3.pack()

window.resizable(False,False)
window.mainloop()
