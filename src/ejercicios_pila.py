from Class_Pilas import *

class ejercicios_pila:
    
    
    def __init__(self):
        self.pila = Pila(10)
        self.pila.Leer_Pila(1,2,3,4,5)
        
    def Imprimir(self):
        self.pila.Imprimir_Pila()
        
    def Fondo_Pila(self,elemento):
        """
        Colocar en el fondo de una pila un nuevo elemento.
        """
        pila_aux=Pila(self.pila.Num_Elem_Pila()+1)
        pila_aux.Push(elemento)
#        lista=list()
#        while(self.pila.Pila_Vacia() != 'true'):
#            lista.append(self.pila.Pop())
#        
#        c = len(lista)-1
#        while(c > -1):
#            pila_aux.Push(lista[c])
#            c = c-1
        
        while(self.pila.Pila_Vacia() != 'true'):
            pila_aux.Push(self.pila.Pop())
        
        self.pila = pila_aux
        
    def Numero_Elementos(self):
        """
        Calcular el numero de elementos de una pila sin modificar su contenido
        """
        
        print(self.pila.Num_Elem_Pila())
    
        