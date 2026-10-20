
import random

wiederholungen = 100000
Kopf = 0
Zahl = 0
Streak = 0
MaxStreak = 0
Head = False
Number = False
GewünschteStreak = 30 # <---- Hier die gewünschte Streak eingeben, z.B. 10


while MaxStreak < GewünschteStreak: # <---- Hier die gewünschte Streak eingeben, z.B. 10
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



