import string
import secrets

def generate_short_code(length: int = 6) -> str:
    # A-Z, a-z, 0-9 me se random secure 6-letter string banayega
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))