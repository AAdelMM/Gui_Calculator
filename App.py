import tkinter as tk


calculation = ""

#write on the screen
def write_to_screen(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

#clear screen
def clear_screen():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

#get result
def calculation_result():
    #addition
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calculation)
        #addition
        calculation=""
    except:
        clear_screen()
        text_result.insert(1.0,"Error")

#create screen
screen = tk.Tk()
#addition
screen.title("My_Calculator")
screen.geometry("300x275")
text_result = tk.Text(screen, height=2, width=16,font=("Arial",24))
text_result.grid(columnspan=5)

#creat buttons
btn_1 = tk.Button(screen, text="1", command=lambda: write_to_screen(1),width=5,font=("Arial",14))
btn_1.grid(row=2,column=1)
btn_2 = tk.Button(screen, text="2", command=lambda: write_to_screen(2),width=5,font=("Arial",14))
btn_2.grid(row=2,column=2)
btn_3 = tk.Button(screen, text="3", command=lambda: write_to_screen(3),width=5,font=("Arial",14))
btn_3.grid(row=2,column=3)
btn_4 = tk.Button(screen, text="4", command=lambda: write_to_screen(4),width=5,font=("Arial",14))
btn_4.grid(row=3,column=1)
btn_5 = tk.Button(screen, text="5", command=lambda: write_to_screen(5),width=5,font=("Arial",14))
btn_5.grid(row=3,column=2)
btn_6 = tk.Button(screen, text="6", command=lambda: write_to_screen(6),width=5,font=("Arial",14))
btn_6.grid(row=3,column=3)
btn_7 = tk.Button(screen, text="7", command=lambda: write_to_screen(7),width=5,font=("Arial",14))
btn_7.grid(row=4,column=1)
btn_8 = tk.Button(screen, text="8", command=lambda: write_to_screen(8),width=5,font=("Arial",14))
btn_8.grid(row=4,column=2)
btn_9 = tk.Button(screen, text="9", command=lambda: write_to_screen(9),width=5,font=("Arial",14))
btn_9.grid(row=4,column=3)
btn_0 = tk.Button(screen, text="0", command=lambda: write_to_screen(0),width=5,font=("Arial",14))
btn_0.grid(row=5,column=2)
btn_plus = tk.Button(screen, text="+", command=lambda: write_to_screen("+"),width=5,font=("Arial",14))
btn_plus.grid(row=2,column=4)
btn_minus = tk.Button(screen, text="-", command=lambda: write_to_screen("-"),width=5,font=("Arial",14))
btn_minus.grid(row=3,column=4)
btn_mul = tk.Button(screen, text="x", command=lambda: write_to_screen("*"),width=5,font=("Arial",14))
btn_mul.grid(row=4,column=4)
btn_div = tk.Button(screen, text="/", command=lambda: write_to_screen("/"),width=5,font=("Arial",14))
btn_div.grid(row=5,column=4)
btn_open= tk.Button(screen, text="(", command=lambda: write_to_screen("("),width=5,font=("Arial",14))
btn_open.grid(row=5,column=1)
btn_close = tk.Button(screen, text=")", command=lambda: write_to_screen(")"),width=5,font=("Arial",14))
btn_close.grid(row=5,column=3)
btn_equal = tk.Button(screen, text="=", command= calculation_result,width=10,font=("Arial",14))
btn_equal.grid(row=6,column=1,columnspan=2)
btn_clear = tk.Button(screen, text="C", command= clear_screen,width=10,font=("Arial",14))
btn_clear.grid(row=6,column=3, columnspan=2)
screen.mainloop()
