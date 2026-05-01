# Hill Cipher - Encryption (2x2)
from .utils import DEFAULT_SEED, generate_lcg_numbers


def sanitize(text: str) -> str:
    return "".join(ch.upper() for ch in text if ch.isalpha())


def build_key_matrix(seed: int) -> list[list[int]]:
    while True:
        values = generate_lcg_numbers(seed, 4, 26)
        matrix = [values[:2], values[2:]]
        det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
        if det % 2 != 0 and det % 13 != 0:
            return matrix
        seed += 1


def to_numbers(text: str) -> list[int]:
    return [ord(ch) - ord("A") for ch in text]


def to_text(numbers: list[int]) -> str:
    return "".join(chr(n + ord("A")) for n in numbers)


def multiply_block(block: list[int], matrix: list[list[int]]) -> list[int]:
    return [
        (matrix[0][0] * block[0] + matrix[0][1] * block[1]) % 26,
        (matrix[1][0] * block[0] + matrix[1][1] * block[1]) % 26,
    ]


def encrypt(text: str, matrix: list[list[int]]) -> str:
    clean = sanitize(text)
    if len(clean) % 2 != 0:
        clean += "X"
    nums = to_numbers(clean)
    cipher_nums: list[int] = []
    for idx in range(0, len(nums), 2):
        block = nums[idx:idx + 2]
        cipher_nums.extend(multiply_block(block, matrix))
    return to_text(cipher_nums)


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    key_matrix = build_key_matrix(DEFAULT_SEED)
    cipher = encrypt(text, key_matrix)
    return (
        f"Ciphertext: {cipher}\n"
        f"Key Matrix: {key_matrix[0]} / {key_matrix[1]}\n"
        f"Seed: {DEFAULT_SEED}"
    )

