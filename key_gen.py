import os

def generate_key_iv():
    key = os.urandom(32)  # AES-256 için 256 bitlik rastgele anahtar
    iv2 = os.urandom(16)  # AES için 128 bitlik rastgele IV
    return key, iv2

# Anahtar ve IV'yi oluştur
key, iv2 = generate_key_iv()

# Oluşturulan anahtar ve IV'yi hexadecimal olarak yazdır
print(f"Oluşturulan Anahtar (Key): {key.hex()}")
print(f"Oluşturulan IV2: {iv2.hex()}")
