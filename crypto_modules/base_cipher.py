"""
base_cipher.py
--------------
Abstract base class for all block cipher implementations.
Uses OOP Abstraction to enforce a consistent interface across
ECB, CBC, and CTR cipher modes (Method Overriding / Runtime Polymorphism).
"""

from abc import ABC, abstractmethod


class BlockCipher(ABC):
    """
    Abstract base class representing a generic block cipher.

    All derived cipher classes (ECB, CBC, CTR) must implement:
        - encrypt(text: str) -> str
        - decrypt(ciphertext: str) -> str

    This demonstrates:
        - Abstraction  : hides implementation details behind a common interface
        - Inheritance  : ECB / CBC / CTR inherit this class
        - Polymorphism : each subclass overrides encrypt / decrypt differently
    """

    BLOCK_SIZE: int = 8  # bytes

    def __init__(self, key_generator):
        """
        Parameters
        ----------
        key_generator : LCGKeyGenerator
            An instance of the LCG key generator used to derive keys / IVs.
        """
        if key_generator is None:
            raise ValueError("A valid LCGKeyGenerator instance is required.")
        self._key_generator = key_generator

    # ------------------------------------------------------------------
    # Abstract interface — every subclass MUST provide its own version
    # ------------------------------------------------------------------

    @abstractmethod
    def encrypt(self, text: str) -> str:
        """Encrypt plaintext and return a human-readable result string."""

    @abstractmethod
    def decrypt(self, ciphertext: str) -> str:
        """Decrypt ciphertext (hex string) and return plaintext."""

    # ------------------------------------------------------------------
    # Shared helpers available to all subclasses
    # ------------------------------------------------------------------

    @staticmethod
    def _xor_bytes(a: bytes, b: bytes) -> bytes:
        """XOR two equal-length byte sequences."""
        return bytes(x ^ y for x, y in zip(a, b))

    @staticmethod
    def _pad(data: bytes, block_size: int) -> bytes:
        """PKCS#7 padding — adds bytes whose value equals the padding length."""
        pad_len = block_size - (len(data) % block_size)
        if pad_len == 0:
            pad_len = block_size
        return data + bytes([pad_len] * pad_len)

    @staticmethod
    def _unpad(data: bytes) -> bytes:
        """Remove PKCS#7 padding."""
        if not data:
            return b""
        pad_len = data[-1]
        if pad_len < 1 or pad_len > 16:
            return data
        return data[:-pad_len]

    def __str__(self) -> str:
        return f"{self.__class__.__name__} Cipher"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(block_size={self.BLOCK_SIZE})>"
