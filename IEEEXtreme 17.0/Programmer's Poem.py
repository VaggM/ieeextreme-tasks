import string

alphabet = list(string.ascii_lowercase)
alphabet.remove("x")
k = 0


n, m = map(int, input().split())

sets = []
for i in range(n):
    input_string = input()
    sets.append(input_string.split())

sets_flags = []
for i in range(n):
    sets_flags.append("")

input_string = input()

prev_text = ""

for i in range(m):
    input_string = input().split()
    text = input_string[-1].lower()

    rhyme_flag = 0
    
    if prev_text == "":
        prev_text = text
    else:
        l = 0
        for i, single_set in enumerate(sets):
            if prev_text in single_set and text in single_set:
                if sets_flags[i] == "":
                    sets_flags[i] = alphabet[k]
                    k += 1
                l = i
                rhyme_flag = 1
                    

                    
        if rhyme_flag:
            print(2*sets_flags[l].upper(), end="")
        else:
            print("XX", end='')
            
        prev_text = ""
if (m % 2) == 1:
    print("X", end='')
    
print()