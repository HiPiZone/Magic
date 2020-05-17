# Kalkulator napiwku
#Napisz program Kalkulator napiwku, w którym użytkownik wprowadza sumę
#ogólną z rachunku wystawionego przez restaurację. Program powinien potem
#wyświetlić dwie kwoty napiwku — w wysokości 15 i 20 procent.

rachunek = int(input("Podaj wysokosc rachunku:"))
napiwek15 = int(rachunek /(100/15))
napiwek20 = int(rachunek /(100/20))
print(napiwek15,"\n",napiwek20)
print(input("\n\n Nacisnij enter"))