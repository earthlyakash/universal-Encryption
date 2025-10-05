import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

LANGUAGES = {
    "C (.c)": ".c",
    "C Header (.h)": ".h",
    "C++ (.cpp)": ".cpp",
    "C++ (.cc)": ".cc",
    "C++ (.cxx)": ".cxx",
    "C++ Header (.hpp)": ".hpp",
    "C# (.cs)": ".cs",
    "Java (.java)": ".java",
    "Kotlin (.kt)": ".kt",
    "Scala (.scala)": ".scala",
    "Groovy (.groovy)": ".groovy",
    "Clojure (.clj)": ".clj",
    "Swift (.swift)": ".swift",
    "Go (.go)": ".go",
    "Rust (.rs)": ".rs",
    "Objective-C (.m)": ".m",
    "Objective-C++ (.mm)": ".mm",
    "Pascal (.pas)": ".pas",
    "Fortran (.f90)": ".f90",
    "Ada (.adb)": ".adb",
    "D (.d)": ".d",
    "VB (.vb)": ".vb",
    "Python (.py)": ".py",
    "IPython Notebook (.ipynb)": ".ipynb",
    "JavaScript (.js)": ".js",
    "TypeScript (.ts)": ".ts",
    "React JSX (.jsx)": ".jsx",
    "React TSX (.tsx)": ".tsx",
    "PHP (.php)": ".php",
    "Ruby (.rb)": ".rb",
    "Perl (.pl)": ".pl",
    "Lua (.lua)": ".lua",
    "R (.r)": ".r",
    "Julia (.jl)": ".jl",
    "Matlab (.mat)": ".mat",
    "SAS (.sas)": ".sas",
    "Haskell (.hs)": ".hs",
    "Lisp (.lisp)": ".lisp",
    "OCaml (.ml)": ".ml",
    "F# (.fs)": ".fs",
    "Elixir (.ex)": ".ex",
    "Erlang (.erl)": ".erl",
    "Prolog (.pro)": ".pro",
    "SQL (.sql)": ".sql",
    "GraphQL (.graphql)": ".graphql",
    "HTML (.html)": ".html",
    "CSS (.css)": ".css",
    "XML (.xml)": ".xml",
    "JSON (.json)": ".json",
    "YAML (.yaml)": ".yaml",
    "Markdown (.md)": ".md",
    "LaTeX (.tex)": ".tex",
    "Assembly (.asm)": ".asm",
    "Verilog (.v)": ".v",
    "CUDA (.cu)": ".cu",
    "Shell Script (.sh)": ".sh",
    "PowerShell (.ps1)": ".ps1",
    "Batch (.bat)": ".bat",
    "INI (.ini)": ".ini",
    "Config (.cfg)": ".cfg",
    "Dockerfile (.dockerfile)": ".dockerfile",
    "Makefile (.mk)": ".mk",
    "Maya MEL (.mel)": ".mel",
    "Maya ASCII (.ma)": ".ma",
    "Maya Binary (.mb)": ".mb",
    "Cinema4D (.c4d)": ".c4d",
    "3D Studio Max Script (.ms)": ".ms",
    "SketchUp (.skp)": ".skp",
    "Smalltalk (.st)": ".st",
    "Dart (.dart)": ".dart",
    "ABAP (.abap)": ".abap",
    "Solidity (.sol)": ".sol",
    "Vyper (.vy)": ".vy",
    "COBOL (.cob)": ".cob",
}

def decode_from_binary(binary_text):
    try:
        binary_values = binary_text.split()
        ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
        return ''.join(ascii_characters)
    except Exception:
        return None

def decode_file():
    file_path = filedialog.askopenfilename(title="Select Binary File", filetypes=[("Binary Files", "*.bin")])
    if not file_path:
        return

    lang = lang_combo.get()
    ext = LANGUAGES[lang]

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        binary_content = f.read()

    decoded_content = decode_from_binary(binary_content)
    if decoded_content is None:
        messagebox.showerror("Error", "Invalid binary file format.")
        return

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    save_path = os.path.join(os.path.dirname(file_path), f"{base_name}{ext}")

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(decoded_content)

    messagebox.showinfo("Success", f"Binary decoded successfully!\nSaved as: {save_path}\nLanguage selected: {lang}")

# --- UI Setup ---
root = tk.Tk()
root.title("Code Decoder")
root.geometry("500x250")

tk.Label(root, text="Select Programming Language:", font=("Arial", 12)).pack(pady=10)
lang_combo = ttk.Combobox(root, values=list(LANGUAGES.keys()), state="readonly", width=40)
lang_combo.pack()
lang_combo.current(0)

decode_btn = tk.Button(root, text="Decode Binary → Code", command=decode_file, bg="lightgreen", width=25)
decode_btn.pack(pady=30)

root.mainloop()
