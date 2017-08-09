from random import randint

def randomGuesser():
    random_number = randint(1, 10)
    guess = -1

    # print(random_number)
    print('I have a secret number. Can you guess it?')
    while guess != random_number:
        guess = int(input('Enter your guess: '))
        if abs(guess - random_number) < 3:
            print("you're warm...")
        elif abs(guess-random_number) > 5:
            print("you're cold...")

            if guess > random_number:
                print('too high')
            elif guess < random_number:
                print('too low')
            else:
                print('So warm you win! The number was ' + str(guess))


randomGuesser()