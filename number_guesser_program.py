import random

top_of_range = input('Type the number :')
guess = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("please type the number larger than 0 next time!")
        quit()

else:
    print("please type the number next time")

random_number = random.randint(0,top_of_range)


while True:
    guess = guess +1
    user_guess = input('Make a guess :')

    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("please type the number.")
        continue

    if user_guess == random_number:
        print("you got it")
        break
    else:
        print("you got it wrong")

print("You got it in",  str(guess) + " guesses")
