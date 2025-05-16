import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def process():
    text = entry_text.get("1.0", tk.END).strip()
    shift = int(entry_shift.get())

    if var.get() == "Encrypt":
        result = encrypt(text, shift)
    else:
        result = decrypt(text, shift)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def save_to_file():
    message = output_text.get("1.0", tk.END).strip()
    if message:
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt")])
        if filepath:
            with open(filepath, "w") as file:
                file.write(message)
            messagebox.showinfo("Saved", f"Message saved to {filepath}")
    else:
        messagebox.showwarning("Empty", "There is nothing to save.")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher GUI")

# Mode (Encrypt/Decrypt)
var = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=var, value="Encrypt").grid(row=0, column=0, sticky="w")
tk.Radiobutton(root, text="Decrypt", variable=var, value="Decrypt").grid(row=0, column=1, sticky="w")

# Input
tk.Label(root, text="Enter Text:").grid(row=1, column=0, sticky="w")
entry_text = tk.Text(root, height=5, width=50)
entry_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

tk.Label(root, text="Shift:").grid(row=3, column=0, sticky="w")
entry_shift = tk.Entry(root)
entry_shift.grid(row=3, column=1, sticky="w")

# Buttons
tk.Button(root, text="Process", command=process).grid(row=4, column=0, pady=5)
tk.Button(root, text="Save to File", command=save_to_file).grid(row=4, column=1, pady=5)

# Output
tk.Label(root, text="Output:").grid(row=5, column=0, sticky="w")
output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
