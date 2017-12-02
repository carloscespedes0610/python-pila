
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
        if(len(self.pila)==self.capacidad):  # = self.puntero+1==self.capacidad
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
    
    def Pop(self):
        if(self.Pila_Vacia()=='true'):
            return "No Existe Ningun Elemento En La Pila, Pila Vacia"
        else:
            self.puntero = self.puntero - 1
            return self.pila.pop()  # = self.pila[self.puntero]
    
    def Imprimir_Pila(self):
        print("Imprimiento Pila:")
        c = self.puntero
        while(c > -1):
            print(str(self.pila[c]))
            c = c -1
    def Imprimir_Pila_Dev(self):
        print(str(self.pila)+"; posicion_puntero: "+str(self.puntero)+"; capacidad: "+str(self.capacidad))
    
    