# Crypto App

A web-based cryptographic application built with Flask that implements various encryption algorithms and cryptographic techniques.

## Features

This application supports the following cryptographic methods:

**Encryption / Decryption**
1. **Monoalphabetic Cipher** – substitution cipher with deterministic LCG key
2. **Columnar Transposition** – grid-based rearrangement using LCG keyword
3. **Hill Cipher** – 2×2 matrix cipher implemented without external libraries
4. **RC4** – lightweight stream cipher using LCG-derived key bytes
5. **CBC (XOR-based)** – simple block cipher in CBC mode with deterministic IV
6. **RSA** – classic public/private key encryption using small primes for learning

**Hashing**
- **MAC (HMAC-SHA256)**
- **SHA-1**

## Requirements

- Python 3.10+
- Flask >= 3.0.0 (see `requirements.txt`)

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/omarkapil/crypto-app.git>
cd crypto-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Select **Encryption**, **Decryption**, or **Hashing**
4. Choose the technique (Monoalphabetic, RSA, etc.)
5. Enter your text, then click **Start** to run the operation
6. Review the output + key/seed information

## Project Structure

```
crypto-app-main/
├── app.py                      # Flask routes + API
├── requirements.txt            # Dependencies
├── crypto_modules/             # Algorithms (encryption/decryption/hash)
│   ├── utils.py                # LCG helpers and shared logic
│   ├── monoalphabetic_encryption.py
│   ├── monoalphabetic_decryption.py
│   ├── columnar_encryption.py
│   ├── columnar_decryption.py
│   ├── hill_encryption.py
│   ├── hill_decryption.py
│   ├── rc4_encryption.py
│   ├── rc4_decryption.py
│   ├── cbc_encryption.py
│   ├── cbc_decryption.py
│   ├── rsa_encryption.py
│   ├── rsa_decryption.py
│   ├── mac_hashing.py
│   └── sha1_hashing.py
├── static/
│   ├── script.js               # Frontend logic
│   └── style.css               # Styling (clean, simple)
└── templates/
    ├── index.html
    ├── encryption.html
    ├── decryption.html
    └── hashing.html
```

## Notes

- All algorithms now rely on Python's standard library only
- Keys and IVs come from a deterministic Linear Congruential Generator (LCG) seed
- Use the same seed (built-in default) for both encryption and decryption via the UI
- Hashing techniques (MAC/SHA-1) are one-way, so decryption is not available


