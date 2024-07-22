import tkinter as tkinter
from tkinter import *
from tkinter import messagebox, ttk
import win32api
import winsound
import time
import os
from random import *
from tkinter import Tk, Label, PhotoImage

root = Tk()
root.title('A_B_O_B_A')
bg_image = PhotoImage(file="glad.gif")
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
root.config(bg='#400040')
"""root.iconbitmap('img/icon.ico')"""
root.resizable(0,0)
window_width,window_height=400,660
screen_width = root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

def welcome():
        tkinter.messagebox.showinfo('IDI NAHUY')
welcome()

def StatusChange():
        if(StatusMode['text']=="OFF"):
                time.sleep(0.2)
                StatusMode.config(text="ON", fg="lightgreen")
                winsound.Beep(1000,420)
                return True
        elif(StatusMode['text']=="ON"):
                time.sleep(0.2)
                StatusMode.config(text="OFF", fg="red")
                winsound.Beep(2500,400)
                return False

def saveKey():
        key = KeyCombobox.get()
        return key
        
def on_key_press():
        VK_F1 = win32api.GetKeyState(0x70)
        VK_F2 = win32api.GetKeyState(0x71)
        VK_F3 = win32api.GetKeyState(0x72)
        VK_F4 = win32api.GetKeyState(0x73)
        VK_F5 = win32api.GetKeyState(0x74)
        VK_F6 = win32api.GetKeyState(0x75)
        VK_F7 = win32api.GetKeyState(0x76)
        VK_F8 = win32api.GetKeyState(0x77)
        VK_F9 = win32api.GetKeyState(0x78)
        VK_F10 = win32api.GetKeyState(0x79)
        VK_F11 = win32api.GetKeyState(0x7A)
        VK_F12 = win32api.GetKeyState(0x7B)
        VK_Delete = win32api.GetKeyState(0x2E)
        VK_RETURN = win32api.GetKeyState(0x0D)
        VK_CAPITAL = win32api.GetKeyState(0x14)
        VK_NumLOCK = win32api.GetKeyState(0x90)
        VK_NUM0  = win32api.GetKeyState(0x30)
        VK_NUM1  = win32api.GetKeyState(0x31)
        VK_NUM2  = win32api.GetKeyState(0x32)
        VK_NUM3  = win32api.GetKeyState(0x33)
        VK_NUM4  = win32api.GetKeyState(0x34)
        VK_NUM5  = win32api.GetKeyState(0x35)
        VK_NUM6  = win32api.GetKeyState(0x36)
        VK_NUM7  = win32api.GetKeyState(0x37)
        VK_NUM8  = win32api.GetKeyState(0x38)
        VK_NUM9  = win32api.GetKeyState(0x39)
        
        if(VK_F1<0 and "F1"==saveKey() or VK_F2<0 and "F2"==saveKey() or VK_F3<0 and "F3"==saveKey() or VK_F4<0 and "F4"==saveKey()
        or VK_F5<0 and "F5"==saveKey() or VK_F6<0 and "F6"==saveKey() or VK_F7<0 and "F7"==saveKey() or VK_F8<0 and "F8"==saveKey()
        or VK_F9<0 and "F9"==saveKey() or VK_F11<0 and "F11"==saveKey() or VK_F12<0 and "F12"==saveKey() or VK_Delete<0 and "SUPR"==saveKey() 
        or VK_RETURN<0 and "ENTER"==saveKey() or VK_CAPITAL<0 and "CAPSLOCK"==saveKey() or VK_NumLOCK<0 and "NUM_LOCK"==saveKey()):
            StatusChange()  
        root.after(100,on_key_press)
root.after(100,on_key_press)

def saveRecoil():
        tkinter.messagebox.showinfo('Recoil config','Recoil config saved correctlly!')
 
def mouse_down():
        lmb_state = win32api.GetKeyState(0x01)
        return lmb_state < 0
        root.after(100,mouse_down)
root.after(100,mouse_down)

