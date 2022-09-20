#importing required libraries
from tkinter import *
import tkinter.messagebox
from captcha.image import ImageCaptcha
import string
import random
import os
import pyttsx3

audio_captcha=''
image_captcha=''

#generates any 4 random numbers and is stored in a variable , audio captcha

def generate_digit_captcha():
    s1='';s=''
    for i in range(4):
        a = str(random.randint(0,9))
        s=s+a
        s1=s1+a+" "

    global audio_captcha
    audio_captcha=s

    return s1




#function to generate the first audio captcha with the help of voice library which is imported from pyttsx3 library
def generate_audio_captcha():
    s=generate_digit_captcha()
    #print(s)

    voiceEngine = pyttsx3.init()

    voiceEngine.setProperty('rate',170)
    voiceEngine.setProperty('volume',1.0)

    voices = voiceEngine.getProperty('voices')
    voiceEngine.setProperty('voice',voices[1].id)

    voiceEngine.say(s)
    voiceEngine.runAndWait()
    voiceEngine.say(s)
    voiceEngine.runAndWait()

    #print("Audio Captcha Generated.\n\n")

def regenerate_audio_captcha():
    generate_audio_captcha()
#function to return the audio when the button is pressed
def get_audio():
    return audio_captcha




def check_audio_captcha():
    #answer = input("\nEnter Value : ")
    if ans.get() == get_audio():
        tkinter.messagebox.showinfo("SUCCESS!","Captcha Code Matched.")
        ans.set("")

    else:
        tkinter.messagebox.showinfo("WRONG!","Captcha Code does not Matched.")
        ans.set("")



root = Tk()
root.title("GUI : CAPTCHA Generation")

root.geometry("400x450")

root.configure(background = '#ffd9db')


ans = StringVar()
ans1 = StringVar()


MainFrame = Frame(root,bg = 'Powder Blue',pady = 2, width =1350, height = 100, relief = RIDGE)
MainFrame.grid(row=1,column=0)

RightFrame  =  Frame(MainFrame ,bd=10, width =200, height=200, padx=10,pady=2,bg='#68DEED',relief=RIDGE)
RightFrame.pack(side=RIGHT)

Label_1 =Label(RightFrame, font=('lato black', 33,'bold'), text=" Audio Captcha ",padx=2,pady=2, bg="yellow",fg ="black")
Label_1.grid(row=0, column=0,sticky=W)

Label_2 =Label(RightFrame, font=('arial', 20,'bold'), text="",padx=2,pady=2, bg="#68DEED",fg = "black")
Label_2.grid(row=1, column=0,sticky=W)

Label_9 =Button(RightFrame, font=('arial', 19,'bold'), text="Play Audio",padx=2,pady=2, bg="blue",fg = "white",command=generate_audio_captcha)
Label_9.grid(row=4, column=0)

Label_7 =Label(RightFrame, font=('arial', 20,'bold'), text="",padx=2,pady=2, bg="#68DEED",fg = "black")
Label_7.grid(row=2, column=0,sticky=W)

Entry_1=Entry(RightFrame,font=('arial',20,'bold'),bd=2,fg="black",textvariable= ans, width=14,justify=LEFT).grid(row=5,column=0)

Label_7 =Label(RightFrame, font=('arial', 20,'bold'), text="",padx=2,pady=2, bg="#68DEED",fg = "black")
Label_7.grid(row=6, column=0,sticky=W)

Label_7 =Label(RightFrame, font=('arial', 20,'bold'), text="  ",padx=2,pady=2, bg="#68DEED",fg = "black")
Label_7.grid(row=6, column=1,sticky=W)

Label_8 =Button(RightFrame, font=('Arial', 25,'bold'), text="Check",padx=2,pady=2, bg="white",fg = "blue",command=check_audio_captcha)
Label_8.grid(row=9, column=0)

Label_4 =Button(RightFrame, font=('arial', 15,'bold'), text="Regenerate",padx=2,pady=2, bg="white",fg = "red",command=regenerate_audio_captcha)
Label_4.grid(row=10, column=0)

Label_7 =Label(RightFrame, font=('arial', 20,'bold'), text="      ",padx=2,pady=2, bg="#68DEED",fg = "black")
Label_7.grid(row=11, column=1,sticky=W)

root.mainloop()