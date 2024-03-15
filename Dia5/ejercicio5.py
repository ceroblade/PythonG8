edad = 27
#Juan es mayor de edad?
print(edad >=18)#True
print(edad <18)#False

graduacion_edad_colegio = 17
#Juan se graduo antes de los 18
print(graduacion_edad_colegio < 18)#True
print(graduacion_edad_colegio >= 18)#False

experiencia_laboral = 4
#Juan no tiene 4 Años de Experiencia Laboral
print(experiencia_laboral != 4)#False Excluye la cantidad de años
print(experiencia_laboral == 4)#True incluyen los años

numero_hijos = 0
#Juan tiene Hijos?
print(numero_hijos > 0)#False
print(numero_hijos == 0)#True
print(numero_hijos < 1)#True
print(numero_hijos != 0)#False
print(numero_hijos >= 1)#False

"""
Si las exportaciones disminuyen entonces bajarán las utilidades
Los precios son altos si y sólo sí los costos aumentan
Si la producción aumenta entonces bajarán los precios
Si la contaminación aumenta entonces existirá restricción vehicular adicional
Ser o no Ser
La Programacion no es facil
"""

nombre = "Juan"
me_llamo_juan = (nombre == "Juan")
print(me_llamo_juan)      #True
print(type(me_llamo_juan))#<class 'bool'>

#Logica proposicional
""" 
#Quieres helado (P) SI - NO
#Quieres bebida (Q) SI - NO

# AND (Y; i) 2 ^ 3
# Quieres helado y Quieres bebida
#Punto critico para el AND es : ambos verdaderos el resultado es verdadero
P y Q
-------
V y V = V *
V y F = F
F y V = F
F y F = F 

#Punto critico para el O es: ambos falsos el resultado es falso
P o Q
-------
V o V = V
V o F = V
F o V = V
F o F = F *

#XoR
#Punto critico para el XoR es: ambas iguales el resultado es False
P ^ Q

-F = V
-V = F

"""