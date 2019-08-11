class LRU:

    def __init__(self):

        self.vittima = 0      #posizione pagina da sostituire
        self.page_faults = 0 #totale page fault

    def start_lru(self,processi, totFrame, frameMemoria, riferimenti):

        # richiama algoritmo FIFO per ogni processo e frame rimasti non allocati in memoria
        for posizione in range(len(processi.frameProcessi) - processi.ultimoProcesso):

            p = processi.ultimoFrame  # leggo ultimo frame del processo interrotto

            u = posizione + processi.ultimoProcesso  # posizione ultimo processo interrotto

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

                    # se il frame in memoria di posizione "vittima" non e' vuoto
                    if frameMemoria[self.vittima] != "-":

                        min = 999

                        for k in range(totFrame):
                            controllore = 0
                            j = u  # riferimento attuale
                            while j >= 0:
                                j -= 1  # riferimento precedente

                                # se il riferimento precedente e' presente in memoria
                                #  modifica variabile controllore ad 1
                                if (frameMemoria[k] == riferimenti.successione[j]):
                                    controllore = 1
                                    break
                            # se controllore e' uguale a 1
                            if (controllore == 1 and min > j):
                                min = j
                                self.vittima = k  # aggiorno posizione pagina da sostituire

                    frameMemoria[self.vittima] = riferimenti.successione[u]  # sostituzione pagina
                    self.vittima = (self.vittima + 1) % totFrame
                    self.page_faults += 1

                    print("\n%d ->" % (riferimenti.successione[u])),  # stampa riferimento in esame

                    # Stampa i riferimenti delle pagine presenti in memoria
                    # o "-" se non ve ne sono
                    for j in range(totFrame):
                        if frameMemoria[j] != -1:
                            print(frameMemoria[j]),
                        else:
                            print("-"),

                else:

                    # Non vi sono Page Fault
                    print("\n%d -> No Page Fault" % (riferimenti.successione[u])),

                # incremento posizione ultimo riferimento
                riferimenti.ultimoRif += 1



        # stampa numero totale di Page Fault
        print("\n---------------------------------------------------------------")
        print("\nTotale Page Faults : %d." % (self.page_faults))
        print("---------------------------------------------------------------")

        processi.ultimoFrame = 0  # reset ultimo frame
