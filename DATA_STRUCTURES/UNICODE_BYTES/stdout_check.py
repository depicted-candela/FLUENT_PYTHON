import sys
from unicodedata import name, lookup

print(sys.version)
print()
print('sys.stdout.isatty():', sys.stdout.isatty())
print('sys.stdout.encoding:', sys.stdout.encoding)
print()
test_chars = [
    '\N{HORIZONTAL ELLIPSIS}', # Escape Sequence Interpretation \N{upper case name}
    # exists in cp1252, not in cp437
    '\N{INFINITY}',
    # exists in cp437, not in cp1252
    '\N{CIRCLED NUMBER FORTY TWO}', # not in cp437 or in cp1252
]

for char in test_chars:
    print(f'Trying to output {name(char)}:')
    print(char)

print('Another one')
# name get the name of a symbol when we need to use it iteratively, lookup from unicodedata is also useful
print(name('㊷') + ": " + lookup('TAMIL SYLLABLE NNAA'))