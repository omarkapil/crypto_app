# RC4 Encryption
import base64
from .utils import DEFAULT_SEED, generate_lcg_bytes


def ksa(key: bytes) -> list[int]:
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s


def prga(state: list[int], length: int) -> bytes:
    i = 0
    j = 0
    output = bytearray()
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
        k = state[(state[i] + state[j]) % 256]
        output.append(k)
    return bytes(output)


def rc4_encrypt(data: bytes, key: bytes) -> bytes:
    state = ksa(key)
    keystream = prga(state, len(data))
    return bytes(b ^ k for b, k in zip(data, keystream))


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    key = generate_lcg_bytes(DEFAULT_SEED, 16)
    cipher_bytes = rc4_encrypt(text.encode("utf-8"), key)
    cipher_b64 = base64.b64encode(cipher_bytes).decode("utf-8")
    key_hex = key.hex()
    return f"Ciphertext (Base64): {cipher_b64}\nKey (hex): {key_hex}\nSeed: {DEFAULT_SEED}"

