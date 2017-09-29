#Pedro Gallino
#9/29/17
#divisors.py - tells divisors that go into a number

num = int(input('Enter a number: '))
for i in range(1,num):
    if num%i == 0:
        print(i)
