import random

def generate_random_number(min, max):
    """Generate a random number between min and max, inclusive."""
    return random.randint(min, max)

def play_game(name, allowed_guesses):
    """Play the number guessing game."""
    number_to_guess = generate_random_number(-100, 100)
    print(f"Welcome to the number guessing game, {name}!")
    print(f"You have {allowed_guesses} guesses to correctly guess a number between -100 and 100.")
    guesses_taken = 0
    with open("game_report.txt", "a") as report_file:
        while guesses_taken < allowed_guesses:
            user_guess = int(input("What is your guess? "))
            guesses_taken += 1
            if user_guess == number_to_guess:
                print("Congratulations! You guessed the number correctly!")
                if guesses_taken < allowed_guesses:
                    print(f"You guessed the number in {guesses_taken} guesses.")
                report_file.write(f"{name}, {guesses_taken}\n")
                return
            elif user_guess < number_to_guess:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")
        print(f"You did not guess the number correctly in {allowed_guesses} guesses.")

if __name__ == "__main__":
    player_name = input("What is your name? ")
    play_game(player_name, 7)
