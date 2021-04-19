import os
from pilas import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/=":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            
diccionario = dict()

def en_orden(arbol):
    if arbol == None:
        return ''
    elif arbol.valor in ['+', '-', '*', '/']:
        return "(" + en_orden(arbol.izq) + str(arbol.valor) + en_orden(arbol.der) + ")"
    else:
        return str(arbol.valor)

def resp(arbol): 
    
    return str(en_orden(arbol)) +' = '+ str(evaluar(arbol))

def evaluar(arbol):
    
    if arbol == None:
        pass
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor == "=":
        diccionario[arbol.der.valor]=evaluar(arbol.izq)
        return str(arbol.der.valor)+" = "+str(evaluar(arbol.izq))
   
    return int(arbol.valor)

    

f = open ('entradas.txt','r')
op = f.read().split()
print(op)
f.close()

pila = Pila()

convertir(op, pila)
t = open ('salida.txt','w')

while (pila.es_vacia() != True):   
    t.write(resp(pila.desapilar()) + os.linesep)
  #print(pila.es_vacia())
    
t.close()
print(diccionario.items())





