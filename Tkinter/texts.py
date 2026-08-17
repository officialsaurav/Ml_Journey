import tkinter as tk


def clear_and_get():
    # "1.0" means line 1, character 0 (the absolute start)
    # tk.END means read all the way to the very last character
    user_story = my_text.get("1.0", tk.END).strip()

    print(f"Submitted Story:\n{user_story}")


root = tk.Tk()
root.geometry("400x300")

# 1. Create the Text widget (width in characters, height in lines of text)
my_text = tk.Text(root, width=40, height=8, font=("Arial", 11))
my_text.pack(pady=15)

# 2. Add a submit button
btn = tk.Button(root, text="Get Text", command=clear_and_get)
btn.pack()

root.mainloop()