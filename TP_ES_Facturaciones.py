print("A")
precio_uno= int(input("Ingrese el precio del primer producto: "))
precio_dos= int(input("Ingrese el precio del segundo producto: "))
precio_tres= int(input("Ingrese el precio del tercer producto: "))
precio_final= int(precio_uno + precio_dos + precio_tres)
print ("La suma de los 3 productos da un total de: ", precio_final)

print()
print("B")
precio_uno_uno= int(input("Ingrese el precio del primer producto: "))
precio_dos_dos= int(input("Ingrese el precio del segundo producto: "))
precio_tres_tres= int(input("Ingrese el precio del tercer producto: "))
precio_final_dos= int((precio_uno_uno + precio_dos_dos + precio_tres_tres) /3)
print ("El promedio de los 3 productos da un total de: ", precio_final_dos)

print()
print("C")
precio_uno_c= int(input("Ingrese el precio del primer producto: "))
precio_dos_c= int(input("Ingrese el precio del segundo producto: "))
precio_tres_c= int(input("Ingrese el precio del tercer producto: "))
precio_subtotal= int (precio_uno_c + precio_dos_c + precio_tres_c)
iva= (precio_subtotal *0.21) 
precio_final_c= (precio_subtotal + iva)
print ("El precio final de los 3 productos más el IVA agregado da el total de: ", precio_final_c)
