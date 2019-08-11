from memoria import *
from riferimenti import *
from processi import *



'''Metodo main, richiede l'inserimento dei dati necessari al funzionamento dell Applicativo '''
def main():


    #Schermata di Avvio
    print("\n---------------------------------------------------------------")
    print("\tSimulatore algoritmi di sostituzione delle pagine ")
    print(" \nStudente: Campanile Domenico Giacomo")
    print("Matricola: 445794")
    print("---------------------------------------------------------------")



    # ----- Dati in input -----

    pagProcessi = []    #Array per la memorizzazione delle pagine inserite per ogni processo

    totFrame = int(input("\nInserisci numero massimo di frame : "))
    minFrame = int(input("Inserisci numero minimo di frame per processo : "))

    nProcessi = int(input("\nInserisci numero di processi : "))
    for i in range(nProcessi):
        pagProcessi.append(input("Inserisci numero pagine del processo [%2d] : " % (i + 1)))

    lRiferimenti = input("\nInserisci la lunghezza della successione dei riferimento : ")

    # ----- /Dati in input -----


    #creazione processi con la propria dimensione
    processi = Processi()
    processi.crea_processo(pagProcessi,nProcessi,totFrame, minFrame)

    #creazione memoria
    memoria = Memoria(totFrame)
    memoria.crea_memoria()

    #creazione successione dei riferimenti
    riferimenti = Riferimenti()
    riferimenti.crea_successione(lRiferimenti)
    #stampa successione
    riferimenti.stampa_successione()

    # richiamo metodo cerca frame liberi in memoria
    memoria.cerca_frame_liberi(processi, riferimenti)


#avvio main
main()



#TEST
#processi.stampa_stato_processi()
#memoria.stampa_stato_memoria()
#riferimenti.stampa_successione()

