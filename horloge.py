import tkinter as tk
import time
import math

def update_clock():
    # Obtenir l'heure actuelle
    now = time.localtime()
    hours = now.tm_hour
    minutes = now.tm_min
    seconds = now.tm_sec

    # Affichage numérique de l'heure
    time_display.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    # Calculer les angles pour les aiguilles
    seconds_angle = math.radians(seconds * 6 - 90)
    minutes_angle = math.radians(minutes * 6 - 90)
    hours_angle = math.radians((hours % 12) * 30 + minutes * 0.5 - 90)

    # Mettre à jour les aiguilles
    canvas.coords(second_hand, 200, 200, 200 + 90 * math.cos(seconds_angle), 200 + 90 * math.sin(seconds_angle))
    canvas.coords(minute_hand, 200, 200, 200 + 70 * math.cos(minutes_angle), 200 + 70 * math.sin(minutes_angle))
    canvas.coords(hour_hand, 200, 200, 200 + 50 * math.cos(hours_angle), 200 + 50 * math.sin(hours_angle))

    # Changer la couleur de fond selon le moment de la journée
    if 6 <= hours < 18:
        canvas.config(bg="white")
        time_display.config(bg="white", fg="black")
    else:
        canvas.config(bg="black")
        time_display.config(bg="black", fg="white")

    # Mettre à jour toutes les secondes
    root.after(1000, update_clock)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Horloge Analogique et Numérique")

# Créer un canvas pour dessiner l'horloge
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Dessiner le cadran de l'horloge avec un design arrondi et des marques
canvas.create_oval(50, 50, 350, 350, width=4, outline="black")  # Bordure du cadran
for i in range(60):
    angle = math.radians(i * 6 - 90)
    x_outer = 200 + 140 * math.cos(angle)
    y_outer = 200 + 140 * math.sin(angle)
    if i % 5 == 0:  # Marques des heures
        x_inner = 200 + 120 * math.cos(angle)
        y_inner = 200 + 120 * math.sin(angle)
        canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=3, fill="black")
    else:  # Marques des minutes
        x_inner = 200 + 130 * math.cos(angle)
        y_inner = 200 + 130 * math.sin(angle)
        canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=1, fill="gray")

for i in range(12):
    angle = math.radians(i * 30 - 90)
    x = 200 + 110 * math.cos(angle)
    y = 200 + 110 * math.sin(angle)
    canvas.create_text(x, y, text=str(i if i != 0 else 12), font=("Arial", 16), fill="white")

# Ajouter les aiguilles
hour_hand = canvas.create_line(200, 200, 200, 150, width=6, fill="black", capstyle=tk.ROUND)
minute_hand = canvas.create_line(200, 200, 200, 120, width=4, fill="blue", capstyle=tk.ROUND)
second_hand = canvas.create_line(200, 200, 200, 100, width=2, fill="red", capstyle=tk.ROUND)

# Ajouter l'affichage numérique de l'heure
time_display = tk.Label(root, text="", font=("Arial", 24), bg="white")
time_display.pack()

# Démarrer l'animation
update_clock()

# Lancer la boucle principale
root.mainloop()
