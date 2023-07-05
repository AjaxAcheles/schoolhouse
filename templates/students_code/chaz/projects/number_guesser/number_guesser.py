# 1. user inputs a number between 1 and 10
# 2. if they are right, then ask if they want to play again.
# 2.5. if they don't want to play again then the program will end. if they do, then go back to step 1
# 3. if they are wrong, go back to step 1
print("WELCOME TO THE NUMBER GUESSER!")
game_over = False
while game_over is False:
    user_input = input("pick a number 1 to 10")
    number_1_to_10 = "8"

    if user_input == number_1_to_10:
        print("congratulations, you guessed the number!")
        user_input = input("would you like to start over?")
        if user_input == "no":
            game_over = True
            continue
        elif user_input == "yes":
            continue
    else:
        print("guess again!")
        continue




