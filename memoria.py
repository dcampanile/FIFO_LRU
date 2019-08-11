from menu import *

'''Classe contenente dati e metodi attinenti alla Memoria Virtuale'''

class Memoria:

    '''Dati della Memoria'''
    def __init__(self, totFrame):

        self.frameMemoria = []      #array contenente i frame in memoria
        self.totFrame = totFrame    #totale frame inserito

        self.posizione = 0          #posizione frame in memoria

        self.menu = Menu()  # istanzio menu di scelta

    '''Metodo per la ricerca di frame libero, se esiste lo si usa
    inserendo il riferimento alla pagina in successione altrimenti avvia il menu
    con scelta di un algoritmo di sostituzione delle pagine'''
    def cerca_frame_liberi(self, processi, riferimenti):

        # ciclo da 0 al numero totale dei processi
        for posizione in range(len(processi.frameProcessi)):



            print("\n---------------------------------------------------------------")
            print("Processo %d di dimensione %d" % (posizione + 1, processi.frameProcessi[posizione]))

            # richiamo metodo inserimento in memoria
            self.push(processi, posizione, riferimenti)

            # TEST: stampa stato attuale della memoria
            self.stampa_stato_memoria()

            if (posizione == len(processi.frameProcessi) -1):
                print("\nLa Memoria e' in grado di contenere tutti i frame richiesti dai processi")

                #Avvio menu di scelta Nuovo Test o Modifica tot Frame
                self.menu.start_menu_2(processi,Memoria,riferimenti)


    def crea_memoria(self):

        # ----- inizializzazione memoria -----
        # inserisce "-" in posizione da 0 al totale dei frame inseriti

        for i in range(self.totFrame):
            self.frameMemoria.append("-")

        # ----- /inizializzazione memoria -----

    '''Metodo per l'inserimento delle pagine in frame in memoria'''
    def push(self, processi, i, riferimenti):

        #ciclo da 0 al numero dei frame richiesti dal processo in esame
        for j in range(processi.frameProcessi[i]):

            #riciclo successione dei riferimenti se si raggiunge la fine della successione
            if(riferimenti.ultimoRif >= len(riferimenti.successione)):

                riferimenti.ultimoRif = 0       #reset ultimo riferimento nella successione

            u = riferimenti.ultimoRif



            #se vi e' spazio in memoria
            if (self.posizione < len(self.frameMemoria)):

                self.frameMemoria[self.posizione] = riferimenti.successione[u] #inserimento pagina in frame


            else:

                # se non vi sono frame liberi in memoria
                processi.ultimoProcesso = i  # memorizzazione ultimo processo in esame
                processi.ultimoFrame = j  # memorizzazione ultimo frame inserito


                self.stampa_stato_memoria()  # TEST: stampa stato attuale memoria

                print("\n\nErrore: la memoria non puo'contenere tutti i frame richiesti dai processi")

                processi.stampa_stato_processi()  # TEST: stampa stato processo attuale

                #avvio menu di scelta algoritmo
                self.menu.start_menu(Memoria, processi, self.totFrame, self.frameMemoria, riferimenti)





            self.posizione += 1     #aggiorna posizione frame in memoria
            riferimenti.ultimoRif +=1   #aggiorna ultimo riferimento successione



    '''Metodo stampa stato della memoria attuale'''
    def stampa_stato_memoria(self):
        print("Totale frame : %d " % len(self.frameMemoria))
        print("\nStato attuale memoria :")
        for i in range(len(self.frameMemoria)):
         print(self.frameMemoria[i]),

        print("\n---------------------------------------------------------------")
