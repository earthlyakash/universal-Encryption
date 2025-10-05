import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

# Mapping of language names with extensions
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

def encode_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def encode_file():
    file_path = filedialog.askopenfilename(title="Select Code File")
    if not file_path:
        return

    lang = lang_combo.get()
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    binary_content = encode_to_binary(content)

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    save_path = os.path.join(os.path.dirname(file_path), f"{base_name}.bin")

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(binary_content)

    messagebox.showinfo("Success", f"File encoded successfully!\nSaved as: {save_path}\nLanguage selected: {lang}")

# --- UI Setup ---
root = tk.Tk()
root.title("Code Encoder")
root.geometry("500x250")

tk.Label(root, text="Select Programming Language:", font=("Arial", 12)).pack(pady=10)
lang_combo = ttk.Combobox(root, values=list(LANGUAGES.keys()), state="readonly", width=40)
lang_combo.pack()
lang_combo.current(0)

encode_btn = tk.Button(root, text="Encode Code → Binary", command=encode_file, bg="lightblue", width=25)
encode_btn.pack(pady=30)

root.mainloop()
