from osoba import Osoba
from databaze_pojistenych import DatabazePojistenych
print("--------------------------------\n"
      "Evidence pojištěných\n"
      "--------------------------------")

databaze = DatabazePojistenych()
akce = True

while akce != 4:
    akce = int(input("Vyberte si akci:\n"
                     "1 - Přidat nového pojistného\n"
                     "2 - Vypsat všechny pojištěné\n"
                     "3 - Vyhledat pojištěného\n"
                     "4 - Konec\n"))
    print()
    if akce == 1:
        jmeno = input("Zadej jméno pojistného: ")
        prijmeni = input("Zadej příjmení pojistného: ")
        vek = input("Zadej věk: ")
        cislo = input("Zadejte telefonní číslo: ")

        pojisteny = Osoba(jmeno, prijmeni, vek, cislo)
        databaze.pridej_pojistence(pojisteny)

        print()
        input("Data byla uložena. Pokračujte libovolnou klávesou...")
        print()

    elif akce == 2:
        databaze.vypis_pojistence()

        print()
        input("Pokračujte libovolnou klávesou...")
        print()

    elif akce == 3:
        jmeno = input("Zadej jméno pojistného: ")
        prijmeni = input("Zadej příjmení pojistného: ")

        print()
        databaze.vyhledej_pojistence(jmeno, prijmeni)
        print()
        input("Pokračujte libovolnou klávesou...")

    elif akce == 4:
        break







