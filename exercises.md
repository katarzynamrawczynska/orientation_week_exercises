(formatted file at google drive: https://docs.google.com/document/d/1Fhru_t7CyJsmgPzxcSLpL8PyrHx6TDdGSdUiSfKolF8/edit?usp=sharing )

1. Rock, paper and scissors game
In the rock, paper and scissors game the goal is to create a command-line game where a user has the option to choose between rock, paper and scissors.The program also selects randomly one of the three options. Then the program adds the point to the computer or a player (if someone is the winner) and displays actual scores. The user is is asked if he wants to play again or not.

Hints:

At the beginning create a list with all options (rock, paper and scissors as strings). Then you can choose one of the options randomly using the code:
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)

Remember that in python ‘Paper’ is not the same as ‘paper’. 

2. Password generator
In this project you will write your own password generator. Program asks the user to input password lenght. Then generate random passwords with lower case letters, upper case letters, digits and special characters. In the basic version you don't don't have to worry about whether your randomly generated password contains at least one character from every set, but you can also think about how to do it!

Hints:
Object string has builded-in constance strings you can use in your program:
string.ascii_letters # Concatenation of the ascii (upper and lowercase) letters
string.ascii_lowercase # All lower case letters
string.ascii_uppercase # All Upper case letters
string.digits  # The string ‘0123456789’.
string.punctuation  # String of ASCII characters which are considered special characters.

You can concatenated strings you need and choose a random character using:
random.choice(string_with_all_characters)

