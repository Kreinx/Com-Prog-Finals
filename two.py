import random
import winsound
import time
import tkinter as tk
from PIL import Image, ImageTk # for image handling

# preload tkinter window and jumpscare image
root = tk.Tk()
root.title("lolxd")
root.attributes("-fullscreen", True)
root.withdraw()  # keep window hidden until jumpscare
try:
    _scare_img = Image.open("il_570xN.5280345482_6jab.webp")
    _scare_photo = ImageTk.PhotoImage(_scare_img)
    label_scare = tk.Label(root, image=_scare_photo) #eto yung widget para madisplay yung image sa window
    with open("Sound.wav", "rb") as f: #para mapreload yung sound pero di gumagana
        _sound_data = f.read()
except Exception:
    label_scare = tk.Label(root, text="")  # fallback

def jumble(): 
    levels = [
        ['python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone'],
        ['programming', 'developer', 'function', 'variable', 'iteration', 'condition'],
        ['asynchronous', 'polymorphism', 'inheritance', 'encapsulation', 'abstraction', 'synchronization']
    ]
    level_chances = [10, 25, 40]
    sanity = 100  # hidden sanity meter
    current_level = 0
    jumpscare_chance = 0.0  # kept for adjustments but not used for random jumpscares

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
                    time.sleep(1)
                    print("Your sanity has shattered...")
                    try:
                        root.deiconify()
                        label_scare.pack(fill="both", expand=True) #para din sa fullscreen pero di pa tapos
                        root.update()
                        root.lift() #para maforce forward yung window
                    except Exception:
                        pass
                    try:
                        winsound.PlaySound(_sound_data, winsound.SND_MEMORY)
                    except Exception:
                        pass
                    time.sleep(3)
                    try:
                        label_scare.pack_forget()
                        root.withdraw()
                    except Exception:
                        pass
                    print("You couldn't continue. Game over.")
                    return
        current_level += 1
        print(f"Level {current_level} cleared. Proceeding...")
        time.sleep(1.5)

    print("Congratulations! You completed all levels without losing your mind... probably.")

if __name__ == "__main__":
    jumble()
    root.mainloop()