print('We are going to play a game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be! This will be the answer to the calculations.')
answer = int(input('Player 1 enter a number between 10 and 49: '))
factor = 99 - answer
Num1 = int(input('Player 2 enter a number between 55 and 99: '))
Num2 = Num1 + factor
Num4 = str(Num2)
Num3 = ((Num2 - 100)+int(Num4[0]))
NUMBER = Num1 - Num3
print(NUMBER)
print('I said the answer was '+str(NUMBER)+',and the calculation result is '+str(NUMBER))





