import random

def get_difficulty():
    """Ask the player to choose a difficulty level."""
    print("\n🎮 Welcome to Guess the Number!")
    print("-----------------------------------")
    print("Choose a difficulty:")
    print("  1. Easy   (1–50,  10 guesses)")
    print("  2. Medium (1–100,  7 guesses)")
    print("  3. Hard   (1–200,  5 guesses)")

    while True:
        choice = input("\nEnter 1, 2 or 3: ").strip()
        if choice == "1":
            return 50, 10, "Easy"
        elif choice == "2":
            return 100, 7, "Medium"
        elif choice == "3":
            return 200, 5, "Hard"
        else:
            print("Please enter 1, 2 or 3.")


def play_game(score):
    """Run one round of the game. Returns updated score."""

    # Set up the round based on difficulty
    max_number, max_guesses, difficulty = get_difficulty()
    secret = random.randint(1, max_number)
    guesses_left = max_guesses

    print(f"\n🔢 I'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_guesses} guesses. Good luck!\n")

    while guesses_left > 0:
        # Show how many guesses remain
        print(f"Guesses left: {guesses_left}")

        # Get a valid number from the player
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.\n")
            continue

        # Check if the guess is in range
        if guess < 1 or guess > max_number:
            print(f"Enter a number between 1 and {max_number}.\n")
            continue

        guesses_left -= 1

        # Give feedback
        if guess == secret:
            guesses_used = max_guesses - guesses_left
            points = guesses_left * 10 + 50  # More points for fewer guesses
            score += points
            print(f"\n✅ Correct! The number was {secret}.")
            print(f"You got it in {guesses_used} guess(es).")
            print(f"+{points} points! Total score: {score}")
            return score

        elif guess < secret:
            print("📈 Too low!\n")
        else:
            print("📉 Too high!\n")

    # Player ran out of guesses
    print(f"\n❌ Out of guesses! The number was {secret}.")
    print(f"Your score stays at: {score}")
    return score


def main():
    """Main game loop — keeps playing until the player quits."""
    score = 0
    rounds = 0

    while True:
        rounds += 1
        score = play_game(score)

        print(f"\n🏆 Score after {rounds} round(s): {score}")
        print("-----------------------------------")
        again = input("Play again? (yes / no): ").strip().lower()

        if again not in ("yes", "y"):
            print(f"\nThanks for playing! Final score: {score} over {rounds} round(s).")
            print("See you next time. 👋\n")
            break


# Entry point
if __name__ == "__main__":
    main()
