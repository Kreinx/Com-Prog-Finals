import random # For shuffling words
import winsound # For playing sound on Windows
import time
def jumble(): 
    levels = [
        ['python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone'],
        ['programming', 'developer', 'function', 'variable', 'iteration', 'condition'],
        ['asynchronous', 'polymorphism', 'inheritance', 'encapsulation', 'abstraction', 'synchronization']
    ]
    lives = 3
    current_level = 0

    print("Welcome to Word Jumble!")

    while lives != 0 and current_level < len(levels):
        words = levels[current_level][:]
        random.shuffle(words)
        for word in words:
            jumbled = ''.join(random.sample(word, len(word)))
            print(f"\nLevel {current_level + 1} - The jumbled word is:", jumbled)
            guess = input("Your guess: ").strip()
            if guess.lower() == word.lower():
                print("Congratulations! You guessed it right.")
            else:
                lives -= 1
                print("Try again!")
                print(f"You have {lives} lives left.")
                if lives == 0:
                    winsound.PlaySound(r"C:\Users\Ken\Documents\Python\Final\Sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    print("Game over! The word was:", word)
                    time.sleep(6)  # Wait for the sound to finish
                    return
        current_level += 1

    if current_level == len(levels):
        print("Congratulations! You completed all levels!")

if __name__ == "__main__":
    jumble()