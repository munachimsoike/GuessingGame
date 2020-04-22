import random
number_of_guess = 1
sum_of_guesses = 0

print("Welcome!, Choose a level.")

# Choosing a Level
play = True

while play:
    try:
        level_of_choice = int(input("Select a level 1(Easy), 2(Medium), 3(Hard): "))
        break
    except ValueError:
        print("Please enter a number")
    continue


# Conditions for easy level
if level_of_choice == 1:
    sum_of_guesses = 6
    print("Cool!, Guess our secret number betweem 1 and 10. You have 6 guesses")
    secret_number = random.randint(1, 10)
    print(secret_number)

    while number_of_guess <= 6:
        guest_guess = int(input("Guess: "))
        if guest_guess in range(1, 10):
            if guest_guess == secret_number:
                print("You are right!")
                break
            elif number_of_guess < 6 and guest_guess != secret_number:
                sum_of_guesses -= 1
                print("wrong!, you have " + str(sum_of_guesses) + " " + "guesses left,Try again") 
                number_of_guess += 1
            else:
             print("Game Over!")
             break
        else:
            print("Guess must be between 1 and 10")




# Conditions for medium level
if level_of_choice == 2:
    sum_of_guesses = 4
    print("Cool!, Guess our secret number betweem 1 and 20. You have 4 guesses")
    secret_number = random.randint(1, 20)
    print(secret_number)

    while number_of_guess <= 4:
        guest_guess = int(input("Guess: "))
        if guest_guess in range(1, 20):
            if guest_guess == secret_number:
                print("You are right!")
                break
            elif number_of_guess < 4 and guest_guess != secret_number:
                sum_of_guesses -= 1
                print("wrong!, you have " + str(sum_of_guesses) + " " + "guesses left,Try again") 
                number_of_guess += 1
            else:
             print("Game Over!")
             break
        else:
            print("Guess must be between 1 and 20")


# Conditions for hard level
if level_of_choice == 3:
    sum_of_guesses = 3
    print("Cool!, Guess our secret number betweem 1 and 50. You have 5 guesses")
    secret_number = random.randint(1, 50)
    print(secret_number)

    while number_of_guess <= 3:
        guest_guess = int(input("Guess: "))
        if guest_guess in range(1, 50):
            if guest_guess == secret_number:
                print("You are right!")
                break
            elif number_of_guess < 3 and guest_guess != secret_number:
                sum_of_guesses -= 1
                print("wrong!, you have " + str(sum_of_guesses) + " " + "guesses left,Try again") 
                number_of_guess += 1
            else:
             print("Game Over!")
             break
        else:
            print("Guess must be between 1 and 50")