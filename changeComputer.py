#Pedro Gallino
#9/29/17
#changeComputer.py - tells the number change in coins

total = int(input('Enter the number of cents you need to give in cents: '))
q = 0
d = 0
n = 0
p = 0

while q < total:
    q = q + 25
    if q > total:
        q = q-25
        break
total = total - q

while d < total:
    d = d + 10
    if d > total:
        d = d-10
        break
total = total - d

while n < total:
    n = n + 5
    if n > total:
        n = n-5
        break
total = total - n

while p < total:
    p = p + 1
    if p > total:
        p = p - 1
        break

print('Quarters: ',q/25)
print('Dimes: ',d/10)
print('Nickels: ',n/5)
print('Pennies: ',p)