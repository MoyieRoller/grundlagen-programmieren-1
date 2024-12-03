# AUFGABE 1: Rechnet 33.5°C in Fahrenheit und Kelvin um.

# Grad Celsius in Variable schreiben:
c = 33.5

# In gegebene Formeln einsetzen:
f = (c * 1.8) + 32
k = (f + 459.67) * (5/9)

print("Aufgabe 1")
print("T in Fahrenheit: " + str(f))
print("T in Kelvin: " + str(k))
print( )

# AUFGABE 2: Rechnet 3 Meter in Zoll (Inches) um.

# Meter direkt in Zentimeter umrechnen, 3m = 300cm:
m = 300

i = m / 2.54

print("Aufgabe 2")
print("3 Meter sind " + str(i) + " Zoll.")
print()

#AUFGABE 3: Berechnet die Summe der Zahlen von 1 bis 100.

# Jetzt könnte man mit der Gauss-Formel arbeiten, dann würde das so aussehen:
n = 100
z = (n * (n + 1)) / 2

print("Aufgabe 3")
print(int(z))

# Wenn man jetzt aber die Aufgabe nicht ganz genau anschaut und schonmal programmiert hat, kann es leicht sein, dass man anfängt mit Kanonen auf Spatzen zu schießen... uppsi
y = 0
for x in range(1, 101):
    y = y + x

print(y)