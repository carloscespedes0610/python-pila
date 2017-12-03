from ejercicios_pila import *

ej= ejercicios_pila()

# Imprimir pila sin modificar su contenido ----------------------
print("-*-*-*-*-*-*-*- Imprimir pila sin modificar su contenido *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila('c','a','r','l','o','s')

ej.Imprimir(pila)
print("Pila Original, verificamos que no se modifico su contenido: ")
pila.Imprimir_Pila()
pila=[]

# Colocar en el Fondo de la pila ----------------------
print("-*-*-*-*-*-*-*- Colocar en el Fondo de la pila *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila(1,2,3,4,5,6,7,8,9)
print("Pila con elemento agregado al fondo: ")
ej.Fondo_Pila(pila,0)
pila.Imprimir_Pila()
pila=[]

# calcular el numero de elementos de una pila sin modificar su contenido -----------------
print("-*-* numeros de elementos de una pila sin modificar su contenido *-*-*-*")
pila = Pila(10)
pila.Leer_Pila('c','a','r','l','o','s')

print("Numeros de Elementos: "+str(ej.Numero_Elementos(pila)))
print("Pila Original, verificamos que no se modifico su contenido: ")
pila.Imprimir_Pila()
pila=[]

# Eliminar de una pila todas las ocurrencias de un elemento dado-------------
print("-*-*-*-*-*-*-*- eliminar las ocurrencias de un elemento de una pila *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila(1,2,3,4,5,6,7,8,9)
ej.Eliminar_Ocurrencias(pila,5)
print("Pila con elemento elminado: ")
pila.Imprimir_Pila()
pila=[]

# Intercambiar los valores del tope y el fondo de una pila-------------
print("-*-*-*-*-*-*-*- Intercambiar tope y fondo de una pila *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila(1,2,3,4,5,6,7,8,9)
ej.Intercambio_tope_fondo(pila)
print("Pila con tope y fondo intercambiado: ")
pila.Imprimir_Pila()
pila=[]

# Duplicar el contenido de una pila--------------------------------------------
print("-*-*-*-*-*-*-*- Duplicar el contenido de una pila *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila(0,1,2,3,4,5,6,7,8,9)
print("Pila con elementos duplicados: ")
ej.Duplicar_Contenido(pila).Imprimir_Pila()
pila=[]

# es palindrome -----------------------------------------
print("-*-*-*-*-*-*-*- es palindrome *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila('s','e','d','e','p','s','e','c') # cespedes
#pila.Leer_Pila('a','n','a')
pila.Imprimir_Pila()
print("es palindrome: "+str(ej.es_palindrome(pila)))
pila = []

# suma de enteros ----------------------------------------
print("-*-*-*-*-*-*-*- suma de elementos *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila(1,2,3,4,5,6,7,8,9)
print("La suma de los Elementos es: "+str(ej.Suma_Elementos(pila)))
pila = []

# Invertir Pila ----------------------------------------
print("-*-*-*-*-*-*-*- Invertir Pila *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila(1,2,3,4,5,6,7,8,9)
print("Pila Original:")
pila.Imprimir_Pila()
print("Pila Invertida:")
ej.Invertir_Pila(pila).Imprimir_Pila()
pila = []

# Existe_en_Pila ----------------------------------------
print("-*-*-*-*-*-*-*- Existe_en_Pila *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila(1,2,3,4,5,6,7,8,9)
print("El Elemento existe en la Pila: "+str(ej.Existe_en_Pila(pila,5)))
pila = []

# Interseccion ----------------------------------------
print("-*-*-*-*-*-*-*- Interseccion *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila(1,2,3,4,5,6,7,8,9)
pila2 = Pila(4)
pila2.Leer_Pila(7,10,9,5)
print("Pila Resultante de la Interseccion: ")
ej.Interseccion(pila,pila2).Imprimir_Pila()
pila = []
pila2 = []

# Union ----------------------------------------
print("-*-*-*-*-*-*-*- Union *-*-*-*-*-*-*-*-*-*-*-*-*")
pila = Pila(10)
pila.Leer_Pila(1,2,3,4,5)
pila2 = Pila(4)
pila2.Leer_Pila(6,7,8,9)
print("Pila Resultante de la Union: ")
ej.Union(pila,pila2).Imprimir_Pila()
pila = []
pila2 = []

print("-*-*-*-*-*-*-*- Fin *-*-*-*-*-*-*-*-*-*-*-*-*")
print("Alumno: Carlos Alberto Cespedes Soliz")

