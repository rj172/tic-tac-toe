from Tkinter import *
import tkMessageBox
import tkFont
root = Tk()

root.title("Tic-Tac-Toe")
helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
click = True

def clear():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

 
def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and click==False:
        buttons["text"] = "O"
        click = True
    
    if (button1["text"]!=" " and button2["text"]!=" " and button3["text"]!=" " and
        button5["text"]!=" " and button4["text"]!=" " and 
        button6["text"]!=" " and button7["text"]!=" " and button8["text"]!=" " and button9["text"]!=" "):
        tkMessageBox.showinfo("Draw" , "It is a Draw")
                            
    elif (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
    button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
    button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
    button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
    button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
    button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
    button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
    button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" ):
        
        tkMessageBox.showinfo("Winner X" , "You have just won the game")        


    elif (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
    button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
    button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
    button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
    button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
    button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
    button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
    button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" 
    ):
        
        tkMessageBox.showinfo("Winner O" , "You have just won the game")


buttons  = StringVar

button1 = Button(root , text = " ", height = 6 , width =12 ,font=helv36, command = lambda : checker(button1))
button1.grid(row = 0 , column = 0,sticky = S+N+E+W)

button2 = Button(root , text = " ", height = 6 , width =12 ,font=helv36, command = lambda : checker(button2))
button2.grid(row = 0 , column = 1,sticky = S+N+E+W)

button3 = Button(root , text = " ", height = 6 , width =12 ,font=helv36, command = lambda : checker(button3))
button3.grid(row = 0 , column = 2,sticky = S+N+E+W)

button4 = Button(root , text = " ", height = 6 , width =12,font=helv36 , command = lambda : checker(button4))
button4.grid(row = 1 , column = 0,sticky = S+N+E+W)

button5 = Button(root , text = " ", height = 6 , width =12 ,font=helv36, command = lambda : checker(button5))
button5.grid(row = 1 , column = 1,sticky = S+N+E+W)

button6 = Button(root , text = " ", height = 6 , width =12,font=helv36 , command = lambda : checker(button6))
button6.grid(row = 1 , column = 2,sticky = S+N+E+W)

button7 = Button(root , text = " ", height = 6 , width =12,font=helv36 , command = lambda : checker(button7))
button7.grid(row = 2 , column = 0,sticky = S+N+E+W)

button8 = Button(root , text = " ", height = 6 , width =12,font=helv36 , command = lambda : checker(button8))
button8.grid(row = 2 , column = 1,sticky = S+N+E+W)

button9 = Button(root , text = " ", height = 6 , width =12 ,font=helv36, command = lambda : checker(button9))
button9.grid(row = 2 , column = 2,sticky = S+N+E+W)

clearbutton = Button(root  , text = "reset", width = 6 ,activebackground = "blue",bg="red", height = 2  ,command = lambda : clear())
clearbutton.grid(row = 3 , column =1 , sticky = S+N+E+W)

root.grid_rowconfigure((0,1,2), weight=1)
root.grid_columnconfigure((0,1,2), weight=1) 


root.mainloop()