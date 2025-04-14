from collections import Counter
from load_cipher_text import cipher4_cleaned  # Make sure load_cipher4.py exposes this variable

# === Frequency Analysis ===
total = len(cipher4_cleaned)
counts = Counter(cipher4_cleaned)

print(" Letter Frequencies (%):")
for letter in sorted(counts):
    frequency = (counts[letter] / total) * 100
    print(f"{letter}: {frequency:.2f}")

# === Index of Coincidence (IC) Calculation ===
ic_numerator = sum(v * (v - 1) for v in counts.values())
ic = ic_numerator / (total * (total - 1))

print(f"\n Index of Coincidence: {ic:.5f}")
