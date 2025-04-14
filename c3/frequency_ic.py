from load_cipher3 import CLEANED_CIPHER3
from collections import Counter

cipher = CLEANED_CIPHER3
total = len(cipher)

# Frequency analysis
counts = Counter(cipher)
print(" Letter Frequencies (%):")
for letter in sorted(counts):
    freq_percent = (counts[letter] / total) * 100
    print(f"{letter}: {freq_percent:.2f}")

# Index of Coincidence
ic_numerator = sum(v * (v - 1) for v in counts.values())
ic = ic_numerator / (total * (total - 1))
print(f"\n Index of Coincidence: {ic:.5f}")
