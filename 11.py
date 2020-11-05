preuproducte = int(input("Pon el precio del Producto:\n"))
IVA = int(input("Pon el IVA:\n"))
print("El IVA es:\n" , preuproducte * IVA / 100)
print("El Total es:\n" , preuproducte * (IVA / 100 + 1))