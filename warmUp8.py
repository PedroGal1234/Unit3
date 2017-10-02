#Pedro Gallino
#10/2/17
#warmUp8.py - find sum of all positive integers less than 100,000 that are divisible by 3, 1o, and 17

sum = 0
for i in range(1,100001):
    if i%3 == 0 and i%10 == 0 and i%17 == 0:
        sum = sum+i
print(sum)
