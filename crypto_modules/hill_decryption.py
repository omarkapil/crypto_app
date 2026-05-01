from .utils import DEFAULT_SEED, generate_lcg_numbers


def build_key_matrix(seed: int) -> list[list[int]]:
    while True:
        values = generate_lcg_numbers(seed, 4, 26)
        matrix = [values[:2], values[2:]]
        det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
        if det % 2 != 0 and det % 13 != 0:
            return matrix
        seed += 1


def mod_inverse(value: int, modulus: int) -> int | None:
    for i in range(1, modulus):
        if (value * i) % modulus == 1:
            return i
    return None


def inverse_matrix(matrix: list[list[int]]) -> list[list[int]] | None:
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        return None
    return [
        [(matrix[1][1] * det_inv) % 26, (-matrix[0][1] * det_inv) % 26],
        [(-matrix[1][0] * det_inv) % 26, (matrix[0][0] * det_inv) % 26],
    ]


def sanitize(text: str) -> str:
    return "".join(ch.upper() for ch in text if ch.isalpha())


def to_numbers(text: str) -> list[int]:
    return [ord(ch) - ord("A") for ch in text]


def to_text(numbers: list[int]) -> str:
    return "".join(chr(n + ord("A")) for n in numbers)


def multiply_block(block: list[int], matrix: list[list[int]]) -> list[int]:
    return [
        (matrix[0][0] * block[0] + matrix[0][1] * block[1]) % 26,
        (matrix[1][0] * block[0] + matrix[1][1] * block[1]) % 26,
    ]


def decrypt(text: str, matrix: list[list[int]]) -> str:
    clean = sanitize(text)
    if len(clean) % 2 != 0:
        clean += "X"
    nums = to_numbers(clean)
    plain_nums: list[int] = []
    for idx in range(0, len(nums), 2):
        block = nums[idx:idx + 2]
        plain_nums.extend(multiply_block(block, matrix))
    return to_text(plain_nums).rstrip("X")


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    key_matrix = build_key_matrix(DEFAULT_SEED)
    inverse = inverse_matrix(key_matrix)
    if inverse is None:
        return "ERROR: Key matrix is not invertible."

    plaintext = decrypt(text, inverse)
    return (
        f"Plaintext: {plaintext}\n"
        f"Key Matrix: {key_matrix[0]} / {key_matrix[1]}\n"
        f"Seed: {DEFAULT_SEED}"
    )

