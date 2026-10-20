
import random

wiederholungen = 100000
Kopf = 1 # Wir müssen Kopf oder Zahl auf 1 setzen, damit die while Schleife nicht sofort abbricht, da wir wollen, dass die Schleife läuft, bis Kopf und Zahl gleich sind
Zahl = 0
Streak = 0
MaxStreak = 0
Head = False
Number = False
GewünschteStreak = 30 # <---- Hier die gewünschte Streak eingeben, z.B. 10


while not Kopf == Zahl:
    # Zufällige Zahl zwischen 1 und 2 generieren
    zahl = random.randint(1, 2)

    # Ausgabe der Zahl
    #print(zahl). <----- Mach Komma weg, wenn du die Ausgabe nicht sehen willst, sonst wird der PC sehr langsam
    if zahl == 1:
        Kopf += 1
        Head = True
        Streak += 1
        if Number:
            Streak = 1
            Number = False
        if Streak > MaxStreak:
                    MaxStreak = Streak
        
        
               
        
    elif zahl == 2:
        Zahl += 1
        Number = True
        Streak += 1
        if Head:
            Streak = 1
            Head = False
        if Streak > MaxStreak:
                    MaxStreak = Streak
        

print("Kopf:", Kopf)
print("Zahl:", Zahl)
print("Maximale Streak:", MaxStreak)



