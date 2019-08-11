import os
import sys
from fifo import *
from lru import *

'''Classe di creazione Menu' di scelta algoritmo di sostituzione delle pagine'''
class Menu:

    '''Metodo creazione e avvio menu'''
    def start_menu(self, Memoria, processi, totFrame, frameMemoria, riferimenti):

        while True:

            print("\n Seleziona l'algoritmo di sostituzione pagine desiderato o annulla l'operazione")
            print(" 0. Annulla.")
            print(" 1. FIFO.")
            print(" 2. LRU.")
            print(" 3. Modifica totale frame.")

            ch = input(" \nSeleziona : ")

            if ch == 0:

                #Restart applicativo
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

            if ch == 1:
                print("\n------------------- Algoritmo FIFO -----------------------------")

                # creazione istanza algoritmo Fifo()
                algo_FIFO = Fifo()




                #richiamo metodo start_fifo
                algo_FIFO.start_fifo( processi, totFrame, frameMemoria, riferimenti)



            if ch == 2:
                print("\n------------------- Algoritmo LRU ------------------------------")

                # creazione istanza algoritmo LRU()
                algo_LRU = LRU()


                # richiamo metodo start_fifo
                algo_LRU.start_lru(processi, totFrame, frameMemoria, riferimenti)

            if ch == 3:
                totFrame = int(input("\nInserisci numero massimo di frame : "))

                # reset parametri ultimo processo e ultimo frame
                processi.ultimoProcesso = 0
                processi.ultimoFrame = 0

                # creazione memoria
                memoria = Memoria(totFrame)
                memoria.crea_memoria()

                # richiamo metodo cerca frame liberi in memoria
                memoria.cerca_frame_liberi(processi, riferimenti)

                # stampa stato attuale memoria
                memoria.stampa_stato_memoria()


            # se la scelta non e' valida
            if ch > 3 or ch < 0:
                print("Selezione non valida")



    def start_menu_2(self,processi, Memoria, riferimenti):

        print("\n Seleziona una scelta")
        print(" 0. Nuovo Test.")
        print(" 1. Modifica totale frame.")

        ch = input(" \nSeleziona : ")

        if ch == 0:
            # Restart applicativo
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

        if ch == 1:
            totFrame = int(input("\nInserisci numero massimo di frame : "))

            # reset parametri ultimo processo e ultimo frame
            processi.ultimoProcesso = 0
            processi.ultimoFrame = 0

            # creazione memoria
            memoria = Memoria(totFrame)
            memoria.crea_memoria()

            # richiamo metodo cerca frame liberi in memoria
            memoria.cerca_frame_liberi(processi, riferimenti)

            # stampa stato attuale memoria
            memoria.stampa_stato_memoria()
