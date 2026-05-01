# Monoalphabetic Cipher - Decryption
from .utils import DEFAULT_SEED, generate_lcg_key_alphabet


def normalize_cipher(text: str) -> str:
    return "".join(ch.lower() for ch in text if ch.isalpha())


def decrypt(cipher: str, key: str) -> str:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    translation = str.maketrans(key, alpha)
    return cipher.translate(translation)


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    key = generate_lcg_key_alphabet(DEFAULT_SEED)
    normalized = normalize_cipher(text)
    plain = decrypt(normalized, key)
    return f"Plaintext: {plain}\nKey: {key}\nSeed: {DEFAULT_SEED}"

