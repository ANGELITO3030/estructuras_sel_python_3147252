'''
Estructura de control if:
se utiliza para tomar decisiones
basadas en expresiones condicionales

'''
#ejemplo 1 : if simple
edad = int( input('ingrese su edad: '))

documento=input('tienes documento? (si/no): ')
#condicional : si la edad es mayor o igual a 18
if edad >= 18 and documento=='si':
    #codigo para cuando es mayor a 18
    print('eres mayor de edad, puedes votar')
else:
    #codigo para cuando es menor a 18
    print('eres menor de edad o no tienes documento no puedes votar')
#codigo que se ejecuta siempre
print('fin del programa')
