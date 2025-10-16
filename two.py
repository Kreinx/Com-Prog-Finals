import random # For shuffling words
import winsound # For playing sound on Windows
import time
from tkinter import*
from PIL import Image, ImageTk

def jumble(): 
    levels = [
        ['python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone'],
        ['programming', 'developer', 'function', 'variable', 'iteration', 'condition'],
        ['asynchronous', 'polymorphism', 'inheritance', 'encapsulation', 'abstraction', 'synchronization']
    ]
    lives = 3
    current_level = 0

    print("This is a Totally Normal Word Game")
    time.sleep(2)
    start_game = input("Do you want to start the game? (yes/no): ").strip().lower()
    if start_game != 'yes':
        print("Maybe next time. Goodbye!")
        return
    else:
        print("Let's get started!")
        time.sleep(1)
    print("You have 3 lives. Guess the correct word to proceed to the next level.")
    time.sleep(4)
    print("If you run out of lives, the game is over.")
    time.sleep(3)
    # Game loop / playing the game
    while lives != 0 and current_level < len(levels):
        words = levels[current_level][:]
        random.shuffle(words)
        for word in words:
            jumbled = ''.join(random.sample(word, len(word)))
            print(f"\n\033[1m=+=+=+= LEVEL {current_level + 1} =+=+=+=\033[0m\nThe jumbled word is:", jumbled)
            guess = input("Your guess: ").strip()
            if guess.lower() == word.lower():
                print("Congratulations! You guessed it right.")
            else:
                lives -= 1
                print("Try again!")
                print(f"You have {lives} lives left.")
                if lives == 0:
                    winsound.PlaySound(r"Sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    print("Game over! The word was:", word)
                    time.sleep(6)  # Wait for the sound to finish
                    return
        current_level += 1

    if current_level == len(levels):
        print("Congratulations! You completed all levels!")

if __name__ == "__main__":
    jumble()