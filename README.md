# 🔐 Advanced Cryptographic System — Python OOP

A comprehensive cryptographic application built using **Object-Oriented Programming (OOP)** principles in Python. This project demonstrates various encryption, decryption, and hashing techniques, fulfilling the requirements for the **Advanced Programming Project**.

---

## 📑 Project Overview

This system provides two interfaces for performing cryptographic operations:
1.  **Console Interface:** A robust menu-driven CLI (Command Line Interface) with full exception handling.
2.  **Web Interface:** A modern, interactive web application built with **Flask**, **HTML5**, and **CSS3**.

### 📘 Documentation & Theory
For detailed theoretical explanations, real-world analysis, and the system's Class Diagram, please refer to:
👉 **[DOCUMENTATION.md](./DOCUMENTATION.md)**

---

## ✨ Features

### 1. Block Cipher Modes (Symmetric)
*   **ECB (Electronic Code Book):** Independent block encryption.
*   **CBC (Cipher Block Chaining):** Chained blocks with Initialization Vector (IV).
*   **CTR (Counter Mode):** Converts block cipher to stream cipher using counters.

### 2. Asymmetric & Other Ciphers
*   **RSA:** Public-key encryption with key generation using prime pairs.
*   **RC4:** Lightweight stream cipher.
*   **Monoalphabetic & Hill Ciphers:** Classic substitution and transposition techniques.

### 3. Hashing Algorithms
*   **SHA-1:** Deterministic one-way hash function (160-bit).
*   **MAC:** Message Authentication Code for data integrity.

### 4. Core Components
*   **LCG Key Generator:** Custom Linear Congruential Generator for deterministic key/IV material.
*   **Exception Handling:** Comprehensive protection against invalid inputs and runtime errors.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   Flask (for web interface)

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/omarkapil/crypto_app.git
    cd crypto_app
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

#### Option A: Console Menu (Recommended for testing OOP)
```bash
python main.py
```

#### Option B: Web Dashboard
```bash
python app.py
```
*Once running, visit `http://localhost:5000` in your browser.*

---

## 📂 Project Structure

```text
crypto_app/
├── main.py                     # Console UI Entry Point
├── app.py                      # Flask Web UI Entry Point
├── DOCUMENTATION.md            # Theory, Analysis & Class Diagram
├── TEAM_RESPONSIBILITIES.md    # Task Allocation & Ownership
├── FLOWCHART.md                # System Flow Visualization
├── crypto_modules/             # core Algorithm Implementations
│   ├── base_cipher.py          # Abstract Base Class (OOP)
│   ├── block_ciphers.py        # ECB, CBC, CTR Classes
│   ├── rsa_cipher.py           # RSA Implementation Class
│   ├── sha1_cipher.py          # SHA-1 Hashing Class
│   └── lcg_key_generator.py    # LCG Key Generator Class
├── static/                     # Web Assets (CSS/JS)
└── templates/                  # HTML Templates
```

---

## 🛡️ OOP Principles Applied
*   **Abstraction:** Using `ABC` for the `BlockCipher` interface.
*   **Inheritance:** Hierarchical structure for cipher modes.
*   **Polymorphism:** Method overriding for `encrypt()` and `decrypt()` across different classes.
*   **Encapsulation:** Protecting internal states like LCG seeds and RSA private keys.

---
*Created for the Advanced Programming Project — 2026*
