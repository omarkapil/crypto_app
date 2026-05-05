"""
block_ciphers.py
----------------
Concrete block cipher implementations derived from BlockCipher.

Class hierarchy (Hierarchical Inheritance):

    BlockCipher  (abstract)
    ├── ECBCipher
    ├── CBCCipher
    └── CTRCipher

Each class overrides encrypt() and decrypt() differently,
demonstrating Runtime Polymorphism (Method Overriding).
"""

from .base_cipher import BlockCipher


# ══════════════════════════════════════════════════════════════════════
# ECB — Electronic Code Book
# ══════════════════════════════════════════════════════════════════════

class ECBCipher(BlockCipher):
    """
    Electronic Code Book (ECB) mode.

    Each block is encrypted independently using a fixed key (XOR-based).
    Identical plaintext blocks produce identical ciphertext blocks.

    Inherits from: BlockCipher
    Overrides    : encrypt(), decrypt()
    """

    def __init__(self, key_generator):
        super().__init__(key_generator)

    def encrypt(self, text: str) -> str:
        """
        Encrypt plaintext in ECB mode.

        Parameters
        ----------
        text : str — plaintext

        Returns
        -------
        str — formatted result with ciphertext hex, key, and seed

        Raises
        ------
        ValueError   : if text is empty
        RuntimeError : on unexpected encryption failure
        """
        if not text:
            raise ValueError("Input text cannot be empty.")

        try:
            key = self._key_generator.generate_bytes(self.BLOCK_SIZE)
            data = self._pad(text.encode("utf-8"), self.BLOCK_SIZE)
            cipher = bytearray()

            for i in range(0, len(data), self.BLOCK_SIZE):
                block = data[i: i + self.BLOCK_SIZE]
                cipher.extend(self._xor_bytes(block, key))

            return (
                f"[ECB] Ciphertext (hex): {bytes(cipher).hex()}\n"
                f"Key (hex)            : {key.hex()}\n"
                f"Seed                 : {self._key_generator.seed}"
            )
        except Exception as exc:
            raise RuntimeError(f"ECB encryption failed: {exc}") from exc

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt ECB-mode ciphertext.

        Parameters
        ----------
        ciphertext : str — hex-encoded ciphertext

        Returns
        -------
        str — formatted result with recovered plaintext

        Raises
        ------
        ValueError   : if ciphertext is empty or not valid hex
        RuntimeError : on unexpected decryption failure
        """
        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty.")

        try:
            data = bytes.fromhex(ciphertext.strip())
        except ValueError:
            raise ValueError("Ciphertext must be a valid hex string.")

        try:
            key = self._key_generator.generate_bytes(self.BLOCK_SIZE)
            plain = bytearray()

            for i in range(0, len(data), self.BLOCK_SIZE):
                block = data[i: i + self.BLOCK_SIZE]
                plain.extend(self._xor_bytes(block, key))

            decoded = self._unpad(bytes(plain)).decode("utf-8")
            return (
                f"[ECB] Plaintext: {decoded}\n"
                f"Key (hex)      : {key.hex()}\n"
                f"Seed           : {self._key_generator.seed}"
            )
        except Exception as exc:
            raise RuntimeError(f"ECB decryption failed: {exc}") from exc


# ══════════════════════════════════════════════════════════════════════
# CBC — Cipher Block Chaining
# ══════════════════════════════════════════════════════════════════════

class CBCCipher(BlockCipher):
    """
    Cipher Block Chaining (CBC) mode.

    Each plaintext block is XOR-ed with the previous ciphertext block
    before encryption, eliminating the pattern weakness of ECB.

    Inherits from: BlockCipher
    Overrides    : encrypt(), decrypt()
    """

    def __init__(self, key_generator):
        super().__init__(key_generator)

    def encrypt(self, text: str) -> str:
        """
        Encrypt plaintext in CBC mode.

        Parameters
        ----------
        text : str — plaintext

        Returns
        -------
        str — formatted result including ciphertext, key, IV, and seed

        Raises
        ------
        ValueError   : if text is empty
        RuntimeError : on unexpected encryption failure
        """
        if not text:
            raise ValueError("Input text cannot be empty.")

        try:
            key = self._key_generator.generate_bytes(self.BLOCK_SIZE)
            iv = self._key_generator.generate_bytes_with_offset(
                self.BLOCK_SIZE, self._key_generator.seed + 1
            )
            data = self._pad(text.encode("utf-8"), self.BLOCK_SIZE)
            cipher = bytearray()
            previous = iv

            for i in range(0, len(data), self.BLOCK_SIZE):
                block = data[i: i + self.BLOCK_SIZE]
                mixed = self._xor_bytes(block, previous)
                cipher_block = self._xor_bytes(mixed, key)
                cipher.extend(cipher_block)
                previous = bytes(cipher_block)

            return (
                f"[CBC] Ciphertext (hex): {bytes(cipher).hex()}\n"
                f"Key (hex)             : {key.hex()}\n"
                f"IV (hex)              : {iv.hex()}\n"
                f"Seed                  : {self._key_generator.seed}"
            )
        except Exception as exc:
            raise RuntimeError(f"CBC encryption failed: {exc}") from exc

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt CBC-mode ciphertext.

        Parameters
        ----------
        ciphertext : str — hex-encoded ciphertext

        Returns
        -------
        str — formatted result with recovered plaintext

        Raises
        ------
        ValueError   : if input is empty or not valid hex
        RuntimeError : on unexpected decryption failure
        """
        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty.")

        try:
            data = bytes.fromhex(ciphertext.strip())
        except ValueError:
            raise ValueError("Ciphertext must be a valid hex string.")

        try:
            key = self._key_generator.generate_bytes(self.BLOCK_SIZE)
            iv = self._key_generator.generate_bytes_with_offset(
                self.BLOCK_SIZE, self._key_generator.seed + 1
            )
            plain = bytearray()
            previous = iv

            for i in range(0, len(data), self.BLOCK_SIZE):
                block = data[i: i + self.BLOCK_SIZE]
                mixed = self._xor_bytes(block, key)
                plain.extend(self._xor_bytes(mixed, previous))
                previous = block

            decoded = self._unpad(bytes(plain)).decode("utf-8")
            return (
                f"[CBC] Plaintext: {decoded}\n"
                f"Key (hex)      : {key.hex()}\n"
                f"IV (hex)       : {iv.hex()}\n"
                f"Seed           : {self._key_generator.seed}"
            )
        except Exception as exc:
            raise RuntimeError(f"CBC decryption failed: {exc}") from exc


