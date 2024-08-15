# ShortCoder
# by https://qpikzzbot.t.me
# license: CC BY

from tkinter import *
import json

white = "#E9E4E9"
grey = "#B1B0B8"
blue = "#3E4754"
green = "#698B38"
lime = "#A4BB77"

inputSymbols = 0
outputSymbols = 0

with open("keys.json","r",-1,"utf-8") as file:
    keys = json.load(file)

tk = Tk()
tk.geometry("720x480")
tk.title("ShortCoder")
tk["bg"] = grey
tk.resizable(0, 0)

input = Text(tk,
             bd=0,
             bg=blue,
             fg=white,
             width=42,
             height=22,
             insertbackground=white,
             selectbackground=white,
             selectforeground=blue,
             wrap=WORD)
input.place(x=10, y=40)

def updateSym(event):
    global inputLabel, inputSymbols, input
    inputSymbols = len(input.get("1.0","end-1c"))
    inputLabel.config(text=f"Symbols: {inputSymbols}")
input.bind("<KeyRelease>",updateSym)


output = Text(tk,
              bd=0,
              bg=blue,
              fg=white,
              width=42,
              height=22,
              insertbackground=blue,
              selectbackground=white,
              selectforeground=blue,
              wrap=WORD)
output.place(x=370, y=40)

Label(tk,
      text="Input",
      bg=grey,
      fg=blue).place(x=10, y=19)
Label(tk,
      text="Output",
      bg=grey,
      fg=blue).place(x=370, y=19)

inputLabel = Label(tk,
                   text=f"Symbols: {inputSymbols}",
                   bg=grey,
                   fg=blue)
inputLabel.place(x=10, y=395)
outputLabel = Label(tk,
                   text=f"Symbols: {inputSymbols}",
                   bg=grey,
                   fg=blue)
outputLabel.place(x=370, y=395)

def encode():
    global output, input, outputSymbols, outputLabel, keys
    text = input.get("1.0","end-1c").lower()

    for i in keys:
        text = text.replace(i,keys[i])

    output.delete("1.0",END)
    output.insert("1.0",text)

    outputSymbols = len(text)
    outputLabel.config(text=f"Symbols: {outputSymbols}")

def decode():
    global output, input, outputSymbols, outputLabel, keys
    text = input.get("1.0","end-1c")

    for i in keys:
        text = text.replace(keys[i],i)

    output.delete("1.0",END)
    output.insert("1.0",text)

    outputSymbols = len(text)
    outputLabel.config(text=f"Symbols: {outputSymbols}")


saencode = Button(tk,
                width=47,
                height=2,
                text="shorten and encode",
                bg=blue,
                fg=white,
                bd=0,
                activebackground=blue,
                activeforeground=lime,
                command=encode)
saencode.place(x=10, y=425)

decodeB = Button(tk,
                width=47,
                height=2,
                text="decode",
                bg=blue,
                fg=white,
                bd=0,
                activebackground=blue,
                activeforeground=lime,
                command=decode)
decodeB.place(x=370, y=425)

tk.mainloop()