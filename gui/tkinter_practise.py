import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, askyesno
import tkinter.ttk as ttk

window = tk.Tk()
window.title("practise page for tkinter")
window.geometry('600x400')
window.resizable(False, True)
name = tk.StringVar(value="")
heading = tk.Label(window, text="Hello World!")
name_box = ttk.Entry(window, textvariable=name, width=50)
heading.pack()
name_box.pack()
name_box.focus()

def name_given():
    name = name_box.get()
    name_box.delete(0, tk.END)
    tk.Label(window, text=f"I have greeted {name}!").pack()
    showinfo(
        title='Greeting',
        message=f"Hello {name}!"
    )
    heading["text"] = f"Hello {name}!! Thank you for introducing yourself!"

def exit_button():
    response = askyesno(
        title='Is this the end?',
        message="Are you really going to end this?"
    )
    if response:
        window.destroy()

button1 = tk.Button(window, text="submit name", bg="blue", command=name_given)
button1.pack()
button2 = tk.Button(window, text="close the app", bg="red", command=exit_button)
button2.pack(side="bottom")



# counter 
counter = tk.Frame()

counter.rowconfigure(0, minsize=50, weight=1)
counter.columnconfigure([0, 1, 2], minsize=50, weight=1)

counter_value = 0
lbl_value = tk.Label(master=counter, text=counter_value)
lbl_value.grid(row=0, column=1)

def increment():
    lbl_value["text"] += 1
def decrement():
    lbl_value["text"] -= 1
btn_decrease = tk.Button(master=counter, text="-", command=decrement)
btn_decrease.grid(row=0, column=0, sticky="nsew")

btn_increase = tk.Button(master=counter, text="+", command=increment)
btn_increase.grid(row=0, column=2, sticky="nsew")
counter.pack()

window.mainloop()
