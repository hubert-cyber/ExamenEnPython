#Problema 4
print("Problema 4")
''' cabe resaltar que para la operacion de potencia use el modulo ( ** )'''
#datos de entrada
multiA=int(input("Ingrese el primer numero para hacer la operacion aritmetica → "))
multiB=input("Ingrese el signo para hacer la operacion aritmetica → ")
multiC=int(input("Ingrese el segundo segundo numero para hacer la operacion aritmetica → "))
#Procedimiento
if multiB == '+' and multiB == '-':
    resultado= multiA + multiC
if multiB == '-' :
    resultado=multiA - multiC
if multiB == '*':
    resultado=multiA * multiC
if multiB =='/':
    resultado=multiA / multiC
if multiB =='**':
    resultado= multiA ** multiC
#Datos de Salida
print("Su resultado es:",resultado)







