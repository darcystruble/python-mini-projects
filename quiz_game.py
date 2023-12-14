print("Welcome to the Friends Quiz Game!")

playing = input("Would you like to play? y/n ")
# .lower() converts all text to lower case
# .upper() converts all text to upper case (answers would need to be in upper case to render as true)
if playing.lower() != "y":
    # quit stops the program
    quit()

print("Ok! Let's play :) ")
score = 0

answer1 = input("Which character has a twin? ")
# uses if/else statement. If correct, print correct, if anything else besides correct answer, print sorry!
# if state can only have one else statement
if answer1.lower() == "phoebe":
    print('Correct!')
    score += 1
else:
    print('Sorry! Correct answer is Phoebe')

answer2 = input("Who was Monica's first kiss? ")
if answer2.lower() == "ross":
    print('Correct!')
    score += 1
else:
    print('Sorry! Correct answer is Ross')

answer3 = input("How many times has Ross been married? ")
if answer3 == "3" or answer3.lower() == "three":
    print('Correct!')
    score += 1
else:
    print('Sorry! Correct answer is 3')

answer4 = input("What nickname did Monica's dad give her? ")
if answer4.lower() == "little harmonica":
    print('Correct!')
    score += 1
else:
    print('Sorry! Correct answer is Little Harmonica')

answer5 = input("What is the name of the millionaire Monica dated? ")
if answer5.lower() == "pete":
    print('Correct!')
    score += 1
else:
    print('Sorry! Correct answer is Pete')

# str() turns score from in int to a string. You can't concatanate a number to strings. It will try to add the number to string which isn't possible
print("You got " + str(score) + " questions correct!")
# calculate percentage:
print("You got " + str((score / 5) * 100) + "%!")

