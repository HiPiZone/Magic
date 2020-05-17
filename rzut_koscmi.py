# Rzut kośćmi
# Demonstruje generowanie liczb losowych

#Użyłem w programie Rzut kośćmi obu funkcji — randint() i randrange() — żeby
#pokazać dwie różne funkcje służące do generowania liczb losowych. W ogólnym
#przypadku będziesz musiał wybrać funkcję, która będzie najlepiej pasowała do
#Twoich potrzeb.


import random
# generuj liczby losowe z zakresu 1 - 6
die1 = random.randint(1, 6)
#randint() - generuje losowa liczbe calkowita
#Wykorzystujące notację z kropką wyrażenie random.randint() oznacza funkcję randint(), która należy do modułu random.
die2 = random.randrange(6) + 1
#funkcja randrange() wybiera losowo jedną z grupy sześciu liczb, a lista liczb zaczyna się od 0 - dlatego jest "+1"
total = die1 + die2
print("Wyrzuciłeś", die1, "oraz", die2, "i uzyskałeś sumę", total)
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
