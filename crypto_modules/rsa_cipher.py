"""
rsa_cipher.py
-------------
Simplified RSA cipher implemented as an OOP class.
Uses LCGKeyGenerator for prime-pair generation.

RSA Steps:
    1. Choose two primes p, q  (via LCG)
    2. n   = p * q
    3. phi = (p-1)(q-1)
    4. e   = public exponent coprime with phi
    5. d   = modular inverse of e mod phi
    6. Encrypt : C = M^e mod n
    7. Decrypt : M = C^d mod n
"""

from .lcg_key_generator import LCGKeyGenerator


class RSACipher:
    """
    Simplified RSA Cipher.

    Demonstrates:
        - Encapsulation : key values hidden as private attributes
        - Reusability   : depends on LCGKeyGenerator (composition)

    Notes
    -----
    This is a *simplified educational* RSA using small primes from a
    predetermined list. It is NOT suitable for production security.
    """

    def __init__(self, key_generator: LCGKeyGenerator):
        """
        Parameters
        ----------
        key_generator : LCGKeyGenerator
            Used to generate the prime pair (p, q).

        Raises
        ------
        ValueError : if key_generator is None
        """
        if key_generator is None:
            raise ValueError("A valid LCGKeyGenerator instance is required.")
        self._key_generator = key_generator
        self._n: int = 0
        self._e: int = 0
        self._d: int = 0
        self._generate_keys()

    # ------------------------------------------------------------------
    # Key generation
    # ------------------------------------------------------------------

    @staticmethod
    def _gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def _mod_inverse(a: int, m: int) -> int:
        """Extended Euclidean Algorithm for modular inverse."""
        a = a % m
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        raise ValueError(f"No modular inverse exists for a={a}, m={m}.")

    def _generate_keys(self) -> None:
        """Derive (n, e, d) from LCG-generated primes."""
        try:
            p, q = self._key_generator.generate_prime_pair()
            n = p * q
            phi = (p - 1) * (q - 1)

            e = None
            for candidate in (65537, 257, 17, 5, 3):
                if self._gcd(candidate, phi) == 1:
                    e = candidate
                    break
            if e is None:
                raise RuntimeError("Could not find a valid public exponent.")

            d = self._mod_inverse(e, phi)
            self._n, self._e, self._d = n, e, d
        except Exception as exc:
            raise RuntimeError(f"RSA key generation failed: {exc}") from exc

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def encrypt(self, text: str) -> str:
        """
        Encrypt plaintext using RSA.

        Each character is independently encrypted: C = ord(char)^e mod n.

        Parameters
        ----------
        text : str — plaintext

        Returns
        -------
        str — formatted result with space-separated cipher numbers,
              public key (n, e), and seed

        Raises
        ------
        ValueError   : if text is empty
        RuntimeError : if any character value >= n (key too small)
        """
        if not text:
            raise ValueError("Input text cannot be empty.")

        cipher_values = []
        for char in text:
            m = ord(char)
            if m >= self._n:
                raise RuntimeError(
                    f"Character '{char}' (value {m}) is too large for n={self._n}. "
                    "Use shorter text or a larger key."
                )
            cipher_values.append(pow(m, self._e, self._n))

        return (
            f"[RSA] Ciphertext       : {' '.join(map(str, cipher_values))}\n"
            f"Public Key  (n, e)     : ({self._n}, {self._e})\n"
            f"Seed                   : {self._key_generator.seed}"
        )

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt RSA ciphertext.

        Parameters
        ----------
        ciphertext : str — space-separated integers

        Returns
        -------
        str — formatted result with recovered plaintext and private key

        Raises
        ------
        ValueError   : if input is empty or not space-separated integers
        RuntimeError : on unexpected decryption failure
        """
        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty.")

        try:
            numbers = [int(part) for part in ciphertext.strip().split()]
        except ValueError:
            raise ValueError("Ciphertext must be space-separated integers.")

        try:
            plaintext = "".join(chr(pow(num, self._d, self._n)) for num in numbers)
            return (
                f"[RSA] Plaintext        : {plaintext}\n"
                f"Private Key (n, d)     : ({self._n}, {self._d})\n"
                f"Seed                   : {self._key_generator.seed}"
            )
        except Exception as exc:
            raise RuntimeError(f"RSA decryption failed: {exc}") from exc

    # ------------------------------------------------------------------
    # Properties (read-only access to key material)
    # ------------------------------------------------------------------

    @property
    def public_key(self) -> tuple:
        """Return the public key as (n, e)."""
        return self._n, self._e

    @property
    def private_key(self) -> tuple:
        """Return the private key as (n, d)."""
        return self._n, self._d

    def __str__(self) -> str:
        return f"RSACipher(n={self._n}, e={self._e}, seed={self._key_generator.seed})"
