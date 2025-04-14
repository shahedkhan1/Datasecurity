import random
import math
from collections import Counter
from load_cipher_text import cipher4_cleaned as cipher  # Cleaned cipher string

# === Load quadgram frequencies ===
with open("english_quadgrams.txt") as f:
    quads = {}
    total = 0
    for line in f:
        k, v = line.split()
        quads[k] = int(v)
        total += int(v)

log_quads = {k: math.log10(v / total) for k, v in quads.items()}
floor = math.log10(0.01 / total)

def quad_score(text):
    return sum(log_quads.get(text[i:i+4], floor) for i in range(len(text) - 3))

# === Decrypt mono-sub using key ===
def decrypt(text, key):
    table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', key)
    return text.translate(table)

# === Generate frequency-based starting key ===
english_freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
cipher_freq = [item[0] for item in Counter(cipher).most_common()]
initial_key = ''.join([english_freq_order[cipher_freq.index(c)] if c in cipher_freq else c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

# === Hill Climbing ===
def random_swap(s):
    a, b = random.sample(range(26), 2)
    lst = list(s)
    lst[a], lst[b] = lst[b], lst[a]
    return ''.join(lst)

best_key = initial_key
best_score = quad_score(decrypt(cipher, best_key))
max_tries = 3000

for _ in range(max_tries):
    candidate = random_swap(best_key)
    candidate_score = quad_score(decrypt(cipher, candidate))
    if candidate_score > best_score:
        best_key, best_score = candidate, candidate_score

# === Final Output ===
plaintext = decrypt(cipher, best_key)
print(f" Best Key Mapping:\n{best_key}")
print(f"\n Decryption Preview:\n{plaintext[:500]}")
