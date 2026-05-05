"""
main.py
-------
Console-based menu interface for the Cryptographic System.
"""
main.py
-------
Console-based menu interface for the Cryptographic System.
واجهة قائمة معتمدة على وحدة التحكم لنظام التشفير.

(Part E — Simple User Interface)
(الجزء هـ — واجهة مستخدم بسيطة)

Demonstrates: / يوضح البرنامج:
    - Exception Handling : try / except / finally throughout
      معالجة الاستثناءات: استخدام try / except / finally في جميع أنحاء البرنامج
    - Polymorphism       : all cipher objects called via the same interface
      تعدد الأشكال: استدعاء جميع كائنات التشفير من خلال نفس الواجهة
    - OOP usage          : all classes instantiated and used here
      استخدام البرمجة كائنية التوجه: يتم إنشاء مثيلات لجميع الكلاسات واستخدامها هنا
"""

from crypto_modules.lcg_key_generator import LCGKeyGenerator
from crypto_modules.block_ciphers import ECBCipher, CBCCipher, CTRCipher
from crypto_modules.rsa_cipher import RSACipher
from crypto_modules.sha1_cipher import SHA1Hasher


# ── ANSI colour helpers / مساعدات الألوان ────────────────────────────────────────────────
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RED    = "\033[91m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# ── Banner / الشعار ───────────────────────────────────────────────────
BANNER = f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════╗
║      Advanced Cryptographic System           ║
║      Python OOP — Educational Demo           ║
╚══════════════════════════════════════════════╝{RESET}
"""

# ── Menu / القائمة ─────────────────────────────────────────────────────
MENU = f"""
{YELLOW}{BOLD}──────────────────── MAIN MENU ────────────────────{RESET}
  [1]  ECB Mode   — Electronic Code Book (نمط التشفير الإلكتروني)
  [2]  CBC Mode   — Cipher Block Chaining (نمط ربط كتل التشفير)
  [3]  CTR Mode   — Counter Mode (نمط العداد)
  [4]  RSA        — Public-Key Encryption (تشفير المفتاح العام)
  [5]  SHA-1      — Hash Function (دالة الهاش - اتجاه واحد)
  [0]  Exit       — خروج
{YELLOW}────────────────────────────────────────────────────{RESET}
"""


# ── Cipher factory / مصنع خوارزميات التشفير ─────────────────────────────────────────────────────

def build_ciphers(seed: int) -> dict:
    """
    Instantiate all cipher objects with a shared LCG key generator.
    تهيئة جميع كائنات التشفير باستخدام مولد مفاتيح LCG مشترك.
    """
    # Create the key generator instance with the user-provided seed
    # إنشاء مثيل لمولد المفاتيح باستخدام البذرة المقدمة من المستخدم
    kg = LCGKeyGenerator(seed)
    
    # Return a dictionary mapping choice numbers to cipher objects
    # إرجاع قاموس يربط أرقام الخيارات بكائنات التشفير
    return {
        "1": ECBCipher(kg),
        "2": CBCCipher(kg),
        "3": CTRCipher(kg),
        "4": RSACipher(kg),
        "5": SHA1Hasher(),
    }


# Labels for display / تسميات للعرض
CIPHER_LABELS = {
    "1": "ECB Mode",
    "2": "CBC Mode",
    "3": "CTR Mode",
    "4": "RSA Encryption",
    "5": "SHA-1 Hash",
}


# ── Sub-menu helpers / مساعدات القائمة الفرعية ───────────────────────────────────────────────────

