'''Classe contenente dati e metodi algoritmo FIFO'''
class Fifo:

    '''Dati Algoritmo'''
    def __init__(self):

        self.vittima = -1  # pagina "vittima" da sostituire inizializzata a -1
        self.page_faults = 0  # numero totale dei page fault verificati


    def start_fifo(self,processi, totFrame, frameMemoria, riferimenti):

        # esegui algoritmo FIFO per ogni processo e frame rimasti non allocati in memoria
        for posizione in range(len(processi.frameProcessi) - processi.ultimoProcesso):

            p = processi.ultimoFrame  # leggo ultimo frame del processo interrotto

            u = posizione + processi.ultimoProcesso  # leggo posizione ultimo processo interrotto

            # leggo dimensione di ogni processo
            dimProcesso = int(processi.frameProcessi[u] - p)

            # Stampa info
            print("\n\n----- Processo %d di pagine rimanenti %d -----" % (posizione + processi.ultimoProcesso + 1, dimProcesso))

            # ciclo da 0 alla dimensione calcolata del processo in esame
            for i in range(dimProcesso):

                controllore = 0  # variabile di controllo pagine

                # riciclo successione dei riferimenti se si raggiunge la fine della successione
                if (riferimenti.ultimoRif >= len(riferimenti.successione)):
                    riferimenti.ultimoRif = 0  # reset ultimo riferimento nella successione

                u = riferimenti.ultimoRif

                # Controllo presenza riferimento pagina in esame in memoria
                for j in range(totFrame):

                    # se il riferimento e' gia' presente in memoria modifica variabile controllore ad 1
                    if (frameMemoria[j] == riferimenti.successione[u]):
                        controllore = 1
                        break

                # se controllore e' uguale a 0, vi e' un page fault
                if controllore == 0:

                    # calcola la posizione della pagina "vittima" da sostituire
                    # ovvero la pagina presente in memoria da piu' tempo
                    self.vittima = (self.vittima + 1) % totFrame

                    # sostituisce la pagina vittima con il riferimento in esame
                    # nella posizione calcolata
                    frameMemoria[self.vittima] = riferimenti.successione[u]

                    # incrementa page_fault
                    self.page_faults += 1

                    # Stampa il riferimento in esame
                    print("\n%d ->" % (riferimenti.successione[u])),

                    # Stampa i riferimenti delle pagine presenti in memoria
                    # o "-" se non ve ne sono
                    for j in range(totFrame):
                        if frameMemoria[j] != "-":
                            print(frameMemoria[j]),
                        else:
                            print("-"),

                elif controllore == 1:

                    # Non vi sono Page Fault
                    print("\n%d -> No Page Fault" % (riferimenti.successione[u])),

                # incremento posizione ultimo riferimento
                riferimenti.ultimoRif += 1




        # stampa numero totale di Page Fault
        print("\n\n---------------------------------------------------------------")
        print("\nTotale Page Faults : %d." % (self.page_faults))
        print("---------------------------------------------------------------")

        processi.ultimoFrame = 0    #reset ultimo frame
