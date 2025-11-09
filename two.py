import random
import winsound
import time
import tkinter as tk
from PIL import Image, ImageTk # for image handling

# preload tkinter window and jumpscare image
root = tk.Tk()
root.title("lolxd")
root.attributes("-fullscreen", True)
root.withdraw()
try:
    _scare_img = Image.open("d4c5faea-8dbd-4602-95c1-19be1f463eff.jpg")
    _scare_img = _scare_img.resize((1000, 800), Image.LANCZOS)
    _scare_photo = ImageTk.PhotoImage(_scare_img)
    label_scare = tk.Label(root, image=_scare_photo, bg="black") #Diko pa sya mafullscreen, so black nalang muna yung background
except Exception:
    label_scare = tk.Label(root, text="image failed to load")  # fallback

def jumble(): 
    global label_scare, _screen_width, scree
    levels = [
        ['python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone'],
        ['programming', 'developer', 'function', 'variable', 'iteration', 'condition'],
        ['asynchronous', 'polymorphism', 'inheritance', 'encapsulation', 'abstraction', 'synchronization']
    ]
    level_chances = [10, 25, 40]
    sanity = 100  # hidden sanity meter
    current_level = 0
    jumpscare_chance = 100.0  # kept for adjustments but not used for random jumpscares

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

    while current_level < len(levels):
        words = levels[current_level][:]
        random.shuffle(words)
        base_inc = level_chances[current_level]
        for word in words:
            jumbled = ''.join(random.sample(word, len(word)))
            print(f"\n\033[1m=+=+=+= LEVEL {current_level + 1} =+=+=+=\033[0m\nThe jumbled word is: {jumbled}")
            guess = input("Your guess: ").strip()
            if guess.lower() == word.lower():
                sanity = min(100, sanity + 5)
                jumpscare_chance = max(0.0, jumpscare_chance - (base_inc * 0.5))
                print("Congratulations! You guessed it right.")
            else:
                jumpscare_chance = min(100.0, jumpscare_chance + base_inc)
                sanity -= base_inc
                print("Wrong guess...")
                time.sleep(1)
                print("Tough luck! Stay focused.")
                time.sleep(1)

                # trigger jumpscare only when sanity is depleted
                if sanity <= 0:
                    print("Your sanity has shattered...")
                    time.sleep(1)
                    if label_scare:
                        root.deiconify()
                        label_scare.place(x=0, y=0, relwidth=1, relheight=1)                   
                        root.update()
                    try:
                        winsound.PlaySound("Sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    except Exception:
                        pass
                    time.sleep(6)
                    try:
                        label_scare.place_forget()
                        root.update()
                    except Exception:
                        pass
                    print("You couldn't continue. Game over.")
                    return
        current_level += 1
        print(f"Level {current_level} cleared. Proceeding...")
        time.sleep(1.5)

    print("Congratulations! You completed all levels without losing your mind... probably.")
    root.destroy()
if __name__ == "__main__":
    jumble()
