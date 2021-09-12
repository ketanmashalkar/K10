import tkinter as tk

win=tk.Tk()
win.title("JAI HIND")
win.geometry("1920x1200")

# add frame1
frame1=tk.Frame(master=win,width=50,height=110,bg="orange")
frame1.pack(fill=tk.X) # fill=tk.X,tk.Y,tk.BOTH

# add frame2
frame2=tk.Frame(master=win,width=10000,height=100,bg="green")
frame2.pack(side=tk.BOTTOM)


# add frame3
frame3=tk.Frame(master=win,width=50,height=50,bg="navy blue")
frame3.pack(expand=True)

frame4=tk.Frame(x,y,r,tk.CanvasName):
x0=x-r
y0=y-r
x1=x-r
y1=y=r
return canvasName.create_oval(x0,y0,x1,y1)
create_circle(100,100,20,myCanavs)
create_circle(50,25,10,myCanvas)
win.mainloop()