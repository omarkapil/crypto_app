"""
sha1_cipher.py
--------------
SHA-1 hashing implemented as an OOP class.

SHA-1 properties:
    - One-way function  : cannot be reversed (no decrypt)
    - Fixed output size : always 160 bits / 40 hex characters
    - Deterministic     : same input always produces the same hash
"""


class SHA1Hasher:
    """
    SHA-1 (Secure Hash Algorithm 1) implementation.

    Demonstrates:
        - Encapsulation : all internal constants and helpers are private
        - Single Responsibility : one class, one job (hashing)

    Notes
    -----
    SHA-1 is considered cryptographically broken for security purposes.
    It is implemented here for *educational demonstration only*.
    """

    # ---- SHA-1 initial hash values (section 5.3.1 of FIPS 180-4) ----
    _H0: int = 0x67452301
    _H1: int = 0xEFCDAB89
    _H2: int = 0x98BADCFE
    _H3: int = 0x10325476
    _H4: int = 0xC3D2E1F0

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _left_rotate(value: int, count: int) -> int:
        """Circular left shift of a 32-bit word."""
        return ((value << count) | (value >> (32 - count))) & 0xFFFFFFFF

    def _pre_process(self, message: str) -> bytearray:
        """
        Apply SHA-1 padding:
            1. Append bit '1' (0x80 byte)
            2. Pad with zero bytes until length ≡ 448 (mod 512) bits
            3. Append original length as a 64-bit big-endian integer
        """
        data = bytearray(message.encode("utf-8"))
        original_bit_len = len(message) * 8
        data.append(0x80)
        while (len(data) * 8) % 512 != 448:
            data.append(0x00)
        for i in range(7, -1, -1):
            data.append((original_bit_len >> (i * 8)) & 0xFF)
        return data

    def _process_chunk(
        self,
        chunk: memoryview,
        h0: int, h1: int, h2: int, h3: int, h4: int,
    ) -> tuple:
        """Process a single 512-bit (64-byte) chunk."""
        w = [0] * 80
        for i in range(16):
            base = i * 4
            w[i] = (
                (chunk[base]     << 24)
                | (chunk[base+1] << 16)
                | (chunk[base+2] << 8)
                | chunk[base+3]
            )
        for i in range(16, 80):
            w[i] = self._left_rotate(
                w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1
            )

        a, b, c, d, e = h0, h1, h2, h3, h4

        for i in range(80):
            if i < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (self._left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = self._left_rotate(b, 30)
            b = a
            a = temp

        return (
            (h0 + a) & 0xFFFFFFFF,
            (h1 + b) & 0xFFFFFFFF,
            (h2 + c) & 0xFFFFFFFF,
            (h3 + d) & 0xFFFFFFFF,
            (h4 + e) & 0xFFFFFFFF,
        )

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def hash(self, text: str) -> str:
        """
        Compute the SHA-1 hash of the input string.

        Parameters
        ----------
        text : str — input data

        Returns
        -------
        str — 40-character lowercase hex digest

        Raises
        ------
        ValueError   : if text is empty
        RuntimeError : on unexpected hashing failure
        """
        if not text:
            raise ValueError("Input text cannot be empty.")

        try:
            message = self._pre_process(text)
            h0, h1, h2, h3, h4 = (
                self._H0, self._H1, self._H2, self._H3, self._H4
            )
            view = memoryview(message)
            for chunk_start in range(0, len(message), 64):
                h0, h1, h2, h3, h4 = self._process_chunk(
                    view[chunk_start: chunk_start + 64],
                    h0, h1, h2, h3, h4,
                )
            digest = f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"
            return (
                f"[SHA-1] Hash   : {digest}\n"
                f"Input length   : {len(text)} characters\n"
                f"Output length  : {len(digest)} hex chars (160 bits)\n"
                f"Note           : SHA-1 is one-way — no decryption possible."
            )
        except Exception as exc:
            raise RuntimeError(f"SHA-1 hashing failed: {exc}") from exc

    # Alias so it feels symmetric with cipher classes
    def encrypt(self, text: str) -> str:
        """Alias for hash() — SHA-1 has no decryption."""
        return self.hash(text)

    def decrypt(self, _: str) -> str:  # noqa: D401
        """SHA-1 is a one-way function — decryption is not possible."""
        raise NotImplementedError(
            "SHA-1 is a one-way hash function. Decryption is not supported."
        )

    def __str__(self) -> str:
        return "SHA1Hasher"
