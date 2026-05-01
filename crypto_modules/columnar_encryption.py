from math import ceil
from .utils import DEFAULT_SEED, generate_lcg_numbers


def build_key(seed: int, length: int = 5) -> str:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = generate_lcg_numbers(seed, length, len(letters))
    return "".join(letters[n] for n in numbers)


def sanitize(text: str) -> str:
    return "".join(ch.upper() for ch in text if ch.isalpha())


def encrypt(text: str, key: str) -> str:
    clean = sanitize(text)
    if not clean:
        return ""

    cols = len(key)
    rows = ceil(len(clean) / cols)
    padded = clean.ljust(rows * cols, "X")

    matrix = [list(padded[r * cols:(r + 1) * cols]) for r in range(rows)]
    order = sorted(range(cols), key=lambda idx: key[idx])

    cipher_chars: list[str] = []
    for col in order:
        for row in range(rows):
            cipher_chars.append(matrix[row][col])
    return "".join(cipher_chars)


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    key = build_key(DEFAULT_SEED)
    cipher = encrypt(text, key)
    return f"Ciphertext: {cipher}\nKey: {key}\nSeed: {DEFAULT_SEED}"
