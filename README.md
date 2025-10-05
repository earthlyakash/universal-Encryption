# Only Binary System & Pure Encryption System

## Overview

This repository contains two advanced Python projects designed for code manipulation, binary encoding, and secure file encryption. Both projects feature interactive GUI interfaces built with Tkinter, providing users with an intuitive and powerful experience.

1. **Only Binary System** – An encoder and decoder for programming code files that converts code to binary and back.
2. **Pure Encryption System** – A secure, token-based encryption and decryption system for any file type.

These projects aim to enhance understanding of binary encoding, file security, and GUI programming while providing practical tools for developers, students, and hobbyists.

---

## Project 1: Only Binary System

### Description

**Only Binary System** is a Python project for encoding and decoding programming code files into binary format. It is useful for:

* Learning binary representation of text/code.
* Securely transmitting code in binary format.
* Experimenting with encoding and decoding algorithms.

The project supports a wide range of programming languages and provides a real-time binary display for live typing.

### Features

1. **Binary Encoder**

   * Converts text/code into 8-bit space-separated binary.
   * Supports live updates as users type.
   * Saves output as `.bin` files.

2. **Binary Decoder**

   * Converts binary `.bin` files back to readable code.
   * Automatically restores the correct file extension based on user-selected language.

3. **Multi-Language Support**

   * Supports 50+ programming languages including Python, C++, Java, JavaScript, Rust, PHP, HTML, CSS, and more.

4. **User-Friendly GUI**

   * Tkinter-based interface with side-by-side text and binary display.
   * Easy load and save operations.

### Technical Details

**Encoding:**

* Each character is converted to an 8-bit binary using `format(ord(char), '08b')`.
* Binary strings are space-separated and displayed in real-time.

**Decoding:**

* Binary strings are split into 8-bit chunks.
* Each chunk is converted back to a character using `chr(int(binary, 2))`.
* File is saved with the appropriate language extension.

### Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/username/only-binary-system.git
cd only-binary-system
```

2. Ensure Python 3.8+ is installed.
3. Run the scripts:

```bash
python encoder.py      # Encode code to binary
python decoder.py       # Decode binary to code
python textEditor.py   # Dual live binary editor
```

4. Use the GUI to select the language, input code, and save binary files.

---

## Project 2: Pure Encryption System

### Description

**Pure Encryption System** is a secure Python project that encrypts and decrypts files using a custom **token-based mapping algorithm**. It is designed for:

* Protecting files by converting them to a secure `.enc` format.
* Learning the principles of symmetric encryption.
* Experimenting with deterministic mapping encryption algorithms.

### Features

1. **Custom Token-Based Encryption**

   * Each byte (0–255) maps to a unique 8-character token.
   * Deterministic mapping using a fixed random seed ensures consistency.

2. **File Extension Preservation**

   * Original file extensions are stored in the encrypted file and restored upon decryption.

3. **Error Detection**

   * Detects corrupted or invalid encrypted files.
   * Ensures only valid tokens are decrypted.

4. **Simple GUI**

   * Tkinter interface with buttons for encrypting and decrypting files.

### Technical Details

**Encryption:**

* Read the file as bytes.
* Each byte is replaced with its corresponding 8-character token.
* Original file extension is prepended and saved as `.enc`.

**Decryption:**

* Read the `.enc` file and split the stored extension from token sequences.
* Convert each token back to its corresponding byte.
* Save the decrypted file with the correct extension.

### Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/username/pure-encryption-system.git
cd pure-encryption-system
```

2. Ensure Python 3.8+ is installed.
3. Run the scripts:

```bash
python encrypt.py   # Encrypt files
python decrypt.py   # Decrypt .enc files
```

4. Use the GUI to select files and perform encryption or decryption.

### Security Notes

* Deterministic encryption is used with a fixed seed.
* Suitable for educational or personal use.
* Not recommended for highly sensitive data in production.

---

## Combined Benefits

By combining **Only Binary System** and **Pure Encryption System**, users can:

* Learn binary encoding and custom encryption simultaneously.
* Experiment with Python GUI programming.
* Securely encode, encrypt, and transmit files or code.
* Extend the projects for more languages, stronger encryption, and enhanced GUI features.

---

## Requirements

* Python 3.8+
* Tkinter (standard with Python)
* Windows / Linux / macOS

---

## Contribution

Contributions, bug reports, and suggestions are welcome. Potential enhancements:

* Support more languages in Only Binary System.
* Improve encryption strength with dynamic tokens and randomness.
* Enhance GUI for better user experience.

---

## License

This repository is **open-source** and License free.