def recoil():
        Down = recoilDownEntry.get()
        Up = recoilUpEntry.get()
        Left = recoilLeftEntry.get()
        Right = recoilRightEntry.get()
        if (mouse_down() and StatusMode['text']=='ON'):
            win32api.mouse_event(0x0001, -abs(int(Left)), int(Down))
            win32api.mouse_event(0x0001, int(Right), -abs(int(Up)))
        root.after(10,recoil)
root.after(10,recoil) 

Title = Frame(root, width=600)
Title.pack()
Title = Label(Title,text="Rosh1ajin NoRecoil", width=600, padx=80, pady=20, bg='#C71585', fg="white", font=("Segoe UI", 16, "italic", "bold")).pack()

StatusFrame = Frame(root, bg='#FF69B4')
StatusFrame.pack(anchor="w", padx=0,pady=25)
StatusLabel=Label(StatusFrame, text="MODE :", bg='#FF69B4', font=("Segoe UI",12,"italic","bold"),fg="green")
StatusLabel.pack(side=LEFT)
StatusMode=Label(StatusFrame, text="OFF",bg='#FF69B4', font=("Segoe UI",11,"italic","bold"),fg="red")
StatusMode.pack(pady=5)

ConfigKeyLabelFrame = LabelFrame(root, text="Script config",font=("Segoe UI", 12, "italic", "bold"), bg='#FF69B4', fg="white")
ConfigKeyLabelFrame.pack(anchor="w",padx=0, ipadx=100, ipady=15)

margin1= Label(ConfigKeyLabelFrame, bg='#FF69B4')
margin1.pack()

KeyLabel = Label(ConfigKeyLabelFrame, text="On/Off Key", bg='#FF69B4', font=("Segoe UI", 11, "bold"), fg="darkgrey")
KeyLabel.place(x=55,y=7)

KeyCombobox = ttk.Combobox(ConfigKeyLabelFrame, state="readonly", values=["F1","F2","F3","F4","F5","F6","F7","F8","F9","F11","F12","ENTER","SUPR","CAPSLOCK","NUM_LOCK"], width=10, font=("Segoe UI", 10))
KeyCombobox.place(x=155,y=10)

RecoilConfig  = LabelFrame(root, text="Config", font=("Segoe UI",12,"bold","italic"), fg="white", bg='#FF69B4')
RecoilConfig.pack(anchor="w",padx=0, ipadx=120, ipady=65, pady=25)

recoilEmptyMargin = Label(RecoilConfig, bg='#FF69B4')
recoilEmptyMargin.pack()

recoilDown = Label(RecoilConfig, text="Down", bg='#FF69B4', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilDown.place(x=20,y=7)
recoilDownEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilDownEntry.insert(0,"0")
recoilDownEntry.place(x=35,y=30)

recoilUp = Label(RecoilConfig, text="Up", bg='#FF69B4', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilUp.place(x=200,y=7)
recoilUpEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilUpEntry.insert(0,"0")
recoilUpEntry.place(x=210,y=30)

recoilLeft = Label(RecoilConfig, text="Left", bg='#FF69B4', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilLeft.place(x=20,y=80)
recoilLeftEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilLeftEntry.insert(0,"0")
recoilLeftEntry.place(x=35,y=105)

recoilRight = Label(RecoilConfig, text="Right", bg='#FF69B4', font=("Segoe UI", 10, "bold"), fg="lightgreen")
recoilRight.place(x=200,y=80)
recoilRightEntry = Entry(RecoilConfig, width=6, font=("Segoe UI", 10, "bold"), fg="black", justify="center")
recoilRightEntry.insert(0,"0")
recoilRightEntry.place(x=210,y=105)

happyFace = Label(RecoilConfig, text="♥‿♥", bg='#FF69B4', font=("Segoe UI", 20, "bold"), fg="pink")
happyFace.place(x=120,y=45)

updates = Label(root, text="READY", bg='#FF69B4', font=("Segoe UI", 10, "bold"), fg="lightgreen")
updates.place(x=180,y=450)

root.mainloop()
