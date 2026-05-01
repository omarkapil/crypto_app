DEFAULT_SEED = 98765
LCG_MOD = 2**31 - 1
LCG_A = 1103515245
LCG_C = 12345


def generate_lcg_sequence(seed: int, length: int, modulo: int) -> list[int]:
    numbers: list[int] = []
    state = seed % LCG_MOD
    for _ in range(length):
        state = (LCG_A * state + LCG_C) % LCG_MOD
        numbers.append(state % modulo)
    return numbers


def generate_lcg_bytes(seed: int, length: int) -> bytes:
    values = generate_lcg_sequence(seed, length, 256)
    return bytes(values)


def generate_lcg_key_alphabet(seed: int) -> str:
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    positions = generate_lcg_sequence(seed, len(alpha), len(alpha))
    paired = sorted(zip(positions, alpha))
    return "".join(letter for _, letter in paired)


def generate_lcg_numbers(seed: int, count: int, limit: int) -> list[int]:
    return generate_lcg_sequence(seed, count, limit)


def generate_lcg_prime_pair(seed: int) -> tuple[int, int]:
    primes = [
        101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
        151, 157, 163, 167, 173, 179, 181, 191, 193, 197
    ]
    sequence = generate_lcg_sequence(seed, 2, len(primes))
    p = primes[sequence[0]]
    q = primes[sequence[1]] if primes[sequence[1]] != p else primes[(sequence[1] + 1) % len(primes)]
    return p, q

