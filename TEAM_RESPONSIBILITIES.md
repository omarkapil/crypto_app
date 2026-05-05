# 👥 Team Responsibilities — Advanced Programming Project
### Cryptographic System | Python OOP

> **Team Size:** 6 Members (Member 1 → Member 6)
> **Project:** Python-based cryptographic system using Object-Oriented Programming

---

## 📋 Responsibility Overview

| Member | Role | Tasks |
|--------|------|-------|
| **Member 1** | 🏗️ OOP Architecture & Base Design | Task 1 (Theory) + Base Classes |
| **Member 2** | 🔐 Block Cipher Modes (ECB & CBC) | Task 2 Part A (ECB + CBC) |
| **Member 3** | 🔑 Key Generator & CTR Mode | Task 2 Part B + CTR Mode |
| **Member 4** | 🔓 RSA & SHA-1 Algorithms | Task 2 Part C + Part D |
| **Member 5** | 🖥️ Console UI & Exception Handling | Task 2 Part E + Task 4 |
| **Member 6** | 📐 UML, Documentation & Flask App | Task 3 + Task 4 (UML) + Web App |

---

## 👤 Member 1 — OOP Architecture & Base Design

**Role:** Project Lead / OOP Designer

**Responsibilities:**
- Write the theoretical explanation for **Task 1** (Inheritance & Polymorphism)
- Design and implement the **abstract base class** for all block ciphers
- Define shared helper methods used by all cipher classes
- Ensure the overall class hierarchy follows OOP principles

**Files Owned:**
```
crypto_modules/base_cipher.py        ← Abstract BlockCipher base class
crypto_modules/__init__.py           ← Package initialisation
```

**Task Coverage:**
- ✅ Task 1.1 — Explain Inheritance and its features
- ✅ Task 1.2 — Differentiate between Single, Multiple, Multilevel, Hierarchical inheritance
- ✅ Task 1.3 — Explain Polymorphism (Method Overriding & Overloading)

**Key Deliverables:**
- `BlockCipher` abstract class with `@abstractmethod` for `encrypt()` and `decrypt()`
- Shared helpers: `_xor_bytes()`, `_pad()`, `_unpad()`
- Written theory document covering Task 1

---

## 👤 Member 2 — Block Cipher Modes: ECB & CBC

**Role:** Cryptography Developer (Block Ciphers)

**Responsibilities:**
- Implement **ECB Mode** (Electronic Code Book) cipher class
- Implement **CBC Mode** (Cipher Block Chaining) cipher class
- Both classes must inherit from `BlockCipher` and override `encrypt()` / `decrypt()`
- Write Flask wrapper modules for web integration

**Files Owned:**
```
crypto_modules/block_ciphers.py      ← ECBCipher and CBCCipher classes
crypto_modules/ecb_encryption.py     ← Flask wrapper for ECB encryption
crypto_modules/ecb_decryption.py     ← Flask wrapper for ECB decryption
crypto_modules/cbc_encryption.py     ← Flask wrapper for CBC encryption
crypto_modules/cbc_decryption.py     ← Flask wrapper for CBC decryption
```

**Task Coverage:**
- ✅ Task 2 Part A — ECB Mode (encrypt + decrypt)
- ✅ Task 2 Part A — CBC Mode (encrypt + decrypt)

**Key Deliverables:**
- `ECBCipher` class — independent block encryption, no IV
- `CBCCipher` class — chained block encryption with IV from LCG
- Each class demonstrates **Method Overriding** (Runtime Polymorphism)

---

## 👤 Member 3 — LCG Key Generator & CTR Mode

**Role:** Cryptography Developer (Key Generation + CTR)

**Responsibilities:**
- Implement the **LCG Key Generator** as a proper OOP class
- Implement **CTR Mode** (Counter Mode) cipher class
- Ensure the LCG generator is reused by all other cipher classes

