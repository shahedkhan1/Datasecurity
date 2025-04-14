from collections import defaultdict
from math import gcd
from functools import reduce

# cleaned ciphertext here 
ciphertext = "TBOQJOKAUJOCDUFQYVOTAQZMIVSAXDSIBIFNXUMPYDQFFFYAIRATGIEBTIFVYNKGGGSGQQBPXROBNHZPJAFBJROTKUGEXBOCUWOHDDUBEWDITTUTVRSGLMFNNEBFZUFQYVOBJHZFTBOEAGDPVQODXQFRIBEXNZOCLEQTXCOHYQZRDIDZTEBHNIECOGEGZMAAUUNGDBLL"
# === Step 1: Find repeated sequences and their spacings ===
def find_repeats(text, min_len=3, max_len=5):
    repeats = defaultdict(list)
    for length in range(min_len, max_len + 1):
        for i in range(len(text) - length):
            seq = text[i:i+length]
            for j in range(i + length, len(text) - length):
                if text[j:j+length] == seq:
                    repeats[seq].append(j - i)
    return repeats

# === Step 2: Get factors of spacings ===
def get_factors(n):
    return [i for i in range(2, n+1) if n % i == 0]

# === Step 3: Analyze all spacings ===
def kasiski_analysis(repeats):
    factor_counts = defaultdict(int)
    for spacings in repeats.values():
        for space in spacings:
            for f in get_factors(space):
                factor_counts[f] += 1
    return sorted(factor_counts.items(), key=lambda x: x[1], reverse=True)

# === Run analysis ===
repeats = find_repeats(ciphertext)
factors = kasiski_analysis(repeats)

print(" Top key length candidates based on factor frequency:\n")
for f, count in factors[:10]:
    print(f"Length {f}: {count} times")
