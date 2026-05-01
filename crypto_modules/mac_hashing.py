# MAC (Message Authentication Code) - Hashing
# ملف الهاشينج بتقنية MAC

import hmac
import hashlib
import base64
from .utils import DEFAULT_SEED, generate_lcg_bytes

def generate_mac(message: str, key: bytes) -> str:
    """Generate HMAC-SHA256 for the message."""
    mac = hmac.new(key, message.encode('utf-8'), hashlib.sha256)
    return mac.hexdigest()

def process_text(text: str) -> str:
    """
    Process text using MAC (Message Authentication Code) for Hashing.
    """
    if not text:
        return "ERROR: Input text is empty."
    
    try:
        key = generate_lcg_bytes(DEFAULT_SEED, 32)
        mac = generate_mac(text, key)
        key_b64 = base64.b64encode(key).decode('utf-8')
        
        result = (
            f"MAC (HMAC-SHA256): {mac}\n"
            f"Key (base64): {key_b64}\n"
            f"Seed: {DEFAULT_SEED}\n"
            f"Message: {text}"
        )
        return result
    except Exception as e:
        return f"ERROR: MAC generation failed: {str(e)}"

