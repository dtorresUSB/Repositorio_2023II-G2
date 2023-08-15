print('Seleccione una opcion: \n',\
    '1. Calcula el area de un Circulo\n',\
        '2. Calcula el area de un rectangulo\n',\
            '3. Calcula el area de un triangulo')


fig=input('Ingrese el nombre de la figura: ')
A='NAN'

if (fig.lower()=='circulo'):
    r=int(input('Ingrese el valor del radio: '))
    A=3.1416*r**2
elif(fig.lower()=='rectangulo'):
    b=int(input('Ingrese el valor de la base: '))
    h=int(input('Ingrese el valor de la altura: '))
    A=b*h
elif(fig.lower()=='triangulo'):
    b=int(input('Ingrese el valor de la base: '))
    h=int(input('Ingrese el valor de la altura: '))
    A=b*h/2
else:
    print('\nIngreso una opción invalida')
print('El valor del area es',A)