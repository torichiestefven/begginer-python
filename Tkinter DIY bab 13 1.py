#github

from tkinter import*
import tkinter
import time

root=Tk()
canvas=Canvas(root,width=352,height=204)
canvas.pack()

a=canvas.create_polygon(150,50,175,10,200,50,240,75,200,100,175,140,150
                        ,100,110,75,fill="white")


while True:
    zz=canvas.create_polygon(150,50,175,10,200,50,fill='black')
    root.update()
    time.sleep(1)
    canvas.delete(zz)
    zzz=canvas.create_polygon(200,50,240,75,200,100,fill='black')
    root.update()
    time.sleep(1)
    canvas.delete(zzz)
    zzzz=canvas.create_polygon(200,100,175,140,150,100,fill='black')
    root.update()
    time.sleep(1)
    canvas.delete(zzzz)
    zzzzz=canvas.create_polygon(150,100,110,75,150,50,fill='black')
    root.update()
    time.sleep(1)
    canvas.delete(zzzzz)
    
tk.mainloop()
























#github
