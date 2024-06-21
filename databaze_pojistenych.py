from osoba import Osoba
class DatabazePojistenych:

    def __init__(self):            #vytvoří seznam pojistěných osob hned po zavolání
        self.pojistenci = []

    def pridej_pojistence(self, osoba):    #přidá pojištěnou osobou
        self.pojistenci.append(osoba)

    def vypis_pojistence(self):            #vypíše pojištěné osoby
        if self.pojistenci:
            for pojistenec in self.pojistenci:
                print(pojistenec)
        else:
            print("Žádní lidé nebyli pojištěni.")

    def vyhledej_pojistence(self, jmeno, prijmeni):  #vyhledá pojištěnou osobu podle jména a příjmení
        nalezeno = False
        for pojistenec in self.pojistenci:
            if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
                print(pojistenec)
                nalezeno = True
        if not nalezeno:
            print("Tento člověk není pojištěný.")





















