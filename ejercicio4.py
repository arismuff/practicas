botella1 = input ("Cuantas botellas de un litro o menos ")
botella2 = input ("Cuantas botellas de mas de un litro ")

cantidad1 = int (botella1)
cantidad2 = int (botella2)

botella01 = 0.1*cantidad1
botella02 = 0.25*cantidad2

print ("El total a devolver de las botellas de un litro o menos es  " +str(botella01)+ "euros")
print ("El total a devolver de las botellas de mas de un litro es  " +str(botella02)+ "euros")
