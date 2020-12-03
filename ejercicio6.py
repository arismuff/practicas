def calcula_el_precio_total_de_la_comida(comida):
    IVA = round((float(comida)*0.1),2)
    propina = round((float(comida)*0.1),2)
    total = round((float(comida) + float(IVA) + float(propina)),2)
   print("el precio de la comida es de" +str(float(comida)))
print("el IVA es de " +str(float(IVA)))
print("la propina es de " + str(float(propina)))
print("el precio total es de " + str(float(total)))
print("seleccione el menu ")
print("1. Pizza	6€")
print("2. Ensalada 4€")
print("3. Kebab	3€")
print("4. Salmón 8€")
num_orden = int (input("escriba el nuemro del menu "))
if num_orden == 1:
    calcula_el_precio_total_de_la_comida(6)
    elif num_orden == 2:
        calcula_el_precio_total_de_la_comida(4)
    elif num_orden == 3:
        calcula_el_precio_total_de_la_comida(3)
    elif num_orden == 4:
        calcula_el_precio_total_de_la_comida(6)
    else:
        print("el menu seleccionado no se encuentra disponible en estos momentos ")
