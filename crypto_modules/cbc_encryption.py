"""CBC Encryption — wrapper around CBCCipher for Flask compatibility."""
from .lcg_key_generator import LCGKeyGenerator
from .block_ciphers import CBCCipher

BLOCK_SIZE = 8  # kept for any legacy imports

_kg = LCGKeyGenerator()
_cipher = CBCCipher(_kg)

def process_text(text: str) -> str:
    try:
        return _cipher.encrypt(text)
    except Exception as e:
        return f"ERROR: {e}"
