import tkinter as tk
import random
import time
import threading

# === WINDOW ===
root = tk.Tk()
root.title("Love Animation")
root.configure(bg="black")
root.geometry("900x600")
root.resizable(False, False)

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ==== GLOBAL CONFIG ====
WIDTH = 900
HEIGHT = 600

# ==== TEXT EFFECT ====
def fade_in_text(text, size=40, delay=0.03):
    label = tk.Label(canvas, text=text, fg="pink", bg="black", font=("Arial", size, "bold"))
    label.place(relx=0.5, rely=0.5, anchor="center")
    for i in range(0, 255, 8):
        color = f"#{i:02x}{0:02x}{i:02x}"
        label.config(fg=color)
        time.sleep(delay)
    time.sleep(0.5)
    label.destroy()

# === FLY-IN TEXT ===
def fly_in(text, size=40):
    label = tk.Label(canvas, text=text, fg="pink", bg="black", font=("Arial", size, "bold"))
    x = WIDTH
    y = HEIGHT//2
    while x > WIDTH//2:
        label.place(x=x, y=y)
        x -= 20
        time.sleep(0.01)
    time.sleep(0.4)
    label.destroy()

# === HEART RAIN ===
def heart_rain(duration=3):
    hearts = ["❤️", "💖", "💘", "💕"]
    drops = []

    for _ in range(30):
        x = random.randint(0, WIDTH)
        emoji = random.choice(hearts)
        h = canvas.create_text(x, -20, text=emoji, fill="pink", font=("Arial", 24))
        drops.append(h)

    start = time.time()
    while time.time() - start < duration:
        for h in drops:
            canvas.move(h, 0, random.randint(3, 7))
            pos = canvas.coords(h)
            if pos[1] > HEIGHT:
                canvas.coords(h, random.randint(0, WIDTH), -20)
        time.sleep(0.03)

    for h in drops:
        canvas.delete(h)

# === HEARTBEAT ===
def heartbeat(msg="I LOVE YOU"):
    heart1 = canvas.create_text(WIDTH//2, HEIGHT//2, text="💗", font=("Arial", 120))
    text1 = canvas.create_text(WIDTH//2, HEIGHT//2+120, text=msg, font=("Arial", 30), fill="pink")

    for _ in range(6):
        canvas.itemconfig(heart1, font=("Arial", 140))
        time.sleep(0.2)
        canvas.itemconfig(heart1, font=("Arial", 110))
        time.sleep(0.2)

    canvas.delete(heart1)
    canvas.delete(text1)

# === COUNTDOWN ===
def countdown():
    for n in ["3", "2", "1"]:
        fade_in_text(n, size=100, delay=0.01)

# === MAIN ANIMATION THREAD ===
def run_animation():
    countdown()

    for w in ["you", "are", "my", "love"]:
        fly_in(w)

    fade_in_text("FOREVER", 50)

    heart_rain(3)

    # ==== Nama NISA di sini ====
    heartbeat("i love 💘 you Nisa sayang")

    # Loop final heartbeat
    while True:
        heartbeat("i love 💘 you Nisa sayang")

# === RUN IN THREAD (biar window tidak freeze) ===
threading.Thread(target=run_animation, daemon=True).start()

root.mainloop()