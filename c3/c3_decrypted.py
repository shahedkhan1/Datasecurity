from collections import Counter
import math

# === Load cipher text ===
from load_cipher3 import CLEANED_CIPHER3 as cipher
key_length = 6

# === Load quadgram scoring model ===

with open("english_quadgrams.txt") as f:
    quadgrams = {}
    total = 0
    for line in f:
        key, count = line.split()
        quadgrams[key] = int(count)
        total += int(count)

# Convert to log probabilities
log_quadgram = {k: math.log10(v / total) for k, v in quadgrams.items()}
floor = math.log10(0.01 / total)

def score(text):
    return sum(log_quadgram.get(text[i:i+4], floor) for i in range(len(text) - 3))

# === Caesar shift scoring per position ===
def shift(text, s):
    return ''.join(chr((ord(c) - ord('A') - s) % 26 + ord('A')) for c in text)

best_key = ""
best_plain = ""
best_score = -float("inf")

columns = ['' for _ in range(key_length)]
for i, c in enumerate(cipher):
    columns[i % key_length] += c

# Guess each letter
key = ""
for i in range(key_length):
    col = columns[i]
    best_s = 0
    best_s_score = -float("inf")
    for s in range(26):
        decrypted = shift(col, s)
        s_score = score(decrypted)
        if s_score > best_s_score:
            best_s_score = s_score
            best_s = s
    key += chr(best_s + ord('A'))

# Decrypt with best key
def decrypt_vigenere(text, key):
    decrypted = []
    for i, c in enumerate(text):
        k = ord(key[i % len(key)]) - ord('A')
        decrypted.append(chr((ord(c) - ord('A') - k) % 26 + ord('A')))
    return ''.join(decrypted)

plaintext = decrypt_vigenere(cipher, key)
print("✅ Best key:", key)
print("🔓 Preview:", plaintext)
