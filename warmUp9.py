#Pedro Gallino
#10/4/17
#warmpUp9.py - print out word with capital vowels

word = input('Enter a word')

for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print(ch.upper())
    else:
        print(ch)

