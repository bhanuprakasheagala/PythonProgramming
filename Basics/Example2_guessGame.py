secret_number = 42
number_of_guesses = 1
# Read in user's gusess as an integer
user_gues = int(input("Please enter a number: "))

while(user_gues != secret_number and number_of_guesses < 5) :
    print("Incorrect")
    user_gues = int(input("Please enter a number: "))
    number_of_guesses += 1

if user_gues == secret_number:
    print("Correct!\n")
else:
    print("Incorrect, Game Over...\n")