

word = input()
vowels_count = 0
for letter in word:
    if letter == 'a':
        vowels_count += 1
    elif letter == 'e':
        vowels_count += 2
    elif letter == 'i':
        vowels_count += 3
    elif letter == 'o':
        vowels_count += 4
    elif letter == 'u':
        vowels_count += 5

print(vowels_count)