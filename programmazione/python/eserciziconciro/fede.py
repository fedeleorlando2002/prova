class veicolo:
    def __init__(self, nome, velocita , marca , prezzo, durata):
        self.nome= nome
        self.velocita = velocita
        self.marca  = marca 
        self.prezzo = prezzo
        self.durata = durata

    def dimensione(self):
        print("dimensione del veicolo")

    def altezza(self):
        print("altezza del veicolo")
     
    def qualita(self):
        if self.durata > self.marca:
          print("durata vale più della marca ")
        else:
            print("durata vale meno della marca")

class moto(veicolo):
     def ___init__(self, nome, velocita , marca , prezzo, durata, dueruote):
         self.dueruote = dueruote

     def posti(self):
         if self.dueruote:
             print("una moto ha 2 ruote")
