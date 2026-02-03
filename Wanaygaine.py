import time
import os
from Stock import PRODUCT_CATALOG

def showProducts():
    print("Voici la liste des produits disponibles :")
    for product_name, details in PRODUCT_CATALOG.items():
        print(f"{details['num']}. {product_name} - Prix: {details['prix']} euros - Stock: {details['stock']} unités")

def KeenV():
    showProducts()
    sInput = input("Bonjour, veuillez choisir un numéro de produit: ")

    for product_name, details in PRODUCT_CATALOG.items():
        if str(details["num"]) == sInput:
            if details["stock"] > 0:
                print(f"Vous avez choisi {product_name} au prix de {details['prix']} euros.")

                details["stock"] -= 1
                print(f"Il reste {details['stock']} unités de {product_name} en stock")

                return
            else:
                print("Désolé, ce produit est en rupture de stock.")
                return
            
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    KeenV()

    time.sleep(3)