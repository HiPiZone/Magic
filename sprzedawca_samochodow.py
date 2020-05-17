# Napisz program Sprzedawca samochodów, w którym użytkownik wprowadza
#podstawową cenę samochodu. Program powinien dodać szereg dodatkowych
#opłat, takich jak podatek, opłatę rejestracyjną, prowizję przygotowawczą
#dealera, opłatę za dostarczenie. Oblicz podatek i opłatę rejestracyjną jako
#pewien procent ceny podstawowej. Pozostałe opłaty powinny mieć stałe
#wartości. Wyświetl faktyczną cenę samochodu po doliczeniu wszystkich
#dodatków.

cena_auta = int(input("Podaj cene auta: "))
podatek = int(input("podatek: "))
oplata_rejestracyjna = int(input("Oplata rejestracyjna: "))
prowizja = int(input("Prowizja przygotowawcza: "))
oplata_za_dostarczenie = int(input("Oplata za dostarczenie: "))
cena_podstawowa = cena_auta + prowizja + oplata_za_dostarczenie

minus_podatek = (20/100)
minus_rejestracja = 10/100

cena_koncowa = cena_podstawowa - minus_podatek - minus_rejestracja
print("Cena koncowa auta: ", int(cena_koncowa))
print(input("\n\n Nacisnij enter"))


