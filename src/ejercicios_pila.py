from Class_Pilas import *

class ejercicios_pila:
    
    
    def __init__(self):
        self.pila = Pila(10)
        self.pila.Leer_Pila(1,2,3,4,5,6,7,8)
        
    def Imprimir(self):
        self.pila.Imprimir_Pila()
        
    def Fondo_Pila(self,elemento):
        """
        Colocar en el fondo de una pila un nuevo elemento.
        """
        pila_aux=Pila(self.pila.Num_Elem_Pila()+1)
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
        
    def Eliminar_Ocurrencias(self,elemento):
        """
            Eliminar de una pila todas las ocurrencias de un elemento dado.
        """
        pila_aux = Pila(self.pila.get_capacidad())
        
        while(not self.pila.Pila_Vacia()):
            ele = self.pila.Pop();
            if(elemento != ele ):
                pila_aux.Push(ele)
        
        self.pila = pila_aux
        
    def Intercambio_tope_fondo(self):
        """
        Intercambiar los valores del tope y el fondo de una pila
        """
        tope = 'null'
        fondo = 'null'
        pila_aux=Pila(self.pila.get_capacidad())
        while(not self.pila.Pila_Vacia()):
            if( tope == 'null'):
                tope = self.pila.Pop()
            else:
                pila_aux.Push(self.pila.Pop())
        
        while(not pila_aux.Pila_Vacia()):
            if(tope != 'null'):
                self.pila.Push(tope)
                tope = 'null'
                fondo = pila_aux.Pop()
            else:
                self.pila.Push(pila_aux.Pop())
        
        if(fondo != 'null'):
            self.pila.Push(fondo)
            
            
    
        