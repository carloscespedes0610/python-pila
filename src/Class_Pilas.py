
class Pila:
    
    def __init__(self, capacidad):
        self.capacidad=capacidad
        self.pila=list()
        self.puntero=-1
    
    def get_capacidad(self):
        return self.capacidad
    
    def Pila_Vacia(self):
            return self.pila == []
    
    def Pila_Llena(self):
        return len(self.pila)==self.capacidad
        
    def Push(self, elemento):
        if(self.Pila_Llena()):
            print("Pila Llena, el elemento "+str(elemento)+" no pudo ser agregado")
        else:
            self.pila.append(elemento)
            self.puntero=self.puntero+1
#            return "Elemento Agregado: "+str(elemento)
    
    def Pop(self):
        if(self.Pila_Vacia()):
            return "No Existe Ningun Elemento En La Pila, Pila Vacia"
        else:
            self.puntero = self.puntero - 1
            return self.pila.pop()  # = self.pila[self.puntero]
    
    def Leer_Pila(self, *elementos):
        """
            Realiza la carga inicial de elementos de la pila
        """
        for k in elementos:
            self.Push(k)
            
    def Num_Elem_Pila(self):
        """
        Devuelve el numero de elementos de la pila
        """
        return len(self.pila)
    
    def Cima(self):
        """
        Devuelve la cima de la pila, sin eliminarla
        """
        if(self.Pila_Vacia()=='true'):
            return "Pila Vacia"
        else:
            return self.pila[self.puntero]
    
    def Decapitar(self):
        if(self.Pila_Vacia()):
            return "Pila Vacia"
        else:
            self.pila.pop()
            self.puntero = self.puntero -1
            return "Decapitado Correctamente"
        
    def Eliminar_Pila(self,var_pila):
        """
        Recibe una pila y la devuelve vacia
        """
        var_pila = []
        print(var_pila)
        return var_pila
    
    def Imprimir_Pila(self):
        print("Imprimiento Pila:")
        c = self.puntero
        while(c > -1):
            print(str(self.pila[c]))
            c = c -1
            
            
    def Imprimir_Pila_Dev(self):
        print(str(self.pila)+"; posicion_puntero: "+str(self.puntero)+"; capacidad: "+str(self.capacidad))
    
    