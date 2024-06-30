import tkinter as tk
import random
from PIL import Image, ImageTk

compliments = [
    "You're awesome!", "You can achieve anything!", "You make a difference!", 
    "You're a star!", "Keep up the great work!", "You're amazing!", 
    "You light up the room!", "You're a true friend!", "You're so creative!", 
    "You're an inspiration!"
]

animal_gifs = [
    "cat_dance.gif", "dog_wave.gif", "hamster_eat.gif", 
    "parrot_dance.gif", "rabbit_jump.gif"
]

def generate_compliment():
    compliment = random.choice(compliments)
    gif_file = random.choice(animal_gifs)
    compliment_label.config(text=compliment)
    
    gif = Image.open(gif_file)
    gif_frames = []
    try:
        while True:
            gif_frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(len(gif_frames))
    except EOFError:
        pass
    
    def update_gif(ind):
        frame = gif_frames[ind]
        ind += 1
        if ind >= len(gif_frames):
            ind = 0
        gif_label.config(image=frame)
        root.after(100, update_gif, ind)
    
    update_gif(0)

root = tk.Tk()
root.title("Random Compliment Generator")
root.geometry("500x500")

compliment_label = tk.Label(root, text="", font=("Helvetica", 16))
compliment_label.pack(pady=20)

gif_label = tk.Label(root)
gif_label.pack()

generate_button = tk.Button(root, text="Generate Compliment", command=generate_compliment)
generate_button.pack(pady=20)

root.mainloop()
