
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
        
    def Push(self, elemento):
        if(self.Pila_Llena()=='true'):
            return "Pila Llena, el elemento "+str(elemento)+" no pudo ser agregado"
        else:
            self.pila.append(elemento)
            self.puntero=self.puntero+1
            return "elemento agregado"
    
    def Imprimir_Pila(self):
        print(str(self.pila)+"; posicion_puntero: "+str(self.puntero)+"; capacidad: "+str(self.capacidad))
    
    