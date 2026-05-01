# Monoalphabetic Cipher - Encryption
from .utils import DEFAULT_SEED, generate_lcg_key_alphabet


def normalize(text: str) -> str:
    return "".join(ch.lower() for ch in text if ch.isalpha())


def encrypt(text: str, key: str) -> str:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    translation = str.maketrans(alpha, key)
    letters = normalize(text)
    return letters.translate(translation)


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    key = generate_lcg_key_alphabet(DEFAULT_SEED)
    cipher = encrypt(text, key)
    return f"Ciphertext: {cipher}\nKey: {key}\nSeed: {DEFAULT_SEED}"

