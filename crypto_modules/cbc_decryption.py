"""CBC Decryption — wrapper around CBCCipher for Flask compatibility."""
from .lcg_key_generator import LCGKeyGenerator
from .block_ciphers import CBCCipher

_kg = LCGKeyGenerator()
_cipher = CBCCipher(_kg)

def process_text(text: str) -> str:
    try:
        return _cipher.decrypt(text)
    except Exception as e:
        return f"ERROR: {e}"
