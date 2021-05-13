#Vacunacion contra el covid-19
#Datos de entrada
sexo='femenino'
sexo= 'masculino'
edad=int(input("Ingrese su edad → "))
sexo=(input("Ingrese su sexo → "))
#proceso
print()
if edad >= 70 :
    vacunaS="Tipo C"
    if sexo== 'masculino' :
        print(vacunaS)
        vacunaS="Tipo C"
    if sexo== 'femenino':
        print(vacunaS)
        vacunaS="Tipo C"

if edad >=16 and edad <=69:
    if sexo == 'masculino':
        vacunaB = "Tipo B"
        print(vacunaB)
    if sexo == 'femenino':
        vacunaA = "Tipo A"
        print(vacunaA)
if edad <16 :
    vacunA= "Tipo A"
    print(vacunA)










