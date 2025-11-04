import tkinter as tk

def on_click():
    label.config(text="hello"+entry.get()+""
                 )
    

root=tk.Tk()

root.title("my first app")
root.geometry("300*200")


label=tk.Label(root,text="enter you name")
label.pack(pady=10)


entry=tk.Entry(root)
entry.pack()

button=tk.Button(root,text="greet",command=on_click)
button.pack(padx=10)

root.mainloop()
