import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox

# Supported languages
LANGUAGES = {
    "Python (.py)": ".py",
    "JavaScript (.js)": ".js",
    "React JSX (.jsx)": ".jsx",
    "C (.c)": ".c",
    "C++ (.cpp)": ".cpp",
    "Java (.java)": ".java",
}

plain_text = ""  # store actual typed text

def encode_to_binary(text):
    """Convert text to space-separated 8-bit binary."""
    return ' '.join(format(ord(c), '08b') for c in text)

def on_text_change(event=None):
    """Update binary display when real text changes."""
    global plain_text
    plain_text = real_text.get("1.0", tk.END)[:-1]  # remove last newline
    binary_content = encode_to_binary(plain_text)
    binary_display.config(state="normal")
    binary_display.delete("1.0", tk.END)
    binary_display.insert(tk.END, binary_content)
    binary_display.config(state="disabled")

def save_binary_file():
    """Save only binary content to a .bin file."""
    if not plain_text.strip():
        messagebox.showwarning("Empty", "Nothing to save!")
        return

    lang = lang_combo.get()
    ext = LANGUAGES.get(lang, ".txt")
    default_name = f"output.bin"

    save_path = filedialog.asksaveasfilename(
        defaultextension=".bin",
        initialfile=default_name,
        filetypes=[("Binary Files", "*.bin")]
    )
    if save_path:
        try:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(encode_to_binary(plain_text))
            messagebox.showinfo("Saved", f"Binary file saved:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")

# --- UI Setup ---
root = tk.Tk()
root.title("Dual Live Binary Writer")
root.geometry("1000x700")  # initial size

# Language selector at top
tk.Label(root, text="Select Programming Language:", font=("Arial", 12)).pack(pady=5)
lang_combo = ttk.Combobox(root, values=list(LANGUAGES.keys()), state="readonly", width=25)
lang_combo.pack()
lang_combo.current(0)

# Main frame for side-by-side text areas
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Left: real text (smaller)
left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0,10))
tk.Label(left_frame, text="Write Here:", font=("Arial", 10)).pack(anchor="w")
real_text = scrolledtext.ScrolledText(left_frame, width=40, height=35, font=("Arial", 10))
real_text.pack(fill=tk.Y, expand=True)
real_text.bind("<KeyRelease>", on_text_change)

# Right: binary display (bigger)
right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
tk.Label(right_frame, text="Binary Output:", font=("Arial", 10)).pack(anchor="w")
binary_display = scrolledtext.ScrolledText(right_frame, font=("Courier", 10))
binary_display.pack(fill=tk.BOTH, expand=True)
binary_display.config(state="disabled")

# Save button below
save_btn = tk.Button(root, text="Save Binary File", bg="lightgreen", width=25, command=save_binary_file)
save_btn.pack(pady=10)

root.mainloop()
