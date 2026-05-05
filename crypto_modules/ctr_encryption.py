"""CTR Encryption — wrapper around CTRCipher for Flask compatibility."""
from .lcg_key_generator import LCGKeyGenerator
from .block_ciphers import CTRCipher

_kg = LCGKeyGenerator()
_cipher = CTRCipher(_kg)

def process_text(text: str) -> str:
    try:
        return _cipher.encrypt(text)
    except Exception as e:
        return f"ERROR: {e}"
