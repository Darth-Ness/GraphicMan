import tkinter
import os

def install():
    os.system('sudo pacman -S' + " " + packageName.get())

def uninstall():
    os.system('sudo pacman -R' + " " + packageName.get())

def update():
    os.system('sudo pacman -Syu')

def installAUR():
    os.system('git clone' + packageName.get)

root = tkinter.Tk()
root.configure(padx=30, pady=30, background="white")

button1 = tkinter.Button(text='install', command=install)
button1.pack(anchor=tkinter.NW, side=tkinter.LEFT)

button2 = tkinter.Button(text="Uninstall", command=uninstall)
button2.pack(anchor=tkinter.NW, side=tkinter.LEFT)

button3 = tkinter.Button(text="Update", command=update)
button3.pack(anchor=tkinter.NW, side=tkinter.LEFT)

button4 = tkinter.Button(text="install from AUR", command=installAUR)
button4.pack(anchor=tkinter.NW, side=tkinter.LEFT)

packageName = tkinter.Entry(root, text='Hello there!')
packageName.pack()

#root.destroy()
root.mainloop()