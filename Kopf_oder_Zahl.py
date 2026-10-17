
import random

wiederholungen = 100000
Kopf = 0
Zahl = 0
Streak = 0
MaxStreak = 0
Head = False
Number = False


for i in range(wiederholungen):
    # Zufällige Zahl zwischen 1 und 2 generieren
    zahl = random.randint(1, 2)

    # Ausgabe der Zahl
    #print(zahl). <----- Mach Komma weg, wenn du die Ausgabe nicht sehen willst, sonst wird der PC sehr langsam
    if zahl == 1:
        Kopf += 1
        Head = True
        Streak += 1
        if Streak > MaxStreak:
            MaxStreak = Streak
        if Number:
            Streak = 1
            Number = False
        
        
               
        
    elif zahl == 2:
        Zahl += 1
        Number = True
        Streak += 1
        if Streak > MaxStreak:
            MaxStreak = Streak
        if Head:
            Streak = 1
            Head = False
        

print("Kopf:", Kopf)
print("Zahl:", Zahl)
print("Maximale Streak:", MaxStreak)



