url_webhook = "https://discord.com/api/webhooks/781926076112830534/DaLMt5qzYNHtXBr6D8SXtoNbUUBvbkpW0nJxXRJnBP-SPjLqUL4tnnRI-6KUTl7-bFQ7"
def ptint_discord(mensage)
webhook = discordwebhok(url=url_webhook, content=mensaje)
webhook.execute()
def calcula_el_precio_total(comida)
IVA =round((float(comida)*0.1),2)
propina = round((float(comida)0.1),2)
total = round ((float(comida) + (float(IVA) + (float(propina))),2)
print_discord("precio de la comida = " + str(float(comida)))
print_discord("IVA = " + str(float(IVA)))
print_discord("total = " + str(float(total)) + "€")
return calcula_el_precio_total
print_discord("1.pizza    6€")
print_discord("2.ensalada 4€")
print_discord("3.kebab    3€")
printd_discord("4.salmón  8€")
num_ordre = int (input("escriba el numero del menu: "))
if num_ordre == 1:
    calcula_el_precio_total(6)
elif num_ordre == 2:
    calcula_el_precio_total(4)
elif num_ordre == 3:
    calcula_el_precio_total(3)
elif num_ordre == 4:
    calcula_el_precio_total(8)
    else:
        print("este menu no existe ")