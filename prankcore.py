from tkinter import Tk, messagebox
from tkinter.messagebox import *

root = Tk()
root.title("Minecraft launcher")
root.geometry("450x450")
if messagebox.askyesno("Open", "Are you sure you want to open Minecraft Launcher"):
    import virus_prank