def cipher_menu(cipher, label: str) -> None:
    """
    Present encrypt / decrypt (or hash-only) options for a chosen cipher.
    Full exception handling per Task 4.
    عرض خيارات التشفير / فك التشفير (أو الهاش فقط) للخوارزمية المختارة.
    معالجة كاملة للاستثناءات وفقاً للمهمة 4.
    """
    is_hasher = isinstance(cipher, SHA1Hasher)

    while True:
        # Display the sub-menu options
        # عرض خيارات القائمة الفرعية
        print(f"\n{CYAN}── {label} ──{RESET}")
        if is_hasher:
            print("  [1] Hash text")
        else:
            print("  [1] Encrypt")
            print("  [2] Decrypt")
        print("  [0] Back to main menu")

        try:
            # Get the user's choice for the specific cipher
            # الحصول على خيار المستخدم لخوارزمية التشفير المحددة
            choice = input(f"\n{BOLD}Choice: {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+C or end of file gracefully
            # التعامل مع Ctrl+C أو نهاية الملف بشكل لائق
            print("\nReturning to main menu.")
            return

        # Exit sub-menu if user chooses '0'
        # الخروج من القائمة الفرعية إذا اختار المستخدم '0'
        if choice == "0":
            return

        # ---- get text input / الحصول على النص المدخل -------------------------------------------
        try:
            # Ask the user for the text they want to process
            # طلب النص الذي يريد المستخدم معالجته
            text = input(f"{BOLD}Enter text: {RESET}").strip()
            if not text:
                # Validate that text is not empty
                # التحقق من أن النص ليس فارغاً
                print(f"{RED}[!] Text cannot be empty. Please try again.{RESET}")
                continue
        except (EOFError, KeyboardInterrupt):
            print("\nReturning to main menu.")
            return

        # ---- perform operation / تنفيذ العملية ----------------------------------------
        try:
            if is_hasher and choice == "1":
                result = cipher.hash(text)
            elif not is_hasher and choice == "1":
                result = cipher.encrypt(text)
            elif not is_hasher and choice == "2":
                result = cipher.decrypt(text)
            else:
                print(f"{RED}[!] Invalid option / خيار غير صحيح.{RESET}")
                continue

            print(f"\n{GREEN}{result}{RESET}")

        except ValueError as exc:
            # Invalid input errors (Task 4 — invalid input handling)
            # أخطاء إدخال غير صالحة (المهمة 4 - معالجة المدخلات غير الصالحة)
            print(f"\n{RED}[Input Error / خطأ في الإدخال] {exc}{RESET}")

        except NotImplementedError as exc:
            # SHA-1 decrypt attempt (Task 4 — encryption errors)
            # محاولة فك تشفير SHA-1 (المهمة 4 - أخطاء التشفير)
            print(f"\n{RED}[Not Supported / غير مدعوم] {exc}{RESET}")

        except RuntimeError as exc:
            # Encryption / decryption failures (Task 4 — encryption errors)
            # فشل التشفير / فك التشفير (المهمة 4 - أخطاء التشفير)
            print(f"\n{RED}[Encryption Error / خطأ في التشفير] {exc}{RESET}")

        except Exception as exc:
            # Catch-all for unexpected issues
            # معالج شامل للمشاكل غير المتوقعة
            print(f"\n{RED}[Unexpected Error / خطأ غير متوقع] {exc}{RESET}")

        finally:
            # finally block always executes — used for cleanup / logging
            # كتلة finally تُنفذ دائماً - تُستخدم للتنظيف أو تسجيل العمليات
            print(f"{CYAN}── Operation complete / اكتملت العملية ──{RESET}")


def get_seed() -> int:
    """
    Ask the user for a custom seed, or use the default.
    Demonstrates exception handling for invalid input.
    سؤال المستخدم عن "بذرة" (seed) مخصصة، أو استخدام القيمة الافتراضية.
    يوضح معالجة الاستثناءات للمدخلات غير الصالحة.
    """
    default = LCGKeyGenerator.DEFAULT_SEED
    try:
        # Prompt for a seed value
        # طلب قيمة البذرة
        raw = input(
            f"\n{BOLD}Enter LCG seed (press Enter for default {default}): {RESET}"
        ).strip()
        
        # If input is empty, return the default seed
        # إذا كان الإدخال فارغاً، يتم إرجاع البذرة الافتراضية
        if not raw:
            return default
            
        # Convert input string to integer
        # تحويل النص المدخل إلى عدد صحيح
        seed = int(raw)
        
        # Ensure the seed is a positive number
        # التأكد من أن البذرة عدد موجب
        if seed < 0:
            raise ValueError("Seed must be non-negative.")
        return seed
    except ValueError:
        # If input is not a valid number, use the default seed
        # إذا كان الإدخال ليس رقماً صالحاً، يتم استخدام البذرة الافتراضية
        print(f"{RED}[!] Invalid seed — using default ({default}).{RESET}")
        return default
    except (EOFError, KeyboardInterrupt):
        # Fallback to default on interruption
        # الرجوع للافتراضي عند المقاطعة
        return default


# ── Main loop / الحلقة الرئيسية ──────────────────────────────────────────────────────────

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
        # Print the main menu choices
        # طباعة خيارات القائمة الرئيسية
        print(MENU)
        try:
            # Capture user input for the main menu selection
            # التقاط إدخال المستخدم لاختيار القائمة الرئيسية
            choice = input(f"{BOLD}Select option: {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            # Set choice to '0' (Exit) if user interrupts
            # ضبط الخيار على '0' (خروج) إذا قام المستخدم بالمقاطعة
            choice = "0"

        # Exit the application
        # الخروج من التطبيق
        if choice == "0":
            print(f"\n{CYAN}Goodbye! / مع السلامة!{RESET}\n")
            break
        # Navigate to the chosen cipher sub-menu
        # الانتقال إلى القائمة الفرعية للخوارزمية المختارة
        elif choice in ciphers:
            cipher_menu(ciphers[choice], CIPHER_LABELS[choice])
        # Handle invalid menu selections
        # معالجة اختيارات القائمة غير الصالحة
        else:
            print(f"{RED}[!] Invalid option. Please choose 0–5.{RESET}")
            print(f"{RED}[!] خيار غير صحيح. يرجى اختيار رقم من 0 إلى 5.{RESET}")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
