"""SHA-1 Hashing — wrapper around SHA1Hasher for Flask compatibility."""
from .sha1_cipher import SHA1Hasher

_hasher = SHA1Hasher()

def process_text(text: str) -> str:
    try:
        return _hasher.hash(text)
    except Exception as e:
        return f"ERROR: {e}"
