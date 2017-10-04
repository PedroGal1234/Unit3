#Pedro Gallino
#10/4/17
#betterAditionGameDemo.py - ask adition till user gets 5

from random import randint

numCorrect = 0

while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question = 'What is '+ str(num1) + '+' + str(num2) + '?'
    awnser = int(input(question))
    if num1 + num2 == awnser:
        print('Correct!')
        numCorrect += 1
    else:
        print('The answer was', num1+num2)
print("Congratiolations! You Win!")

