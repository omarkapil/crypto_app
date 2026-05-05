# 📘 Member 5 — Console UI & Exception Handling Explanation

This document provides a line-by-line explanation of `main.py`, including the actual code segments, which is the primary responsibility of **Member 5**.

---

## 📄 `main.py` Line-by-Line Breakdown

### 1. Header & Documentation
```python
"""
main.py
-------
Console-based menu interface for the Cryptographic System.
واجهة قائمة معتمدة على وحدة التحكم لنظام التشفير.

(Part E — Simple User Interface)
(الجزء هـ — واجهة مستخدم بسيطة)

Demonstrates: / يوضح البرنامج:
    - Exception Handling : try / except / finally throughout
    - Polymorphism       : all cipher objects called via the same interface
    - OOP usage          : all classes instantiated and used here
"""
```
*   **Purpose:** Defines the file and the core concepts (Exception Handling, Polymorphism, OOP).

### 2. Imports
```python
from crypto_modules.lcg_key_generator import LCGKeyGenerator
from crypto_modules.block_ciphers import ECBCipher, CBCCipher, CTRCipher
from crypto_modules.rsa_cipher import RSACipher
from crypto_modules.sha1_cipher import SHA1Hasher
```
*   **Key Generator:** Imports the class that creates keys.
*   **Ciphers:** Imports all the encryption/hashing classes Member 5 must present to the user.

### 3. Visual Styling & Banner
```python
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RED    = "\033[91m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

BANNER = f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════╗
║      Advanced Cryptographic System           ║
║      Python OOP — Educational Demo           ║
╚══════════════════════════════════════════════╝{RESET}
"""
```
*   **ANSI Codes:** Used to color the text in the terminal.
*   **Banner:** A stylized header shown at startup.

### 4. Main Menu String
```python
MENU = f"""
{YELLOW}{BOLD}──────────────────── MAIN MENU ────────────────────{RESET}
  [1]  ECB Mode   — Electronic Code Book (نمط التشفير الإلكتروني)
  [2]  CBC Mode   — Cipher Block Chaining (نمط ربط كتل التشفير)
  [3]  CTR Mode   — Counter Mode (نمط العداد)
  [4]  RSA        — Public-Key Encryption (تشفير المفتاح العام)
  [5]  SHA-1      — Hash Function (دالة الهاش - اتجاه واحد)
  [0]  Exit       — خروج
{YELLOW}────────────────────────────────────────────────────{RESET}
"""
```
*   **Selection:** The UI allows users to select any cryptographic algorithm via numbers.

### 5. Cipher Factory (OOP in Action)
```python
def build_ciphers(seed: int) -> dict:
    kg = LCGKeyGenerator(seed)
    return {
        "1": ECBCipher(kg),
        "2": CBCCipher(kg),
        "3": CTRCipher(kg),
        "4": RSACipher(kg),
        "5": SHA1Hasher(),
    }
```
*   **Instantiation:** This function creates the objects. Notice how `kg` (the key generator) is shared between ciphers to ensure consistent key material.

### 6. Sub-Menu Logic & Exception Handling
```python
def cipher_menu(cipher, label: str) -> None:
    is_hasher = isinstance(cipher, SHA1Hasher)
    while True:
        print(f"\n{CYAN}── {label} ──{RESET}")
        # ... menu printing ...
        try:
            choice = input(f"\n{BOLD}Choice: {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nReturning to main menu.")
            return

        if choice == "0": return

        try:
            text = input(f"{BOLD}Enter text: {RESET}").strip()
            if not text:
                print(f"{RED}[!] Text cannot be empty. Please try again.{RESET}")
                continue
            
            # Polymorphism: result is fetched by calling the same methods
            if is_hasher and choice == "1":
                result = cipher.hash(text)
            elif not is_hasher and choice == "1":
                result = cipher.encrypt(text)
            elif not is_hasher and choice == "2":
                result = cipher.decrypt(text)
            
            print(f"\n{GREEN}{result}{RESET}")

        except ValueError as exc:
            print(f"\n{RED}[Input Error / خطأ في الإدخال] {exc}{RESET}")
        except NotImplementedError as exc:
            print(f"\n{RED}[Not Supported / غير مدعوم] {exc}{RESET}")
        except Exception as exc:
            print(f"\n{RED}[Unexpected Error / خطأ غير متوقع] {exc}{RESET}")
        finally:
            print(f"{CYAN}── Operation complete / اكتملت العملية ──{RESET}")
```
*   **Polymorphism:** The `cipher` object could be any class, but we call the same methods.
*   **Exception Handling:**
    *   `try`: Wraps risky operations (input, encryption).
    *   `except`: Catches specific errors so the app doesn't crash.
    *   `finally`: Ensures a cleanup message is always shown.

### 7. Seed Input with Validation
```python
def get_seed() -> int:
    default = LCGKeyGenerator.DEFAULT_SEED
    try:
        raw = input(f"\n{BOLD}Enter LCG seed: {RESET}").strip()
        if not raw: return default
        seed = int(raw)
        if seed < 0: raise ValueError("Seed must be non-negative.")
        return seed
    except ValueError:
        print(f"{RED}[!] Invalid seed — using default ({default}).{RESET}")
        return default
```
*   **Validation:** Checks if the user typed a number and if it's positive. If not, it falls back to a safe default.

### 8. The Main Execution Loop
```python
def main() -> None:
    print(BANNER)
    try:
        seed = get_seed()
        ciphers = build_ciphers(seed)
    except Exception as exc:
        print(f"{RED}[Fatal] Could not initialise ciphers: {exc}{RESET}")
        return

    while True:
        print(MENU)
        choice = input(f"{BOLD}Select option: {RESET}").strip()
        if choice == "0": break
        elif choice in ciphers:
            cipher_menu(ciphers[choice], CIPHER_LABELS[choice])
        else:
            print(f"{RED}[!] Invalid option.{RESET}")
```
*   **Flow Control:** The engine that runs the program until the user chooses to exit.

---

## 🛠️ Key Responsibilities for Member 5

1.  **Robustness:** Prevent crashes using `try/except`.
2.  **Validation:** Ensure inputs are not empty or invalid.
3.  **UI Consistency:** Use the ANSI colors (`GREEN`, `RED`, etc.) to guide the user.

> [!IMPORTANT]
> The most important part for Member 5 is the **Exception Handling** implementation in Task 4, ensuring secure and stable software.
