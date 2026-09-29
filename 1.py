import random

WORDS = ["python", "hangman", "keyboard", "science", "laptop"]

HANGMAN = [
    "  -----\n  |   |\n      |\n      |\n      |\n  =====",
    "  -----\n  |   |\n  O   |\n      |\n      |\n  =====",
    "  -----\n  |   |\n  O   |\n  |   |\n      |\n  =====",
    "  -----\n  |   |\n  O   |\n /|   |\n      |\n  =====",
    "  -----\n  |   |\n  O   |\n /|\\  |\n      |\n  =====",
    "  -----\n  |   |\n  O   |\n /|\\  |\n /    |\n  =====",
    "  -----\n  |   |\n  O   |\n /|\\  |\n / \\  |\n  =====",
]

def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = []

    print("\n=== HANGMAN ===")

    while True:
        print(HANGMAN[len(wrong)])
        print("Word :", " ".join(c if c in guessed else "_" for c in word))
        print("Wrong:", ", ".join(wrong) or "None", f"({len(wrong)}/6)\n")

        if all(c in guessed for c in word):
            print(f"You win! The word was '{word}' 🎉")
            break
        if len(wrong) == 6:
            print(f"Game over! The word was '{word}' 💀")
            break

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter.\n")
        elif guess in guessed or guess in wrong:
            print("Already guessed that.\n")
        elif guess in word:
            guessed.add(guess)
            print("Correct!\n")
        else:
            wrong.append(guess)
            print("Wrong!\n")

while True:
    play()
    if input("Play again? (y/n): ").strip().lower() != "y":
        print("Bye! 👋")
        break