**Files Owned:**
```
crypto_modules/lcg_key_generator.py  ← LCGKeyGenerator class
crypto_modules/ctr_encryption.py     ← Flask wrapper for CTR encryption
crypto_modules/ctr_decryption.py     ← Flask wrapper for CTR decryption
crypto_modules/utils.py              ← Legacy utility functions (reference)
```

**Task Coverage:**
- ✅ Task 2 Part B — LCG Key Generator class
- ✅ Task 2 Part A — CTR Mode (encrypt + decrypt)

**Key Deliverables:**
- `LCGKeyGenerator` class with `generate_bytes()`, `generate_prime_pair()`, `reset()`
- `CTRCipher` class — converts block cipher to stream cipher using counter blocks

**LCG Formula:**
```
X_(n+1) = (1,103,515,245 × X_n + 12,345) mod (2^31 - 1)
```

---

## 👤 Member 4 — RSA Algorithm & SHA-1 Hashing

**Role:** Cryptography Developer (Asymmetric + Hashing)

**Responsibilities:**
- Implement simplified **RSA** algorithm as an OOP class using LCGKeyGenerator
- Implement **SHA-1** hashing algorithm as an OOP class
- Update Flask wrapper modules to use the new OOP classes

**Files Owned:**
```
crypto_modules/rsa_cipher.py         ← RSACipher class (key gen, encrypt, decrypt)
crypto_modules/sha1_cipher.py        ← SHA1Hasher class
crypto_modules/rsa_encryption.py     ← Flask wrapper for RSA encryption
crypto_modules/rsa_decryption.py     ← Flask wrapper for RSA decryption
crypto_modules/sha1_hashing.py       ← Flask wrapper for SHA-1
crypto_modules/mac_hashing.py        ← MAC hashing module
```

**Task Coverage:**
- ✅ Task 2 Part C — RSA (key generation, encryption, decryption)
- ✅ Task 2 Part D — SHA-1 hashing (one-way, no decryption)

**Key Deliverables:**
- `RSACipher` class with full key generation, encrypt, and decrypt
- `SHA1Hasher` class — full SHA-1 implementation (160-bit digest, no decryption)

**RSA Steps:**
```
1. Generate primes p, q  (via LCGKeyGenerator)
2. n   = p × q
3. phi = (p-1)(q-1)
4. e   = public exponent (coprime with phi)
5. d   = modular inverse of e mod phi
6. Encrypt: C = M^e mod n
7. Decrypt: M = C^d mod n
```

---

## 👤 Member 5 — Console UI & Exception Handling

**Role:** UI Developer & Quality Assurance

**Responsibilities:**
- Build the **console-based menu** interface for the cryptographic system
- Implement **full exception handling** across all modules
- Handle invalid input, encryption errors, and key generation failures
- Analyse a real-world problem using OOP

**Files Owned:**
```
main.py                              ← Console menu (ECB/CBC/CTR/RSA/SHA-1/Exit)
```

**Task Coverage:**
- ✅ Task 2 Part E — Console-based menu UI
- ✅ Task 4.1 — Exception handling (invalid input, encryption errors, key issues)
- ✅ Task 4.2 — Real-world problem analysis (Login System)

**Key Deliverables:**
- Interactive menu with options: ECB / CBC / CTR / RSA / SHA-1 / Exit
- Full `try / except / finally` blocks for every user interaction
- Exception types handled: `ValueError`, `RuntimeError`, `NotImplementedError`, `Exception`

**Console Menu Structure:**
```
[1] ECB Mode
[2] CBC Mode
[3] CTR Mode
[4] RSA Encryption
[5] SHA-1 Hash
[0] Exit
```

---

## 👤 Member 6 — UML, Documentation & Flask Web App

**Role:** Documentation Lead & Web Developer

**Responsibilities:**
- Write theoretical content for **Task 3** (Exception Handling theory, UML)
- Design the **Class Diagram** for the full system (Task 4.3)
- Maintain and update the **Flask web application**
- Update web templates to include ECB and CTR modes

