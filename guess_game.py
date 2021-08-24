import random

def guess_number():
    number = random.randint(1,10)
    number_of_tries = 0
    print("Guess a number beetween 1 and 10:")

    while number_of_tries < 5:
        guess = int(input())
        number_of_tries += 1
        if guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        else:
            break
    if guess == number:
        print("You guessed the number in " + str(number_of_tries) + " tries")     
    else:
        print("The number was " + str(number))

if __name__ == "__main__":
    next_game = True
    while next_game: 
        guess_number()
        next_time_input = input("Do you want to play next time? y/n")
        if next_time_input == 'n':
            next_game = False