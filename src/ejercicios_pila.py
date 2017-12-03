from Class_Pilas import*

class ejercicios_pila:
    
    def __init__(self):
        self.pila = Pila(10)
        self.pila.Leer_Pila(1,2,3,4,5,6,7,8)
        
    def Imprimir(self, var_pila):
        var_pila.Imprimir_Pila()
        
    def Fondo_Pila(self,var_pila,elemento):
        """
        Colocar en el fondo de una pila un nuevo elemento.
        """
        pila_aux=Pila(var_pila.Num_Elem_Pila()+1)
        while(not var_pila.Pila_Vacia()):
            pila_aux.Push(var_pila.Pop())
        
        var_pila.Push(elemento) # introducimos primero el elemento
            
        while(not pila_aux.Pila_Vacia()):
            var_pila.Push(pila_aux.Pop())
        
        
    def Numero_Elementos(self,var_pila):
        """
        Calcular el numero de elementos de una pila sin modificar su contenido
        """
        
        print(var_pila.Num_Elem_Pila())
        
    def Eliminar_Ocurrencias(self,var_pila,elemento):
        """
            Eliminar de una pila todas las ocurrencias de un elemento dado.
        """
        pila_aux = Pila(var_pila.get_capacidad())
        while(not var_pila.Pila_Vacia()):
            ele = var_pila.Pop();
            if(elemento != ele ):
                pila_aux.Push(ele)
        
        pila_aux.Imprimir_Pila()
        var_pila = pila_aux
        
        
    def Intercambio_tope_fondo(self,var_pila):
        """
        Intercambiar los valores del tope y el fondo de una pila
        """
        tope = 'null'
        fondo = 'null'
        pila_aux=Pila(var_pila.get_capacidad())
        while(not var_pila.Pila_Vacia()):
            if( tope == 'null'):
                tope = var_pila.Pop()
            else:
                pila_aux.Push(var_pila.Pop())
        
        while(not pila_aux.Pila_Vacia()):
            if(tope != 'null'):
                var_pila.Push(tope)
                tope = 'null'
                fondo = pila_aux.Pop()
            else:
                var_pila.Push(pila_aux.Pop())
        
        if(fondo != 'null'):
            var_pila.Push(fondo)
    
    def Duplica_Contenido_Auxiliar(self,var_pila):
        # motodo que devuelve una pila inversa o sea con puros push()
        pila_aux = Pila(var_pila.get_capacidad())
        pila2 = Pila(var_pila.get_capacidad())
        while(not var_pila.Pila_Vacia()):
            elemento = var_pila.Pop()
            pila_aux.Push(elemento)
            pila2.Push(elemento)
        
        # como python funciona con puntero, el parametro se modifico, entonces
        # volveremos a dejarlo como estaba
        while(not pila2.Pila_Vacia()):
            var_pila.Push(pila2.Pop())

        return pila_aux
        
    
    def Duplicar_Contenido(self,var_pila):
        # obtenemos 2 pila iguales inversas
        pila_dup = self.Duplica_Contenido_Auxiliar(var_pila)
        pila_dup2 = self.Duplica_Contenido_Auxiliar(var_pila)
        
        pila_fin = Pila(var_pila.get_capacidad()*2)
        
        while(not pila_dup.Pila_Vacia()):
            pila_fin.Push(pila_dup.Pop())
            # verificamos si la primera pila ya se termino
            if(pila_dup.Pila_Vacia()):
                # si termino, le pasamos la proxima para q asi sea doble
                pila_dup = pila_dup2
            
        return pila_fin
    
    def es_palindrome(self,var_pila):
        """
        Verificar si el contenido de una pila de caracteres es un palindrome.
        palindrome: palabra invertida es igual a la original ej ana, sos, coco
        """
        pila_dup = self.Duplica_Contenido_Auxiliar(var_pila)
        pila_copia_ori = self.Duplica_Contenido_Auxiliar(pila_dup)
        while(not pila_copia_ori.Pila_Vacia()):
            if pila_dup.Pop() != pila_copia_ori.Pop():
                return False
        
        if(self.pila.Pila_Vacia()):
            return False
        else:
            return True
        
    def Suma_Elementos(self, var_pila):
        """
        Calcular la suma de una pila de enteros sin modificar su contenido.
        """
        pila_dup = self.Duplica_Contenido_Auxiliar(var_pila)
        suma=0
        while(not pila_dup.Pila_Vacia()):
            suma = suma + int(pila_dup.Pop())
        
        return suma
    
    def Invertir_Pila(self,var_pila):
        """
        Invertir los elementos de una pila
        """
        
        return self.Duplica_Contenido_Auxiliar(var_pila)
    
    def Existe_en_Pila(self,var_pila,elemento):
        pila_dup = self.Duplica_Contenido_Auxiliar(var_pila)
        while(not pila_dup.Pila_Vacia()):
            if(pila_dup.Pop()==elemento):
                return True
            
        return False
    
    def Interseccion(self,var_pila1,var_pila2):
        """
        Realizar la interseccion de dos pilas
        """
        
        # pila_dup1 contendra la pila con mayor elementos
        
        if(var_pila1.Num_Elem_Pila() > var_pila2.Num_Elem_Pila()):
            pila_dup1 = self.Duplica_Contenido_Auxiliar(var_pila1)
            pila_dup2 = self.Duplica_Contenido_Auxiliar(var_pila2)
        else:
            pila_dup1 = self.Duplica_Contenido_Auxiliar(var_pila2)
            pila_dup2 = self.Duplica_Contenido_Auxiliar(var_pila1)
        
        resultado = Pila(pila_dup2.get_capacidad()) # capacidad de las menores de las pilas
        
        while(not pila_dup2.Pila_Vacia()): #recorremos la pila menor
            elemento = pila_dup2.Pop()
            if(self.Existe_en_Pila(pila_dup1,elemento)):
                resultado.Push(elemento)
                
        return resultado   
    
    def Union(self,var_pila1,var_pila2):
        """
        Realizar la union de dos pilas
        """
        
        pila_dup1 = self.Duplica_Contenido_Auxiliar(var_pila1)
        pila_dup2 = self.Duplica_Contenido_Auxiliar(var_pila2)
        
        resultado = Pila(pila_dup1.get_capacidad()+ pila_dup2.get_capacidad()) 
        
        while(not pila_dup1.Pila_Vacia()): 
            resultado.Push(pila_dup1.Pop())
        
        while(not pila_dup2.Pila_Vacia()): 
            resultado.Push(pila_dup2.Pop())
                
        return resultado   
        
        
        