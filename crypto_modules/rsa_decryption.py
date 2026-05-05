"""RSA Decryption — wrapper around RSACipher for Flask compatibility."""
from .lcg_key_generator import LCGKeyGenerator
from .rsa_cipher import RSACipher

_kg = LCGKeyGenerator()
_cipher = RSACipher(_kg)

def process_text(text: str) -> str:
    try:
        return _cipher.decrypt(text)
    except Exception as e:
        return f"ERROR: {e}"
