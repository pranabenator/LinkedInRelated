import tkinter as tk

def update_logic_operations():
    try:
        state1 = int(state1_var.get())
        state2 = int(state2_var.get())
        if state1 not in [0, 1] or state2 not in [0, 1]:
            raise ValueError("State must be either 0 or 1")
        # Update AND
        and_result_var.set(state1 & state2)
        # Update OR
        or_result_var.set(state1 | state2)
        # Update NOT for State 1 and State 2
        not_result_var.set(f"Not 1: {1 - state1}, Not 2: {1 - state2}")
    except ValueError:
        and_result_var.set("Err")
        or_result_var.set("Err")
        not_result_var.set("Invalid input")

def exit_app():
    root.destroy()

# Setup the root GUI window
root = tk.Tk()
root.title("Logic Gate Simulator")

# Variable setup
state1_var = tk.StringVar()
state2_var = tk.StringVar()
and_result_var = tk.StringVar()
or_result_var = tk.StringVar()
not_result_var = tk.StringVar()

# Layout configurations
labels = ["State 1", "State 2", "AND (State 1, State 2)", "OR (State 1, State 2)", "NOT (State 1, State 2)"]
for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=0, column=i)

# Entry widgets for inputs
tk.Entry(root, textvariable=state1_var, width=10).grid(row=1, column=0)
tk.Entry(root, textvariable=state2_var, width=10).grid(row=1, column=1)

# Labels for results
tk.Label(root, textvariable=and_result_var, width=15).grid(row=1, column=2)
tk.Label(root, textvariable=or_result_var, width=15).grid(row=1, column=3)
tk.Label(root, textvariable=not_result_var, width=20).grid(row=1, column=4)

# Update Button
update_button = tk.Button(root, text="Update", command=update_logic_operations)
update_button.grid(row=2, column=0, columnspan=2)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.grid(row=2, column=4)

# Mainloop
root.mainloop()