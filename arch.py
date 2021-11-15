import tkinter
import os

def install():
    os.system('sudo pacman -S' + " " + packageName.get())

def uninstall():
    os.system('sudo pacman -Rs' + " " + packageName.get())

def update():
    os.system('sudo pacman -Syu')

def info():
    os.system('sudo pacman -Qi' + " " + packageName.get())

def search():
    os.system('sudo pacman -Ss' + " " + packageName.get())

def installAUR():
    os.system('git clone https://aur.archlinux.org/' + packageName.get() + ".git")
    os.system('cd' packageName.get())
    os.system('makepkg -si')
    os.system('cd -')

root = tkinter.Tk()
root.configure(padx=30, pady=30, background="white")

button1 = tkinter.Button(text='install', command=install)
button1.pack(anchor=tkinter.NW, side=tkinter.LEFT)

button2 = tkinter.Button(text="Uninstall", command=uninstall)
button2.pack(anchor=tkinter.NW, side=tkinter.LEFT)

button3 = tkinter.Button(text="Update", command=update)
button3.pack(anchor=tkinter.NW, side=tkinter.LEFT)

button4 = tkinter.Button(text="Info", command=info)
button4.pack(anchor=tkinter.NW, side=tkinter.LEFT)

button5 = tkinter.Button(text="Search", command=search)
button5.pack(anchor=tkinter.NW, side=tkinter.LEFT)

button7 = tkinter.Button(text="install from AUR", command=installAUR)
button7.pack(anchor=tkinter.NW, side=tkinter.LEFT)

packageName = tkinter.Entry(root, text='Hello there!')
packageName.pack()

#root.destroy()
root.mainloop()