import tkinter as tk
import tkinter.font as tfont
from tkinter import *

#creating the box
win = tk.Tk()
win.title("Encryption/Decryption")
win.configure(width=600, height=300)
win.resizable(width=FALSE, height=FALSE)
canvas = tk.Canvas(win,height = 300, width=600, bg="grey")
canvas.pack()
bold_font = tfont.Font(family="Body",size=12,weight="bold")
label1 = tk.Label(win,text= "Input text",width=20,bg="grey")
label1.config(font=bold_font)
canvas.create_window(100,90,window=label1)
user_text = tk.Entry(win)
canvas.create_window(100,120,window=user_text)
label2=tk.Label(win,text="option",width=25,bg="grey")
label2.config(font=bold_font)
canvas.create_window(300,80,window=label2)
var=tk.IntVar()
def choice():
    x = var.get()
    if(x==1):
        encryption()
    elif(x==2):
        decryption()
# creating the encryption
def encryption ():
   txt = user_text.get()
   c_txt = " "
   s = 3
   for i in range(len(txt)):
        char = txt[i]
        if (char.isupper()):
            c_txt+= chr((ord(char)+s-65)% 26 +65)
        else:
            c_txt += chr((ord(char)+s-97)% 26 +97)
   label3 =tk.Label(win,text=c_txt,width=20,bg="light blue")
   label3.config(font=bold_font)
   canvas.create_window(300,120,window=label3)

# creating the decryption
def decryption():
    c_txt = user_text.get()
    txt = ""
    s = 3
    for i in range(len(c_txt)):
     char = c_txt[i]
     if (char.isupper()):
        txt+= chr((ord(char)-s-65)% 26 +65)
     else:
        txt += chr((ord(char)-s-97) % 26 +97)
    label4 =tk.Label(win,text=txt,width=20,bg="light blue")
    label4.config(font=bold_font)
    canvas.create_window(300,120,window=label4)

#making the button for user interact
label5=tk.Radiobutton(win, text="Encryption",padx = 20, variable=var, value=1,command=choice,bg="light yellow")
label5.config(font=bold_font)
canvas.create_window(300,100,window=label5)
label6=tk.Radiobutton(win, text="Decryption",padx = 20, variable=var, value=2,command=choice,bg="light yellow")
label6.config(font=bold_font)
canvas.create_window(300,130,window=label6)
label7 =tk.Label(win,text="output text", width=20,bg="grey")
label7.config(font=bold_font)
canvas.create_window(600,300,window=label7)
win.mainloop()