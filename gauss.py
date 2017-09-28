#Pedro Gallino
#9/28/17
#gauss.py - adds numbers form 1 to 100 up

max = int(input('Enter a Number: '))
difference = int(input('Enter difference'))
num = 0

for i in range(1,(max+1),difference):
    num=num+i
print(num)
