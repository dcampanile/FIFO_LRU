from __future__ import division

'''Classe contenente dati e metodi attinenti ad ogni processo'''

class Processi:

    '''Dati classe'''
    def __init__(self):

        self.frameProcessi = []     #array contenente frame richiesti da ogni processo
        self.sumPagine = 0          #sommatoria necessaria al calcolo della dimensione del processo

        self.ultimoProcesso = 0     #ultimo processo in esame
        self.ultimoFrame = 0        #ultimo frame analizzato di un processo

    '''Metodo creazione processo con calcolo della dimensione in frame date le pagine richieste'''
    def crea_processo(self,pagProcessi, nProcessi, totFrame, minFrame):

        # Sommatoria delle pagine dei processi inserite
        for i in range(nProcessi):
            self.sumPagine += pagProcessi[i]

        # Numero di frame da assegnare al processo
        for j in range(nProcessi):

            # Frame da assegnare ad ogni processo ai = si/sommatoria(si) x m
            ai = round((pagProcessi[j] / self.sumPagine) * totFrame)

            #se la dimensione calcolata e' minore del numero minimo di frame richiesto
            if (ai < minFrame):
                ai = minFrame   #assegna a dimensione il numero minimo di frame

            #inserisci la dimensione del processo i array
            self.frameProcessi.append(int(ai))  # Inserisco risultato su array

    '''Metodo di stampa stato attuale processo'''
    def stampa_stato_processi(self):

        print("\nUltimo processo letto: %d su %d" % (self.ultimoProcesso + 1, len(self.frameProcessi)))
        print("Ultimo frame inserito del processo : %d su %d" % (self.ultimoFrame, self.frameProcessi[self.ultimoProcesso]))

        #TEST: STAMPA DIMENSIONE ASSEGNATA AD OGNI PROCESSO
       # for i in range(len(self.frameProcessi)):
       #     print("Dimensione processo %d : %d" % (i +1,self.frameProcessi[i]))