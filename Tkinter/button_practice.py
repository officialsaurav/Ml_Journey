import tkinter as tk


def check_status():
    # .get() retrieves True if checked, False if unchecked
    if terms_var.get():
        print("User accepted the terms.")
    else:
        print("User did NOT accept the terms.")


root = tk.Tk()
root.geometry("300x150")

# 1. Create a Tkinter variable to track the state
terms_var = tk.BooleanVar()

# 2. Create the Checkbutton and link it to the variable
check_btn = tk.Checkbutton(
    root,
    text="I agree to the terms",
    variable=terms_var,
)
check_btn.pack(pady=15)

# 3. Create a button to check the state
submit_btn = tk.Button(root, text="Submit", command=check_status)
submit_btn.pack()

root.mainloop()