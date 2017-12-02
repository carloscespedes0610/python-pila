from Class_Pilas import *

pila = Pila(2)
print("pila vacia: "+pila.Pila_Vacia())
print("pila llena: "+pila.Pila_Llena())
print("push: "+pila.Push(8))
print("push: "+pila.Push(2))
print("push: "+pila.Push(5))
#print("pop: "+str(pila.Pop()))
pila.Imprimir_Pila()
pila.Imprimir_Pila_Dev()
