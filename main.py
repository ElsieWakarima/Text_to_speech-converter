from tkinter import *
import os
from gtts import gTTS
from playsound import  playsound

root = Tk()
root.geometry("400x400")

label = Label(root, text="Input your text")
label.pack()
e = Entry(root, width=50)
e.pack()
clicked=StringVar()
clicked.set("English")
drop=OptionMenu(root,clicked,"English")
drop.pack()

def translator():
    mytext = e.get()
    language = "en"
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save("translate.mp3")
    os.system("start translate.mp3")

    e.delete(0, END)


button = Button(root, text="Convert", padx=25, bg="#A7C7E7", command=translator)
button.quit()
button.pack()

root.mainloop()
