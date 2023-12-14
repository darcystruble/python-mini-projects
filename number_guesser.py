# NUMBER GUESSER
# random module from python, built into python, no install needed
# must import to use
import random

# FIRST WAY TO GET A RANDOM NUMBER
# random.randrange(start, stop) the stop number IS NOT included in the random number generator, the start number is included
# if you just put one thing in (), it will auto start at 0
# r = random.randrange(-5, 11)
# print(r)

# SECOND WAY TO GET A RANDOM NUMBER
# random.randint(start, stop) the stop number IS included in the random number generator
# random number could now include 11
# randint() must include bottom of the range.
# r = random.randint(0, 11)
# print(r)

top_of_range = input('Type a number: ')

# by default, python returns input as string. int() converts it to a number int("25") => 25
# first we check if it is a number with .isdigit()
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
# print(random_number)

# while the condition is True, the loop will run
# break will stop the loop as soon as line of code meets condition
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    # turn guess into an integer
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    # if/elif/else makes this very clean. if first is false, go to elif. if elif is false, go to else statement.
    if user_guess == random_number:
        print("YOU WIN! You guessed the corrected number. Number is", user_guess)
        # break ends the loop
        break
    elif user_guess > random_number:
        print("Wrong number. You guessed too high. Guess again.")
    else:
        print("Wrong number. You guessed too low. Guess again.")
# print multiple things uses commas, you don't need a space
print("You got it in", guesses, "guesses")