**Files Owned:**
```
app.py                               ← Flask web application (all routes)
templates/index.html                 ← Home page
templates/encryption.html            ← Encryption page
templates/decryption.html            ← Decryption page
templates/hashing.html               ← Hashing page
static/style.css                     ← Application styling
static/script.js                     ← Frontend JavaScript
requirements.txt                     ← Python dependencies
README.md                            ← Project documentation
DOCUMENTATION.md                     ← Theory, Analysis & Class Diagram
FLOWCHART.md                         ← System flowchart
```

**Task Coverage:**
- ✅ Task 3.1 — Exception Handling theory (try/except/finally + importance in secure systems)
- ✅ Task 3.2 — UML definition
- ✅ Task 3.3 — Types of UML diagrams (Structural + Behavioural)
- ✅ Task 3.4 — Class Diagram and its components
- ✅ Task 4.3 — Design full Class Diagram with inheritance and relationships

**Key Deliverables:**
- UML Class Diagram showing all classes, attributes, methods, and relationships
- Updated Flask routes for ECB and CTR modes
- Full project README and documentation

---

## 📁 Complete File Ownership Map

| File | Owner |
|------|-------|
| `crypto_modules/base_cipher.py` | Member 1 |
| `crypto_modules/__init__.py` | Member 1 |
| `crypto_modules/block_ciphers.py` | Member 2 |
| `crypto_modules/ecb_encryption.py` | Member 2 |
| `crypto_modules/ecb_decryption.py" | Member 2 |
| `crypto_modules/cbc_encryption.py` | Member 2 |
| `crypto_modules/cbc_decryption.py` | Member 2 |
| `crypto_modules/lcg_key_generator.py` | Member 3 |
| `crypto_modules/ctr_encryption.py` | Member 3 |
| `crypto_modules/ctr_decryption.py` | Member 3 |
| `crypto_modules/utils.py` | Member 3 |
| `crypto_modules/rsa_cipher.py` | Member 4 |
| `crypto_modules/sha1_cipher.py` | Member 4 |
| `crypto_modules/rsa_encryption.py` | Member 4 |
| `crypto_modules/rsa_decryption.py` | Member 4 |
| `crypto_modules/sha1_hashing.py` | Member 4 |
| `crypto_modules/mac_hashing.py` | Member 4 |
| `main.py` | Member 5 |
| `app.py` | Member 6 |
| `templates/index.html` | Member 6 |
| `templates/encryption.html` | Member 6 |
| `templates/decryption.html` | Member 6 |
| `templates/hashing.html` | Member 6 |
| `static/style.css` | Member 6 |
| `static/script.js` | Member 6 |
| `requirements.txt` | Member 6 |
| `README.md` | Member 6 |
| `DOCUMENTATION.md` | Member 6 |
| `FLOWCHART.md` | Member 6 |

---

## 🗂️ Task Coverage Summary

| Task | Description | Owner |
|------|-------------|-------|
| Task 1.1 | Inheritance concept & features | Member 1 |
| Task 1.2 | Types of inheritance | Member 1 |
| Task 1.3 | Polymorphism (Overriding + Overloading) | Member 1 |
| Task 2A — ECB | ECB cipher class | Member 2 |
| Task 2A — CBC | CBC cipher class | Member 2 |
| Task 2A — CTR | CTR cipher class | Member 3 |
| Task 2B | LCG Key Generator class | Member 3 |
| Task 2C | RSA algorithm class | Member 4 |
| Task 2D | SHA-1 hashing class | Member 4 |
| Task 2E | Console menu UI | Member 5 |
| Task 3.1 | Exception handling theory | Member 6 |
| Task 3.2 | UML definition | Member 6 |
| Task 3.3 | UML diagram types | Member 6 |
| Task 3.4 | Class diagram components | Member 6 |
| Task 4.1 | Exception handling implementation | Member 5 |
| Task 4.2 | Real-world problem analysis | Member 5 |
| Task 4.3 | Class diagram design | Member 6 |

---

*Generated for Advanced Programming Project — Python OOP Cryptographic System*
