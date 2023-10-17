# GUESS THE NUMBER
# NO OF GUESSES=9
# NO OF GUESSES LEFT
# NO OF GUESSSES USED
# GAME OVER IF HE USE 9 TIMES


a = 18
count = 0


while(count > 9):
    b = float(input('Guess number: '))
    if a<b:
        print('You have entered a greater number')
        break
    elif a>b:
        print('You have entered a smaller number')
        break
    elif a==b:
        print('Congrats, You gues the number right')
        continue
    count = count+1
