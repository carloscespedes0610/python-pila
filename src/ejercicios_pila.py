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
#        pila_aux.Push(elemento)
#        lista=list()
#        while(self.pila.Pila_Vacia() != 'true'):
#            lista.append(self.pila.Pop())
#        
#        c = len(lista)-1
#        while(c > -1):
#            pila_aux.Push(lista[c])
#            c = c-1
        
        while(not self.pila.Pila_Vacia()):
            pila_aux.Push(self.pila.Pop())
        
        self.pila.Push(elemento) # introducimos primero el elemento
            
        while(not pila_aux.Pila_Vacia()):
            self.pila.Push(pila_aux.Pop())
        
        
    def Numero_Elementos(self):
        """
        Calcular el numero de elementos de una pila sin modificar su contenido
        """
        
        print(self.pila.Num_Elem_Pila())
        
#    def prueba(self):
#        pila_aux=self.pila
#        print(pila_aux.Pop())
#        self.pila.Imprimir_Pila_Dev()
#        pila_aux.Imprimir_Pila_Dev()
    
        