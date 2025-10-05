import tkinter as tk
from tkinter import filedialog, messagebox
import os, random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*-_=+"
TOKEN_LEN = 8

# Fixed mapping
random.seed(123456789)
mapping_dec, used = {}, set()
for b in range(256):
    while True:
        token = ''.join(random.choice(ALPHABET) for _ in range(TOKEN_LEN))
        if token not in used:
            used.add(token)
            mapping_dec[token] = b
            break

def decrypt_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    try:
        ext, enc_text = text.split("||", 1)
    except ValueError:
        raise ValueError("Invalid encrypted file format.")
    if len(enc_text) % TOKEN_LEN != 0:
        raise ValueError("Corrupted file.")
    out = bytearray()
    for i in range(0, len(enc_text), TOKEN_LEN):
        token = enc_text[i:i+TOKEN_LEN]
        if token not in mapping_dec:
            raise ValueError("Corrupted or wrong algorithm.")
        out.append(mapping_dec[token])
    out_path = os.path.splitext(path)[0] + ext
    with open(out_path, "wb") as f:
        f.write(out)
    return out_path

def decrypt_action():
    file = filedialog.askopenfilename(title="Select .enc file", filetypes=[("Encoded", "*.enc")])
    if not file: return
    try:
        out = decrypt_file(file)
        messagebox.showinfo("Success", f"Decrypted file saved:\n{out}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- UI ---
root = tk.Tk()
root.title("Decrypt File")
root.geometry("320x140")

tk.Button(root, text="Select .enc & Decrypt", command=decrypt_action, bg="lightgreen", width=25).pack(pady=40)

root.mainloop()
