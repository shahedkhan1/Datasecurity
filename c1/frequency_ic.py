from collections import Counter

# cleaned ciphertext from Step 1
ciphertext ="TBOQJOKAUJOCDUFQYVOTAQZMIVSAXDSIBIFNXUMPYDQFFFYAIRATGIEBTIFVYNKGGGSGQQBPXROBNHZPJAFBJROTKUGEXBOCUWOHDDUBEWDITTUTVRSGLMFNNEBFZUFQYVOBJHZFTBOEAGDPVQODXQFRIBEXNZOCLEQTXCOHYQZRDIDZTEBHNIECOGEGZMAAUUNGDBLL"


# Frequency %
def letter_frequency(text):
    total = len(text)
    counter = Counter(text)
    return {char: round((count / total) * 100, 2) for char, count in sorted(counter.items())}

# Index of Coincidence
def index_of_coincidence(text):
    N = len(text)
    counter = Counter(text)
    ic = sum(f * (f - 1) for f in counter.values()) / (N * (N - 1))
    return ic

# Run
freq = letter_frequency(ciphertext)
ic = index_of_coincidence(ciphertext)

print("Letter Frequencies (%):")
for k, v in freq.items():
    print(f"{k}: {v}")

print(f"\nIndex of Coincidence: {round(ic, 5)}")
