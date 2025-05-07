"""
Mikkia Newsome
May 2025
CTEC450 Guess the Word game final
Star Wars edition
"""
import random

def get_guess():
    while True:
        guess = input("Guess: ").strip()
        if len(guess) != 1:
            print("Your guess must have exactly one character!")
        elif not guess.islower() or not guess.isalpha():
            print("Your guess must be a lowercase letter!")
        else:
            return guess

def update_dashes(secret_word, dashes, guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result

def play_game():
    words = ["deathstar", "jedi", "wookie", "ewok", "falcon", "lukeskywalker", "darthvador", "sithlord"]
    secret_word = random.choice(words)
    dashes = "-" * len(secret_word)
    guesses_left = 10
    guessed_letters = set()

    print("Welcome to Mikkia's Guess the Word Game!")
    print("How to play: Guess one lowercase letter at a time. You have 10 chances to guess wrong.")
    print(f"The secret word has {len(secret_word)} letters.")

    while dashes != secret_word and guesses_left > 0:
        print(dashes)
        print(f"{guesses_left} incorrect guesses left.")
        guess = get_guess()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("That letter is in the word!")
            dashes = update_dashes(secret_word, dashes, guess)
        else:
            print("That letter is not in the word.")
            guesses_left -= 1

    if dashes == secret_word:
        print(f"Congrats! You win. The word was: {secret_word}")
    else:
        print(f"You lose. The word was: {secret_word}")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()



