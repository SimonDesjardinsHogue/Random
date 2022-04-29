#!/usr/bin/env python3
# Utilisez ces commandes dans Kali pour installer le logiciel requis :
# sudo apt install python3-pip
# pip install python-nmap

# Importer nmap afin que nous puissions l'utiliser pour l'analyse
import nmap
# Nous devons créer des expressions régulières pour nous assurer que l'entrée est correctement formatée.
import re

# Modèle d'expression régulière pour reconnaître les adresses IPv4.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# Modèle d'expression régulière pour extraire le nombre de ports que vous souhaitez analyser.
# Vous devez spécifier <lowest_port_number>-<highest_port_number> (ex 10-100)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Initialising the port numbers, will be using the variables later on.
port_min = 0
port_max = 65535

# Ce scanner de port utilise le module Python nmap.
# Vous devrez installer les éléments suivants pour le faire fonctionner sous Linux :
# Étape 1 : sudo apt install python3-pip
# Étape 2 : pip install python-nmap


# En-tête de l'interface utilisateur de base

open_ports = []
# Ask user to input the ip address they want to scan.
while True:
    ip_add_entered = input("\n Ip à scanner: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} est une adresse IP valide")
        break

while True:
    # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning 
    # all the ports is not advised.
    print("Veuillez saisir la plage de ports que vous souhaitez analyser au format : <int>-<int> (ex entre: 60-120)")
    port_range = input("Entrer port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()
# Nous effectuons une boucle sur tous les ports de la plage spécifiée.
for port in range(port_min, port_max + 1):
    try:
        # Le résultat est assez intéressant à regarder. Vous voudrez peut-être inspecter le dictionnaire qu'il renvoie.
        # Il contient ce qui a été envoyé à la ligne de commande en plus de l'état du port que nous recherchons. 
        # Pour nmap pour le port 80 et l'ip 10.0.0.2, vous exécuteriez : nmap -oX - -p 89 -sV 10.0.0.2
        result = nm.scan(ip_add_entered, str(port))
        # print(result)
        # Nous extrayons le statut du port de l'objet retourné
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        #Nous ne pouvons pas analyser certains ports et cela garantit que le programme ne plante pas lorsque nous essayons de les analyser.
        print(f"Ne peut pas scanner le port {port}.")
        
