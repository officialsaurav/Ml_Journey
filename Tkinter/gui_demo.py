import tkinter as tk

def summit():
    print("Button Clicked")


root=tk.Tk()
root.title("Gui demo")
root.geometry("400x500")


label=tk.Label(root,text="Hi this is label ")
label.pack()

entry=tk.Entry(root)
entry.pack()
text=tk.Text(root, height = 20)
text.pack()


check=tk.Checkbutton(root,text="i am the button")
check.pack()

button=tk.Button(root,text="sumit",command=summit)
button.pack()


root.mainloop()
