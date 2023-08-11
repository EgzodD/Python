number = 23 
guess = int(input('Enter number : '))

if guess == number:
    print('Happy, you win')
    print('(no win prins)')
elif guess < number:
    print('No number big')
else:
    print('No, number small')

