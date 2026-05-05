from math import ceil
from .utils import DEFAULT_SEED, generate_lcg_numbers


def build_key(seed: int, length: int = 5) -> str:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = generate_lcg_numbers(seed, length, len(letters))
    return "".join(letters[n] for n in numbers)


def sanitize(text: str) -> str:
    return "".join(ch.upper() for ch in text if ch.isalpha())


def decrypt(cipher: str, key: str) -> str:
    clean = sanitize(cipher)
    if not clean:
        return ""

    cols = len(key)
    rows = ceil(len(clean) / cols)
    total = rows * cols
    padded = clean.ljust(total, "X")

    order = sorted(range(cols), key=lambda idx: key[idx])
    matrix = [[""] * cols for _ in range(rows)]

    idx = 0
    for col in order:
        for row in range(rows):
            matrix[row][col] = padded[idx]
            idx += 1

    plaintext = "".join("".join(row) for row in matrix)
    return plaintext.rstrip("X")


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    key = build_key(DEFAULT_SEED)
    plain = decrypt(text, key)
    return f"Plaintext: {plain}\nKey: {key}\nSeed: {DEFAULT_SEED}"

