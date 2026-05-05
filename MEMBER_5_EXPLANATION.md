# 📘 Member 5 — Console UI & Exception Handling Explanation

This document provides a line-by-line explanation of `main.py`, which is the primary responsibility of **Member 5**. This guide will help you understand how the Console UI works and how Exception Handling is implemented throughout the system.

---

## 📄 `main.py` Line-by-Line Breakdown

### 1. Header & Documentation (Lines 1–26)
*   **Lines 1–4:** Define the purpose of the file (Console-based menu).
*   **Lines 5–9:** Bilingual description of the interface.
*   **Lines 11–17:** Lists the core programming concepts demonstrated: Exception Handling, Polymorphism, and OOP usage.

### 2. Imports (Lines 28–31)
*   **Line 28:** Imports `LCGKeyGenerator` to handle deterministic key creation.
*   **Line 29:** Imports block cipher modes (`ECB`, `CBC`, `CTR`).
*   **Line 30:** Imports `RSACipher` for asymmetric encryption.
*   **Line 31:** Imports `SHA1Hasher` for hashing.

### 3. Visual Styling (Lines 34–55)
*   **Lines 39–44:** Define ANSI escape codes for colors (Green, Yellow, Cyan, Red, Bold). These make the console output look professional.
*   **Line 50–55:** The `BANNER` constant displays the project title in a styled box.

### 4. Main Menu String (Lines 58–78)
*   **Lines 59–78:** Defines the `MENU` string, showing all available cryptographic options (1–5) and the Exit option (0).

### 5. Cipher Factory (Lines 82–108)
*   **Function `build_ciphers(seed)`:**
    *   **Line 91:** Creates an instance of `LCGKeyGenerator` using the user's seed.
    *   **Lines 102–108:** Returns a dictionary where keys are strings ("1", "2", etc.) and values are the actual cipher objects. This demonstrates **OOP Instantiation**.

### 6. Sub-Menu Logic (Lines 130–265)
*   **Function `cipher_menu(cipher, label)`:**
    *   **Line 140:** Checks if the object is a hasher (SHA-1) because hashers don't have a "Decrypt" option.
    *   **Lines 142–154:** A `while True` loop keeps the user in the sub-menu until they choose to go back.
    *   **Line 156 (Start of Exception Handling):** Uses `try` to capture user input.
    *   **Lines 161–165:** **Exception Handling:** Catches `EOFError` (Ctrl+D) or `KeyboardInterrupt` (Ctrl+C) so the program doesn't crash if the user tries to quit abruptly.
    *   **Line 173–198:** **Input Validation:** Another `try` block for text input. If the text is empty (Line 192), it warns the user and continues the loop.
    *   **Line 205–218:** **Polymorphism in Action:** Depending on the choice, it calls `.hash()`, `.encrypt()`, or `.decrypt()`. Notice how the code doesn't care which cipher it is; it just calls the method.
    *   **Line 222–241:** **Specific Exception Handling (Task 4):**
        *   `ValueError`: Handles bad inputs (like entering letters where numbers are expected).
        *   `NotImplementedError`: Specifically handles attempts to decrypt a SHA-1 hash.
        *   `RuntimeError`: Handles internal logic failures during encryption.
    *   **Line 243–246:** **The `finally` block:** This line *always* runs, confirming the operation is complete regardless of success or failure.

### 7. Seed Input (Lines 268–319)
*   **Function `get_seed()`:**
    *   **Lines 277–308:** Asks the user for an LCG seed.
    *   **Line 306–307:** Raises a `ValueError` manually if the seed is negative.
    *   **Line 309–318:** **Graceful Fallback:** If the user enters garbage, the program catches the error and uses a `DEFAULT_SEED` instead of crashing.

### 8. The Main Loop (Lines 332–389)
*   **Function `main()`:**
    *   **Line 336:** Gets the seed.
    *   **Line 337:** Builds the cipher dictionary.
    *   **Lines 343–385:** The main loop that drives the entire application.
    *   **Line 352–355:** Handles menu-level interruptions.
    *   **Line 359:** Exits if "0" is selected.
    *   **Line 364:** If the choice is valid, it calls `cipher_menu()`—passing the object and its label.

---

## 🛠️ Key Responsibilities for Member 5

1.  **Robustness:** Your job is to ensure that no matter what the user types (empty strings, symbols, very long text), the program stays running.
2.  **User Feedback:** When an error occurs (like the `Input Error` on Line 226), the message must be clear and helpful.
3.  **Clean Code:** Maintain the ANSI color scheme to ensure the UI remains readable and organized.

> [!TIP]
> Always remember that the `finally` block is your best friend for logging or resetting states after an operation.
