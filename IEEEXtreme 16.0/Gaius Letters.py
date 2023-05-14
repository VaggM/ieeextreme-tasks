letters = input()

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]

alphabet_cap = [
    'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z'
]

output = ''

for letter in letters:

    if letter in alphabet:
        alph = alphabet.index(letter)
        output += alphabet[(alph + 14) % 26]

    elif letter in alphabet_cap:
        alph = alphabet_cap.index(letter)
        output += alphabet_cap[(alph + 14) % 26]

    else:
        output += letter

print(output)
