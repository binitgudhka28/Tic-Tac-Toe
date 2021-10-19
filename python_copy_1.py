from tkinter import *
from tkinter import messagebox
from tkinter import font
from playsound import playsound
import os
from PIL import Image, ImageTk
from tqdm import tqdm

click = True
count = 0
winner = False


def splash():
    splash_sk = Tk()
    splash_sk.title("Tic Tac Toe")
    splash_sk.geometry("1920x1080")
    splash_sk.configure(bg="#FF7C35")

    info1_label_1 = Label(splash_sk, text="initializing....", font="calibri 50 bold", width=100, bg="#FF7C35",
                          fg="black")
    info1_label_1.pack(pady=200)

    def main_code():
        splash_sk.destroy()

        root = Tk()
        root.geometry("1920x1080")
        root.title("Tic Tac Toe")
        root["bg"] = "#FF7C35"

        # frame1
        frame1 = Frame(root, bg="#C7CEEA", width=1350, height=100, relief=RIDGE, pady=2, bd=10)
        frame1.pack(pady=20)
        # title
        title_label = Label(frame1, text="Tic Tac Toe", font="calibri 80 bold", bg="#0d2137", fg="white",
                            justify=CENTER, bd=10, width=25)
        title_label.grid(row=1, column=0)

        # frame2
        frame2 = Frame(root, bg="#0d2137", width=1350, height=550, bd=10)
        frame2.pack()

        # right frame
        left_frame = Frame(frame2, bg="#FF7C35", relief=RIDGE, width=1000, height=800, bd=10)
        left_frame.pack(side=LEFT, padx=10, pady=5)

        right_frame = Frame(frame2, bg="#FF7C35", relief=RIDGE, width=560, height=500, bd=10)
        right_frame.pack(side=RIGHT, padx=10, pady=5)

        right_frame_1 = Frame(right_frame, bg="#0d2137", relief=RIDGE, width=560, height=200, bd=10)
        right_frame_1.grid(row=0, column=0, padx=10, pady=5)

        right_frame_2 = Frame(right_frame, bg="#0d2137", relief=RIDGE, width=560, height=200, bd=10)
        right_frame_2.grid(row=1, column=0, padx=10, pady=5)

        right_frame = Frame(frame2, bg="#FF8E2B", relief=RIDGE)
        right_frame.pack(side=LEFT, padx=10, pady=5)

        PlayerX = IntVar()
        PlayerO = IntVar()

        buttons = StringVar()

        # check to see if someone won
        def check():
            global winner
            global count
            winner = False

            if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
                button1.config(bg="red")
                button2.config(bg="red")
                button3.config(bg="red")
                winner = True
                n = int(PlayerX.get())
                score = n + 1
                PlayerX.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n X wins ")

            elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
                button4.config(bg="red")
                button5.config(bg="red")
                button6.config(bg="red")
                winner = True
                n = int(PlayerX.get())
                score = n + 1
                PlayerX.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n X wins ")


            elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
                button7.config(bg="red")
                button8.config(bg="red")
                button9.config(bg="red")
                winner = True
                n = int(PlayerX.get())
                score = n + 1
                PlayerX.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n X wins ")

            elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
                button1.config(bg="red")
                button4.config(bg="red")
                button7.config(bg="red")
                winner = True
                n = int(PlayerX.get())
                score = n + 1
                PlayerX.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n X wins ")

            elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
                button2.config(bg="red")
                button5.config(bg="red")
                button8.config(bg="red")
                winner = True
                n = int(PlayerX.get())
                score = n + 1
                PlayerX.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n X wins ")

            elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
                button3.config(bg="red")
                button6.config(bg="red")
                button9.config(bg="red")
                winner = True
                n = int(PlayerX.get())
                score = n + 1
                PlayerX.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n X wins ")

            elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
                button1.config(bg="red")
                button5.config(bg="red")
                button9.config(bg="red")
                winner = True
                n = int(PlayerX.get())
                score = n + 1
                PlayerX.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n X wins ")

            elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
                button3.config(bg="red")
                button5.config(bg="red")
                button7.config(bg="red")
                winner = True
                n = int(PlayerX.get())
                score = n + 1
                PlayerX.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n X wins ")

            # winners with O

            elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
                button1.config(bg="red")
                button2.config(bg="red")
                button3.config(bg="red")
                winner = True
                n = int(PlayerO.get())
                score = n + 1
                PlayerO.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n O wins ")

            elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
                button4.config(bg="red")
                button5.config(bg="red")
                button6.config(bg="red")
                winner = True
                n = int(PlayerO.get())
                score = n + 1
                PlayerO.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n O wins ")

            elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
                button7.config(bg="red")
                button8.config(bg="red")
                button9.config(bg="red")
                winner = True
                n = int(PlayerO.get())
                score = n + 1
                PlayerO.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n O wins ")

            elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
                button1.config(bg="red")
                button4.config(bg="red")
                button7.config(bg="red")
                winner = True
                n = int(PlayerO.get())
                score = n + 1
                PlayerO.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n O wins ")

            elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
                button2.config(bg="red")
                button5.config(bg="red")
                button8.config(bg="red")
                winner = True
                n = int(PlayerO.get())
                score = n + 1
                PlayerO.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n O wins ")

            elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
                button3.config(bg="red")
                button6.config(bg="red")
                button9.config(bg="red")
                winner = True
                n = int(PlayerO.get())
                score = n + 1
                PlayerO.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n O wins ")

            elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
                button1.config(bg="red")
                button5.config(bg="red")
                button9.config(bg="red")
                winner = True
                n = int(PlayerO.get())
                score = n + 1
                PlayerO.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n O wins ")

            elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
                button3.config(bg="red")
                button5.config(bg="red")
                button7.config(bg="red")
                winner = True
                n = int(PlayerO.get())
                score = n + 1
                PlayerO.set(score)
                messagebox.showinfo("Tic Tac Toe", "Congratulations!!\n O wins ")

            # check if ties
            if count == 9 and winner == False:
                messagebox.showinfo("Tic Tac Toe", "Its a Tie\nNo One Wins!!")

        # Button click Function
        def b_click(b):
            global click, count
            if b["text"] == " " and click == True:
                b["text"] = "X"

                click = False
                count += 1  # or count=count+1
                check()

            elif b["text"] == " " and click == False:
                b["text"] = "O"

                click = True
                count += 1  # or count=count+1
                check()

            else:
                messagebox.showerror("Tic Tac Toe", "Oops!! This Buttion Is Already Selected\nPick Another Box.......")

        def reset_game():
            global count
            global click
            count = 0
            click = True
            button1["text"] = " "
            button2["text"] = " "
            button3["text"] = " "
            button4["text"] = " "
            button5["text"] = " "
            button6["text"] = " "
            button7["text"] = " "
            button8["text"] = " "
            button9["text"] = " "

            button1.configure(background="white")
            button2.configure(background="white")
            button3.configure(background="white")
            button4.configure(background="white")
            button5.configure(background="white")
            button6.configure(background="white")
            button7.configure(background="white")
            button8.configure(background="white")
            button9.configure(background="white")

        def new_game():
            reset_game()
            PlayerO.set(0)
            PlayerX.set(0)

        def exit():
            root.destroy()

        PlayerX.set(0)
        PlayerO.set(0)

        button1 = Button(left_frame, text=" ", font=("ArialNovaLight", 20), height=3, width=6, bg="white",
                         borderwidth=10, command=lambda: b_click(button1))
        button2 = Button(left_frame, text=" ", font=("ArialNovaLight", 20), height=3, width=6, bg="white",
                         borderwidth=10, command=lambda: b_click(button2))
        button3 = Button(left_frame, text=" ", font=("ArialNovaLight", 20), height=3, width=6, bg="white",
                         borderwidth=10, command=lambda: b_click(button3))

        button4 = Button(left_frame, text=" ", font=("ArialNovaLight", 20), height=3, width=6, bg="white",
                         borderwidth=10, command=lambda: b_click(button4))
        button5 = Button(left_frame, text=" ", font=("ArialNovaLight", 20), height=3, width=6, bg="white",
                         borderwidth=10, command=lambda: b_click(button5))
        button6 = Button(left_frame, text=" ", font=("ArialNovaLight", 20), height=3, width=6, bg="white",
                         borderwidth=10, command=lambda: b_click(button6))

        button7 = Button(left_frame, text=" ", font=("ArialNovaLight", 20), height=3, width=6, bg="white",
                         borderwidth=10, command=lambda: b_click(button7))
        button8 = Button(left_frame, text=" ", font=("ArialNovaLight", 20), height=3, width=6, bg="white",
                         borderwidth=10, command=lambda: b_click(button8))
        button9 = Button(left_frame, text=" ", font=("ArialNovaLight", 20), height=3, width=6, bg="white",
                         borderwidth=10, command=lambda: b_click(button9))

        button1.grid(row=0, column=0)
        button2.grid(row=0, column=1)
        button3.grid(row=0, column=2)

        button4.grid(row=1, column=0)
        button5.grid(row=1, column=1)
        button6.grid(row=1, column=2)

        button7.grid(row=2, column=0)
        button8.grid(row=2, column=1)
        button9.grid(row=2, column=2)

        player_x_label = Label(right_frame_1, text="Player X:", font="arial 40 bold", padx=2, pady=2, fg="white",
                               bg="#0d2137")
        player_x_label.grid(row=0, column=0)
        player_x_entry = Entry(right_frame_1, font="arial 40 bold", textvariable=PlayerX)
        player_x_entry.grid(row=0, column=1)

        player_o_label = Label(right_frame_1, text="Player O:", font="arial 40 bold", padx=2, pady=2, fg="white",
                               bg="#0d2137")
        player_o_label.grid(row=2, column=0)
        player_o_entry = Entry(right_frame_1, font="arial 40 bold", textvariable=PlayerO)
        player_o_entry.grid(row=2, column=1)

        # reset game
        reset_game_button = Button(right_frame_2, text="Reset Game", font="arial 26 bold", bg="white", height=1,
                                   width=20, command=reset_game)
        reset_game_button.grid(row=0, column=0, padx=6, pady=10)

        # new game
        new_game_button = Button(right_frame_2, text="New Game", font="arial 26 bold", bg="white", height=1, width=20,
                                 command=new_game)
        new_game_button.grid(row=2, column=0, padx=6, pady=10)

        # exit game
        exit_button = Button(right_frame_2, text="Exit", font="arial 26 bold", bg="white", height=1, width=20,
                             command=exit)
        exit_button.grid(row=3, column=0, padx=6, pady=10)

    splash_sk.after(7000, main_code)

    mainloop()