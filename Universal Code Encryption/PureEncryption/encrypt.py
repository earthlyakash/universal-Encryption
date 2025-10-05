import tkinter as tk
from tkinter import filedialog, messagebox
import os, random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*-_=+"
TOKEN_LEN = 8

# Fixed mapping
random.seed(123456789)
mapping_enc, used = {}, set()
for b in range(256):
    while True:
        token = ''.join(random.choice(ALPHABET) for _ in range(TOKEN_LEN))
        if token not in used:
            used.add(token)
            mapping_enc[b] = token
            break

def encrypt_file(path):
    ext = os.path.splitext(path)[1] or ".bin"  # save extension
    with open(path, "rb") as f:
        data = f.read()
    enc_text = ''.join(mapping_enc[b] for b in data)
    out_path = os.path.splitext(path)[0] + ".enc"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ext + "||" + enc_text)  # extension + encrypted content
    return out_path

def encrypt_action():
    file = filedialog.askopenfilename(title="Select file to Encrypt")
    if not file: return
    try:
        out = encrypt_file(file)
        messagebox.showinfo("Success", f"Encrypted file saved:\n{out}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- UI ---
root = tk.Tk()
root.title("Encrypt File")
root.geometry("320x140")

tk.Button(root, text="Select File & Encrypt", command=encrypt_action, bg="lightblue", width=25).pack(pady=40)

root.mainloop()
