# obliczanie wieku
# w skundach

age = int(input("Ile masz lat? "))
rokDni = int(input("Ile dni ma rok? "))
dzien = int(input("Ile dzien ma godzin? "))
godzina = int(input("Ile godzina ma minut? "))
minuta = int(input("Ile minuta ma sekund? "))
seconds = age * rokDni * dzien * godzina * minuta
print("zyjesz juz: ", seconds)