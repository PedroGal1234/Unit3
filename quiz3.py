#Pedro Gallino
#10/13/17
#My thrid proggraming quiz on loops

for i in range(-5,6):
    print(i)

k = 18
while k<=32:
    print(k)
    k += 2

total = 0
for y in range(13,332,2):
    total = total + y

print(total)

while True:
    word = input('Enter a Word: ')
    if 'z' in word:
        break