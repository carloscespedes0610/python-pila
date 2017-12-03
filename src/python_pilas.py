from ejercicios_pila import *

ej= ejercicios_pila()

#pila = Pila(10)
#print("push: "+pila.Push('c'))
#print("push: "+pila.Push('a'))
#print("push: "+pila.Push('r'))
#print("push: "+pila.Push('l'))
#print("push: "+pila.Push('o'))
#print("push: "+pila.Push('s'))
#pila.Leer_Pila('a','n','a')
#pila.Imprimir_Pila()
#pila.Imprimir_Pila_Dev()
#
#print("Num_Elem_Pila: "+str(pila.Num_Elem_Pila()))
#print("Cima: "+str(pila.Cima()))
#pila.Imprimir_Pila_Dev()
#
#print("Decapitar: "+pila.Decapitar())
#pila.Imprimir_Pila_Dev()
#
#pila_var=Pila(8)
#pila_var.Leer_Pila(7,8,9)
#
#print("elminar_pila: "+str(pila.Eliminar_Pila(pila_var)))


#ej.Imprimir()

#ej.Fondo_Pila(0)

#ej.Eliminar_Ocurrencias(2)
#ej.Intercambio_tope_fondo()
#print("duplicar")
#ej.Duplicar_Contenido().Imprimir_Pila_Dev()

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




