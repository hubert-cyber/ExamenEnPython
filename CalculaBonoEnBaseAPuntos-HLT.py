#definir variables
print("Problema 2")
#datos de entrada
salario= 950
puntosP=int(input("Ingrese sus puntos obtenidos:"))
#Procedimiento
if puntosP >=0 and puntosP <=100 :
  premio = salario * 0.10
elif puntosP >= 101 and puntosP <=150 :
  premio = salario * 0.40
elif puntosP >=151 :
  premio = salario * 0.70
#Datos de Salida
print("El bono que le corresponde es:",premio)