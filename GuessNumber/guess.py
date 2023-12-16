import random

while True:
    # Print instructions to the user
    print('You have 3 attempts to guess a random number between 1 and 20')

    # Start guessing game by getting a random number between 1 and 20
    number = random.randrange(1, 21)
    i = 1
    print(number)
    user_input = int(input('Guess a number between 1 and 20 '))
    if user_input == number:
        print("Congrats you've got it right!")
    else:
        while i < 3:
            if user_input < number or user_input > number:
                print("Not quite right, try again")
                user_input = int(input('Guess a number between 1 and 20 '))
                i = i + 1
            else:
                i = 4
        if user_input != number:
            print(f"Nice try but the answer was {number}")
        else:
            print("Congrats you've got it right!")
    retry = input("Want to play again? ")
    if retry != 'yes':
        print('Thank you for playing.')
        break

