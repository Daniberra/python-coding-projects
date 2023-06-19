import random

player_score = 0
computer_score = 0


def hangedman(hangman):
    graphic = [
        """
        +-------+
        |
        |
        |
        |
        |
    ==============
    """,
        """
        +-------+
        |       |
        |       0
        |
        |
        |
    ==============
    """,
        """
        +-------+
        |       |
        |       0
        |       |
        |      
        |
    ==============
    """,
        """
        +-------+
        |       |
        |       0
        |      -|
        |      
        |
    ==============
    """,
        """
        +-------+
        |       |
        |       0
        |      -|-
        |      
        |
    ==============
    """,
        """
        +-------+
        |       |
        |       0
        |      -|-
        |      
        |
    ==============
    """,
        """
        +-------+
        |       |
        |       0
        |      -|-
        |      /
        |
    ==============
    """,
        """
        +-------+
        |       |
        |       0
        |      -|-
        |      / \
        |
    ==============
    """
    ]

    print(graphic[hangman])


def start():
    print("Let's play a game of linux themed hangman!")
    while game():
        pass
    scores()
    play_again()


def game():
    dictionary = ["gnu", "kernel", "linux", "magela", "penguin", "ubuntu"]
    word = random.choice(dictionary)
    word_length = len(word)
    clue = list("_" * word_length)
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_wrong = 0
    global computer_score, player_score

    while letters_wrong < tries and "_" in clue:
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letter in letters_tried:
                print("You have already picked", letter)
            else:
                letters_tried += letter
                if letter in word:
                    print("Congratulations! ", letter, "is correct.")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
                else:
                    letters_wrong += 1
                    print("Oops,", letter, "is not in the word.")

        else:
            print("Invalid input. Please enter a single letter.")

        guesses += 1
        hangedman(letters_wrong)
        print(" ".join(clue))
        print("Guesses:", guesses)

    if letters_wrong == tries:
        print("Game over.")
        print("The word was", word)
        computer_score += 1
    else:
        print("You win!")
        print("The word was", word)
        player_score += 1

    return False


def guess_letter():
    print()
    letter = input("Take a guess at a letter: ")
    letter = letter.strip().lower()
    print()
    return letter


def play_again():
    answer = input("Would you like to play again? (y/n): ").lower()
    if answer == 'y':
        start()
    else:
        print("Thank you for playing! See you next time!")


def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)

if __name__ == '__main__':
    start()
