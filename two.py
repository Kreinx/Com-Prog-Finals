import random # For shuffling words
import winsound # For playing sound on Windows
import time

def jumble(): 
    levels = [
        ['python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone'],
        ['programming', 'developer', 'function', 'variable', 'iteration', 'condition'],
        ['asynchronous', 'polymorphism', 'inheritance', 'encapsulation', 'abstraction', 'synchronization']
    ]
    # per-level base chance increment (%) and sanity deduction (%) for each wrong guess
    level_chances = [10, 25, 40]  # level 1, 2, 3
    sanity = 100  # hidden sanity meter
    current_level = 0
    jumpscare_chance = 0.0  # current probability (%)

    print("This is a Totally Normal Word Game")
    time.sleep(1)
    start_game = input("Do you want to start the game? (yes/no): ").strip().lower()
    if start_game != 'yes':
        print("Maybe next time. Goodbye!")
        return
    else:
        print("Let's get started!")
        time.sleep(1)
    print("Guess the correct word to proceed to the next level.")
    time.sleep(1)
    print("Be wary: every wrong guess increases the chance of a surprise. Stay sane...")
    time.sleep(2)

    # Game loop
    while current_level < len(levels):
        words = levels[current_level][:]
        random.shuffle(words)
        base_inc = level_chances[current_level]
        for word in words:
            jumbled = ''.join(random.sample(word, len(word)))
            print(f"\n\033[1m=+=+=+= LEVEL {current_level + 1} =+=+=+=\033[0m\nThe jumbled word is:", jumbled)
            guess = input("Your guess: ").strip()
            if guess.lower() == word.lower():
                # correct: sanity + and slight - to jumpscare chance
                sanity = min(100, sanity + 5)
                jumpscare_chance = max(0.0, jumpscare_chance - (base_inc * 0.5))
                print("Congratulations! You guessed it right.")
            else:
                # wrong: increase jumpscare chance and reduce sanity (both hidden)
                jumpscare_chance = min(100.0, jumpscare_chance + base_inc)
                sanity -= base_inc
                print("Wrong guess...")
                time.sleep(1)
                print("Tough luck! Stay focused.")
                time.sleep(1)

                # Only trigger jumpscare when sanity is depleted
                if sanity <= 0:
                    print("Your sanity has shattered...")
                    try:
                        winsound.PlaySound("Jumpscare.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    except Exception:
                        pass
                    time.sleep(3)
                    print("You couldn't continue. Game over.")
                    return
        current_level += 1
        print(f"Level {current_level} cleared. Proceeding...")
        time.sleep(1.5)

    print("Congratulations! You completed all levels without losing your mind... probably.")

if __name__ == "__main__":
    jumble()