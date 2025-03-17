
'''
if cascada :
estructura de control que permite 
evaluar varias condiciones en
cascada , es decir , si la primera
condicion no se cumple , 
se evalua la siguiente 
y asi sucesivamente
'''
#ejemplo 1
#modificar el programa de votaciones
#para que considere las de dad de 17 años
edad = int( input('ingrese su edad: '))
if edad > 18:
    print('puedes votar')
    
elif edad == 18:
    print('puedes votar con tu contraseña')
    
elif edad == 17:
    print('puedes el proximo año')
    
elif edad < 10:
    print('no puedes votar porque tienes TI')
    
elif edad < 17:
    print('no puedes votar aun')
        


    
print('fin del programa')