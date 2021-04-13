class Kaffeeautomat:
    def __init__(self):
        self.__angeschaltet = False
        self.__Geldstand = 0

    def anschalten(self):
        self.__angeschaltet = True

    def ausschalten(self):
        self.__Geldstand = 0
        self.__angeschaltet = False

    def GeldEinWerfen(self, Betrag):
        if (self.__angeschaltet):
            self.__Geldstand += Betrag
            if (self.__Geldstand>=30):
                print("Kaffee gekocht und in Tasse gefüllt!")
                self.__Geldstand = 0
