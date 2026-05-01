"""
lcg_key_generator.py
--------------------
Encapsulates the Linear Congruential Generator (LCG) algorithm inside
a reusable class.  Used by block ciphers (ECB, CBC, CTR) and RSA.

LCG Formula:
    X_(n+1) = (A * X_n + C) mod M

Where:
    A = 1_103_515_245  (multiplier)
    C = 12_345         (increment)
    M = 2^31 - 1       (modulus — Mersenne prime)
"""


class LCGKeyGenerator:
    """
    Linear Congruential Generator for deterministic key material.

    Demonstrates:
        - Encapsulation : internal state (_state) is private
        - Reusability   : used by ECB, CBC, CTR, and RSA classes
    """

    A: int = 1_103_515_245
    C: int = 12_345
    M: int = 2**31 - 1
    DEFAULT_SEED: int = 98_765

    def __init__(self, seed: int = DEFAULT_SEED):
        """
        Parameters
        ----------
        seed : int
            Starting value for the LCG sequence.

        Raises
        ------
        ValueError
            If seed is not a non-negative integer.
        """
        if not isinstance(seed, int) or seed < 0:
            raise ValueError(f"Seed must be a non-negative integer, got: {seed!r}")
        self.seed: int = seed
        self._state: int = seed % self.M

    # ------------------------------------------------------------------
    # Core generator
    # ------------------------------------------------------------------

    def _next(self) -> int:
        """Advance the generator by one step and return the new state."""
        self._state = (self.A * self._state + self.C) % self.M
        return self._state

    def reset(self) -> None:
        """Reset the generator to its initial seed value."""
        self._state = self.seed % self.M

    # ------------------------------------------------------------------
    # Public helpers
    # ------------------------------------------------------------------

    def generate_sequence(self, length: int, modulo: int = 256) -> list:
        """
        Generate a fresh sequence of `length` integers in [0, modulo).
        Always resets state first so results are deterministic per seed.

        Parameters
        ----------
        length  : int   — how many values to generate
        modulo  : int   — upper bound (exclusive)

        Returns
        -------
        list[int]
        """
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        if modulo <= 0:
            raise ValueError("Modulo must be a positive integer.")
        self.reset()
        return [self._next() % modulo for _ in range(length)]

    def generate_bytes(self, length: int) -> bytes:
        """
        Return `length` pseudo-random bytes derived from the LCG sequence.

        Parameters
        ----------
        length : int — number of bytes

        Returns
        -------
        bytes
        """
        return bytes(self.generate_sequence(length, 256))

    def generate_bytes_with_offset(self, length: int, offset_seed: int) -> bytes:
        """
        Like generate_bytes but uses an offset seed — handy for IVs.

        Parameters
        ----------
        length      : int — number of bytes
        offset_seed : int — alternative seed value

        Returns
        -------
        bytes
        """
        original_seed = self.seed
        self.seed = offset_seed
        result = self.generate_bytes(length)
        self.seed = original_seed      # restore
        return result

    def generate_prime_pair(self) -> tuple:
        """
        Generate two distinct small primes using the LCG sequence.
        Used by the RSA key-generation step.

        Returns
        -------
        tuple[int, int] — (p, q)
        """
        primes = [
            101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
            151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
        ]
        seq = self.generate_sequence(2, len(primes))
        p = primes[seq[0]]
        q = primes[seq[1]] if primes[seq[1]] != p else primes[(seq[1] + 1) % len(primes)]
        return p, q

    # ------------------------------------------------------------------
    # Dunder
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        return f"LCGKeyGenerator(seed={self.seed})"

    def __repr__(self) -> str:
        return f"<LCGKeyGenerator seed={self.seed} state={self._state}>"
