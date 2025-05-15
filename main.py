import tkinter as tk

def get_input():
    text = Output.get("1.0", tk.END)



def clear_text():
    Output.delete("1.0", tk.END)




MainWindow = tk.Tk()
MainWindow.geometry("805x800")
MainWindow.resizable(False, False)
Output = tk.Text(MainWindow, height = 25, width = 100 , background = "#161616", foreground = "White")
Output.config(state=tk.DISABLED)
Input = tk.Text(MainWindow, height = 25, width = 100, foreground = "white",background = "#161616")

Output.pack()
Input.pack()
MainWindow.mainloop()
