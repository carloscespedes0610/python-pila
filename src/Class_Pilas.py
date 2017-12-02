
class Pila:
    
    def __init__(self, capacidad):
        self.capacidad=capacidad
        self.pila=list()
        self.puntero=-1
    
    def Pila_Vacia(self):
        if self.pila == []:
            return 'true'
        else:
            return 'false'
    
    def Pila_Llena(self):
        if(self.puntero+1==self.capacidad):
            return 'true'
        else:
            return 'false'
    
    
    