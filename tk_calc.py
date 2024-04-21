import parser
from tkinter import *
root = Tk()
root.title("Calculator")

entry = Entry(root)
entry.grid(row=1, columnspan=6)
i = 0
def getVariable(num):
    global i
    entry.insert(i, num)
    i += 1
def clearAll():
    entry.delete(0, END)
def undo():
    entireString = entry.get()
    if len(entireString):
        newString = entireString[:-1]
        clearAll()
        entry.insert(0, newString)
    else:
        clearAll()
        entry.insert(0, "Error")
def getOperation(op):
    global i
    length = len(op)
    entry.insert(i,op)
    i = i+length
def calculate():
    entireString = entry.get()
    try:
        expression=parser.expr(entireString).compile()
        result = eval(expression)
        clearAll()
        entry.insert(0,result)
    except :
        clearAll()
        entry.insert(0,"Error")

Button(root, text="1", command=lambda :getVariable(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda :getVariable(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda :getVariable(3)).grid(row=2, column=2)
Button(root, text="<-", command=lambda :undo()).grid(row=2, column=3)

Button(root, text="4", command=lambda :getVariable(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda :getVariable(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda :getVariable(6)).grid(row=3, column=2)
Button(root, text="+", command=lambda :getOperation("+")).grid(row=3, column=3)

Button(root, text="7", command=lambda :getVariable(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda :getVariable(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda :getVariable(9)).grid(row=4, column=2)
Button(root, text="-", command=lambda :getOperation("-")).grid(row=4, column=3)

Button(root, text="0", command=lambda :getVariable(0)).grid(row=5, column=0)
Button(root, text="AC", command=lambda :clearAll()).grid(row=5, column=1)
Button(root, text="*", command=lambda :getOperation("*")).grid(row=5, column=2)
Button(root, text="/", command=lambda :getOperation("/")).grid(row=5, column=3)
root.mainloop()
