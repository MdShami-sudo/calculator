import tkinter as tk

root = tk.Tk()
root.title("Neon Calculator with Emojis")
root.config(bg="#282828")  

neon_fg = "#39ff14"
button_bg = "#282828"
button_active_bg = "#404040"

emojis = {
    '+': '😊',
    '-': '😢',
    '*': '💪',
    '/': '🧐',
    '0': '0️⃣',
    '1': '1️⃣',
    '2': '2️⃣',
    '3': '3️⃣',
    '4': '4️⃣',
    '5': '5️⃣',
    '6': '6️⃣',
    '7': '7️⃣',
    '8': '8️⃣',
    '9': '9️⃣',
    '=': '🤔',
    'C': '💥',
}

def button_click(symbol):
    current = entry.get()
    if symbol == 'C':
        entry.delete(0, tk.END)
    elif symbol == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, symbol)

entry = tk.Entry(root, font=("Helvetica", 24), bd=10, insertwidth=4, width=14, borderwidth=4, fg=neon_fg, bg=button_bg)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: button_click(x)
    btn = tk.Button(root, text=emojis[button], padx=20, pady=20, font=("Helvetica", 24),
                    bg=button_bg, fg=neon_fg, activebackground=button_active_bg, command=action)
    btn.grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()
