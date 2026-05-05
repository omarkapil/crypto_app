import base64
from .utils import DEFAULT_SEED, generate_lcg_bytes
from .rc4_encryption import ksa, prga


def rc4_decrypt(cipher_bytes: bytes, key: bytes) -> bytes:
    state = ksa(key)
    keystream = prga(state, len(cipher_bytes))
    return bytes(b ^ k for b, k in zip(cipher_bytes, keystream))


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    try:
        cipher_bytes = base64.b64decode(text)
    except Exception:
        return "ERROR: Invalid Base64 input."

    key = generate_lcg_bytes(DEFAULT_SEED, 16)
    plain_bytes = rc4_decrypt(cipher_bytes, key)
    try:
        plain_text = plain_bytes.decode("utf-8")
    except UnicodeDecodeError:
        plain_text = plain_bytes.decode("latin-1")

    return f"Plaintext: {plain_text}\nKey (hex): {key.hex()}\nSeed: {DEFAULT_SEED}"

