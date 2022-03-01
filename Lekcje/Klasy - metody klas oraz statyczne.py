class Czlowiek:
    def __init__(self,imie):
        self.imie = imie

    def przedstaw(self):
        print("Nazywam sie " + self.imie)

    @classmethod
    def nowy_czlowiek(cls,imie):
        return cls(imie)

    @staticmethod
    def przywitaj(arg):
        print("Czesc " + arg)


cz1 = Czlowiek.nowy_czlowiek("Szymon")
cz1.przedstaw()
cz2 = cz1.nowy_czlowiek("Seba")
cz2.przedstaw()

Czlowiek.przywitaj("przyjacielu!")
cz2.przywitaj("człowieku.")
