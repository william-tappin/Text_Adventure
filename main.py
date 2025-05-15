import tkinter as tk
import time

def GetInput():
    text = Input.get("1.0", tk.END)



def ClearText():
    Input.delete("1.0", tk.END)

CurrentIndex = 0
def TypeText(text):
    global CurrentIndex
    if CurrentIndex < len(text):
        Output.config(state=tk.NORMAL)
        Output.insert(tk.END, text[CurrentIndex])
        CurrentIndex += 1
        MainWindow.after(100,lambda: TypeText(text))  # call again after 50ms


MainWindow = tk.Tk()
MainWindow.geometry("805x800")
MainWindow.resizable(False, False)
Output = tk.Text(MainWindow, height = 25, width = 100 , background = "#161616", foreground = "White")
Output.config(state=tk.DISABLED)
Input = tk.Text(MainWindow, height = 25, width = 100, foreground = "white",background = "#161616")

Output.pack()
Input.pack()

TypeText(string)
MainWindow.mainloop()

