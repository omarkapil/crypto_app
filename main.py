"""
main.py
-------
Console-based menu interface for the Cryptographic System.
(Part E — Simple User Interface)

Demonstrates:
    - Exception Handling : try / except / finally throughout
    - Polymorphism       : all cipher objects called via the same interface
    - OOP usage          : all classes instantiated and used here
"""

from crypto_modules.lcg_key_generator import LCGKeyGenerator
from crypto_modules.block_ciphers import ECBCipher, CBCCipher, CTRCipher
from crypto_modules.rsa_cipher import RSACipher
from crypto_modules.sha1_cipher import SHA1Hasher


# ── ANSI colour helpers ────────────────────────────────────────────────
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RED    = "\033[91m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

BANNER = f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════╗
║      Advanced Cryptographic System           ║
║      Python OOP — Educational Demo           ║
╚══════════════════════════════════════════════╝{RESET}
"""

MENU = f"""
{YELLOW}{BOLD}──────────────────── MAIN MENU ────────────────────{RESET}
  [1]  ECB Mode   — Electronic Code Book
  [2]  CBC Mode   — Cipher Block Chaining
  [3]  CTR Mode   — Counter Mode
  [4]  RSA        — Public-Key Encryption
  [5]  SHA-1      — Hash Function (one-way)
  [0]  Exit
{YELLOW}────────────────────────────────────────────────────{RESET}
"""


# ── Cipher factory ─────────────────────────────────────────────────────

def build_ciphers(seed: int) -> dict:
    """Instantiate all cipher objects with a shared LCG key generator."""
    kg = LCGKeyGenerator(seed)
    return {
        "1": ECBCipher(kg),
        "2": CBCCipher(kg),
        "3": CTRCipher(kg),
        "4": RSACipher(kg),
        "5": SHA1Hasher(),
    }


CIPHER_LABELS = {
    "1": "ECB Mode",
    "2": "CBC Mode",
    "3": "CTR Mode",
    "4": "RSA Encryption",
    "5": "SHA-1 Hash",
}


# ── Sub-menu helpers ───────────────────────────────────────────────────

def cipher_menu(cipher, label: str) -> None:
    """
    Present encrypt / decrypt (or hash-only) options for a chosen cipher.
    Full exception handling per Task 4.
    """
    is_hasher = isinstance(cipher, SHA1Hasher)

    while True:
        print(f"\n{CYAN}── {label} ──{RESET}")
        if is_hasher:
            print("  [1] Hash text")
        else:
            print("  [1] Encrypt")
            print("  [2] Decrypt")
        print("  [0] Back to main menu")

        try:
            choice = input(f"\n{BOLD}Choice: {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nReturning to main menu.")
            return

        if choice == "0":
            return

        # ---- get text input -------------------------------------------
        try:
            text = input(f"{BOLD}Enter text: {RESET}").strip()
            if not text:
                print(f"{RED}[!] Text cannot be empty. Please try again.{RESET}")
                continue
        except (EOFError, KeyboardInterrupt):
            print("\nReturning to main menu.")
            return

        # ---- perform operation ----------------------------------------
        try:
            if is_hasher and choice == "1":
                result = cipher.hash(text)
            elif not is_hasher and choice == "1":
                result = cipher.encrypt(text)
            elif not is_hasher and choice == "2":
                result = cipher.decrypt(text)
            else:
                print(f"{RED}[!] Invalid option.{RESET}")
                continue

            print(f"\n{GREEN}{result}{RESET}")

        except ValueError as exc:
            # Invalid input errors (Task 4 — invalid input handling)
            print(f"\n{RED}[Input Error] {exc}{RESET}")

        except NotImplementedError as exc:
            # SHA-1 decrypt attempt (Task 4 — encryption errors)
            print(f"\n{RED}[Not Supported] {exc}{RESET}")

        except RuntimeError as exc:
            # Encryption / decryption failures (Task 4 — encryption errors)
            print(f"\n{RED}[Encryption Error] {exc}{RESET}")

        except Exception as exc:
            # Catch-all for unexpected issues
            print(f"\n{RED}[Unexpected Error] {exc}{RESET}")

        finally:
            # finally block always executes — used for cleanup / logging
            print(f"{CYAN}── Operation complete ──{RESET}")


def get_seed() -> int:
    """
    Ask the user for a custom seed, or use the default.
    Demonstrates exception handling for invalid input.
    """
    default = LCGKeyGenerator.DEFAULT_SEED
    try:
        raw = input(
            f"\n{BOLD}Enter LCG seed (press Enter for default {default}): {RESET}"
        ).strip()
        if not raw:
            return default
        seed = int(raw)
        if seed < 0:
            raise ValueError("Seed must be non-negative.")
        return seed
    except ValueError:
        print(f"{RED}[!] Invalid seed — using default ({default}).{RESET}")
        return default
    except (EOFError, KeyboardInterrupt):
        return default


# ── Main loop ──────────────────────────────────────────────────────────

def main() -> None:
    print(BANNER)

    try:
        seed = get_seed()
        ciphers = build_ciphers(seed)
        print(f"\n{GREEN}[✓] Ciphers initialised with seed={seed}{RESET}")
    except Exception as exc:
        print(f"{RED}[Fatal] Could not initialise ciphers: {exc}{RESET}")
        return

    while True:
        print(MENU)
        try:
            choice = input(f"{BOLD}Select option: {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            choice = "0"

        if choice == "0":
            print(f"\n{CYAN}Goodbye!{RESET}\n")
            break
        elif choice in ciphers:
            cipher_menu(ciphers[choice], CIPHER_LABELS[choice])
        else:
            print(f"{RED}[!] Invalid option. Please choose 0–5.{RESET}")


if __name__ == "__main__":
    main()
