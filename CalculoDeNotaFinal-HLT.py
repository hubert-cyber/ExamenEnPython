#Problema 1
print("Problema 1")
''' 1.- Diseñe un algoritmo mediante pseudocódigo, diagrama de flujo y diagrama de N/S, para calcular la nota
 final del curso de Fundamentos de programación, considerando que el porcentaje de valor de la primera unidad es
 20%, de la segunda unidad vale 15%, y de la tercera unidad es un 15%, mientras que el trabajo final vale un 50%'''
#Datois de entrada
print("Problema 1")
promedio1raU=0
promedio2daU=0
promedio3raU=0
promedio4taU=0
nota1U=int(input("Digite su nota en la 1ra Unidad → "))
nota2U=int(input("Digite su nota en la 2da Unidad → "))
nota3U=int(input("Digite su nota en la 3ra Unidad → "))
nota4U=int(input("Digite su nota en la 4ta Unidad → "))
#Procedimiento
print()
if nota1U >=0 and nota1U <=20 :
    promedio1raU = nota1U * 0.20
    a=int(promedio1raU)
    print("Promedio 1ra Unidad:",a)
if nota2U >=0 and nota2U <=20 :
    promedio2daU = nota2U * 0.15
    b=int(promedio2daU)
    print("Promedio 2da Unidad:",b)
if nota3U >=0 and nota3U <=20 :
    promedio3raU = nota3U * 0.15
    c=int(promedio3raU)
    print("Promedio 3ra Unidad:",c)
if nota4U >=0 and nota4U <=20 :
    promedio4taU = nota4U * 0.50
    d=int(promedio4taU)
    print("Promedio 4ta Unidad:",d)
notFinal=a + b + c + d
#Datos de Salida
print("Nota final es:",notFinal)

#gracias
