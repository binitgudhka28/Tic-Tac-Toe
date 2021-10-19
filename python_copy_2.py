from tkinter import *
import os
import python_project_1
from PIL import Image, ImageTk

root = Tk()
root.title("Tic Tac Toe")
root.geometry("1920x1080")
root.configure(bg="#FF7C35")


def b_pressed():
    root.destroy()
    python_project_1.splash()


def about_press():
    root.destroy()
    os.system("rules.pdf")


def exit_window():
    root.destroy()


# frame1
frame1 = Frame(root, bg="#FF7C35", width=1350, height=100, relief=RIDGE, pady=2, bd=10)
frame1.pack(pady=20)
# title
title_label = Label(frame1, text="Welcome To Tic Tac Toe", font="calibri 80 bold underline", bg="#0d2137", fg="white",
                    justify=CENTER, bd=10, width=25)
title_label.grid(row=1, column=0)

frame2 = Frame(root, bg="#FF7C35", width=1500, height=650, bd=10, relief=RIDGE)
frame2.pack()

left_frame = Frame(frame2, bg="#FF7C35", width=1000, height=800)
left_frame.pack(side=LEFT)

right_frame = Frame(frame2, bg="#FF7C35", relief=RIDGE, width=650, height=500)
right_frame.pack(side=RIGHT, padx=10, pady=5)

# frame2

image = Image.open("main.png")
resize_image = image.resize((500, 500))
img = ImageTk.PhotoImage(resize_image)
label_image = Label(left_frame, image=img, bg="#FF7C35")
label_image.pack()

play_button = Button(right_frame, text="Lets Play Tic Tac Toe!!", font="calibri 35 bold", bg="#0d2137", fg="white",
                     relief=RIDGE, bd=10, command=b_pressed, width=20)
play_button.pack(padx=120, pady=10)
about_button = Button(right_frame, text="About", font="calibri 35 bold", bg="#0d2137", fg="white", relief=RIDGE, bd=10,
                      command=about_press, width=20)
about_button.pack(padx=120, pady=10)
exit_button = Button(right_frame, text="Exit", font="calibri 35 bold", bg="#0d2137", fg="white", relief=RIDGE, bd=10,
                     command=exit_window, width=20)
exit_button.pack(padx=120, pady=10)

root.mainloop()
