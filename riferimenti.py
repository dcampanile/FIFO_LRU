from random import randint

class Riferimenti:



    def __init__(self):

        self.successione = []
        self.ultimoRif = 0

    def crea_successione(self, lunghezza):

        for i in range(lunghezza):

            self.successione.append(randint(0, 9))



    def stampa_successione(self):

        print("\nSuccessione dei riferimenti creata :")
        for i in range(len(self.successione)):
            print(self.successione[i]),


