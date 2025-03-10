'''
 operadores logicos
 
gi con valores booleanos (V,F)
 acorde con las tablas de verdad
 '''
 # 
y = not True
print('el resultado de operar con not es',y)
#ejemplo 2
y = False and True
print('el resultado de operar con and es',y)
#ejemplo 3
y = False or False
print('el resultado de operar con and es',y)

'''
jerarquia de predencia de operadores 
(logicos inclusive)
1     ()
2     **
3     *,/,%,
4     +,-
5     >,<,>=,<=, !=,==
6     not
7     and
8      or
9      =
'''
#ejemplo 4 jerarquia de operadores
y = False and not true or False 
print("el resultado de operar con jerarquia de operadores es", y)