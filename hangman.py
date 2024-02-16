import random

def hangman():
    word_list = ["python", "hangman", "coding", "games"]
    chosen_word = random.choice(word_list)
    guessed_word = ["_"] * len(chosen_word)
    attempts = 6

    while attempts > 0 and "_" in guessed_word:
        print(" ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

        if "_" not in guessed_word:
            print("Congratulations! You guessed the word:", chosen_word)
            return

    print("Game over. The word was:", chosen_word)

hangman()