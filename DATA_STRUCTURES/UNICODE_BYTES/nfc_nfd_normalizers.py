from unicodedata import normalize

# From keyboard
s1 = 'café'
# Concatenating unicode symbols with Escape Character
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
print((len(s1), len(s2)) == (4, 5),
      "-> They're essentialy the same, but because the concatenation process not in Python")

print((len(normalize('NFC', s1)), len(normalize('NFC', s2))) == (4, 4),
      "-> NFC comprimes to keyboard symbols as possible")

print((len(normalize('NFD', s1)), len(normalize('NFD', s2))) == (5, 5),
      "-> NFD expands to unicode characters as possible")

print(normalize('NFC', s1) == normalize('NFC', s2),
      "-> Standardize compression to keyboard symbols makes two differently created vars of the same string, the same concatenation")

print(normalize('NFD', s1) == normalize('NFD', s2),
      "-> Standardize expansion to unicode characters makes two differently created vars of the same string, the same concatenation")

print(normalize('NFC', s1))