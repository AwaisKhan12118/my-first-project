import random

words = ["python", "apple", "computer", "code", "student"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("=== Hangman Game ===")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    letter = input("Enter a letter: ").lower()

    if len(letter) != 1:
        print("Enter only one letter!")
        continue

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
  