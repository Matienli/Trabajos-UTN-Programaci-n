print ("Ejercicio 1: ")
nombre_de_usuario= input("Escriba su nombre: ")
print ("Hola " + nombre_de_usuario)

print ("Ejercicio 2:")
num_uno= int(input("Ingrese un numero porfavor: "))
num_dos= int (input("Ingrese otro numero porfavor: "))
print(str(num_uno) +' + '+str(num_dos) +' Da igual a '+str(num_uno+num_dos))

print ("Ejercicio 3: ")
nombre= (input ("Ingrese su nombre: "))
apellido= (input ("Ingrese su apellido: "))
edad= (input ("Ingrese su edad: "))
print ("Su nombre es:", nombre)
print ("Su apellido es:", apellido)
print ("Su edad es:", edad)

print("Ejercicio 4: ")
nombre_usuario= (input ("Escriba su nombre: "))
numero_comision= (input ("Escriba el numero de su comisión: "))
asignatura= (input("Escriba su asignatura: "))
docente= (input("Escriba el nombre de su docente: "))
presencia= (input("Escriba si estuvo presente si/no: "))
print ('Su nombre es '+nombre_usuario+ ' de la comisión '+numero_comision+ ' y la asignatura '+asignatura+'. Su docente se llama '+docente+' y '+presencia+ ' estuvo en la clase')

print("Ejercicio 5: ")
lado_cuadrado= int(input("Escriba el lado de un cuadrado: "))
print("La superficie de este cuadrado es: "+str(lado_cuadrado*lado_cuadrado))

print("Ejercicio 6: ")
lado_rectangulo= int(input("Escriba un lado del rectangulo: "))
lado_rectangulo_1= int(input ("Escriba el otro lado del rectangulo: "))
print("La superficie de este rectangulo es: "+str(lado_rectangulo*lado_rectangulo_1))

print("Ejercio 7: ")
base_triangulo= int(input("Escriba la base del triangulo: "))
alutra_triangulo= int(input("Escriba la altura del triangulo: "))
print("La superficie del triangulo es: "+str((base_triangulo*alutra_triangulo)/2))

print("Ejercicio 8: ")
producto= (input ("Escriba un producto: "))
precio= int(input("Escriba el precio del producto: "))
iva= precio*0.21
print (("El iva de su producto es: "+str (iva)))

print("Ejercicio 9: ")
nombre_alumno= (input("Escriba su nombre y apellido: "))
nota_1= int(input("Escriba su nota de programación: "))
nota_2= int(input("Escriba su nota de matematicas: "))
nota_3= int (input("Escriba su nota de lectura comprensiva:"))
promedio_1= str((nota_1 + nota_2 + nota_3) /3)
print("Tu promedio es de: "+promedio_1)

print("Ejercicio 10: ")
nombre_usuario_1= input("Ingrese su nombre porfavor: ")
edad_1= int(input("Ingrese su edad porfavor: "))
print (nombre_usuario_1+", dentro de 10 años tendras: "+str(edad_1+10) + " años")