# ══════════════════════════════════════════════════════════════════════
# CTR — Counter Mode
# ══════════════════════════════════════════════════════════════════════

class CTRCipher(BlockCipher):
    """
    Counter (CTR) mode.

    Converts a block cipher into a stream cipher by encrypting successive
    counter values and XOR-ing the result with the plaintext.
    CTR is symmetric: encryption and decryption use the same function.

    Inherits from: BlockCipher
    Overrides    : encrypt(), decrypt()
    """

    def __init__(self, key_generator):
        super().__init__(key_generator)

    # ------------------------------------------------------------------
    # Internal: shared keystream generation
    # ------------------------------------------------------------------

    def _generate_keystream(self, key: bytes, nonce: int, length: int) -> bytes:
        """
        Generate a keystream by encrypting counter blocks.

        Parameters
        ----------
        key    : bytes — cipher key (BLOCK_SIZE bytes)
        nonce  : int   — starting counter value
        length : int   — number of keystream bytes required

        Returns
        -------
        bytes
        """
        stream = bytearray()
        counter = nonce
        while len(stream) < length:
            counter_block = counter.to_bytes(self.BLOCK_SIZE, byteorder="big")
            stream.extend(self._xor_bytes(counter_block, key))
            counter += 1
        return bytes(stream[:length])

    # ------------------------------------------------------------------
    # encrypt / decrypt (identical logic — CTR is symmetric)
    # ------------------------------------------------------------------

    def _process(self, text: str, label: str) -> str:
        """Shared logic used by both encrypt and decrypt."""
        key = self._key_generator.generate_bytes(self.BLOCK_SIZE)
        nonce_bytes = self._key_generator.generate_bytes_with_offset(
            self.BLOCK_SIZE, self._key_generator.seed + 2
        )
        nonce = int.from_bytes(nonce_bytes, byteorder="big")

        try:
            raw = bytes.fromhex(text.strip()) if label == "Plaintext" else text.encode("utf-8")
        except ValueError:
            raise ValueError("Ciphertext must be a valid hex string.")

        keystream = self._generate_keystream(key, nonce, len(raw))
        result = self._xor_bytes(raw, keystream)
        return result, key, nonce_bytes

    def encrypt(self, text: str) -> str:
        """
        Encrypt plaintext using CTR mode.

        Parameters
        ----------
        text : str — plaintext

        Returns
        -------
        str — formatted result with ciphertext hex, key, nonce, and seed

        Raises
        ------
        ValueError   : if text is empty
        RuntimeError : on unexpected encryption failure
        """
        if not text:
            raise ValueError("Input text cannot be empty.")

        try:
            key = self._key_generator.generate_bytes(self.BLOCK_SIZE)
            nonce_bytes = self._key_generator.generate_bytes_with_offset(
                self.BLOCK_SIZE, self._key_generator.seed + 2
            )
            nonce = int.from_bytes(nonce_bytes, byteorder="big")
            raw = text.encode("utf-8")
            keystream = self._generate_keystream(key, nonce, len(raw))
            cipher = self._xor_bytes(raw, keystream)

            return (
                f"[CTR] Ciphertext (hex): {cipher.hex()}\n"
                f"Key (hex)             : {key.hex()}\n"
                f"Nonce (hex)           : {nonce_bytes.hex()}\n"
                f"Seed                  : {self._key_generator.seed}"
            )
        except Exception as exc:
            raise RuntimeError(f"CTR encryption failed: {exc}") from exc

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt CTR-mode ciphertext.

        Parameters
        ----------
        ciphertext : str — hex-encoded ciphertext

        Returns
        -------
        str — formatted result with recovered plaintext

        Raises
        ------
        ValueError   : if input is empty or not valid hex
        RuntimeError : on unexpected decryption failure
        """
        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty.")

        try:
            data = bytes.fromhex(ciphertext.strip())
        except ValueError:
            raise ValueError("Ciphertext must be a valid hex string.")

        try:
            key = self._key_generator.generate_bytes(self.BLOCK_SIZE)
            nonce_bytes = self._key_generator.generate_bytes_with_offset(
                self.BLOCK_SIZE, self._key_generator.seed + 2
            )
            nonce = int.from_bytes(nonce_bytes, byteorder="big")
            keystream = self._generate_keystream(key, nonce, len(data))
            plain = self._xor_bytes(data, keystream)

            decoded = plain.decode("utf-8")
            return (
                f"[CTR] Plaintext: {decoded}\n"
                f"Key (hex)      : {key.hex()}\n"
                f"Nonce (hex)    : {nonce_bytes.hex()}\n"
                f"Seed           : {self._key_generator.seed}"
            )
        except Exception as exc:
            raise RuntimeError(f"CTR decryption failed: {exc}") from exc
