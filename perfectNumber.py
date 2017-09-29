#Pedro Gallino
#9/29/17
#perfectNumber.py - says if a number is perfect

num = int(input('Enter a number: '))
i=1
lol = 0

while i < num:
    if num%i == 0:
        lol = lol+i
    i = i+1
if lol == num:
    print('Perfect')
else:
    print('Not Perfect')
