import random
import string

def generer_nom():
    noms = ["Dupont", "Martin", "Lefebvre", "Dubois", "Robert", "Richard", "Thomas", "Durand"]
    return random.choice(noms)

def generer_prenom():
    prenoms = ["Jean", "Marie", "Pierre", "Luc", "Sophie", "Emma", "Léa", "Julie"]
    return random.choice(prenoms)

def generer_mot_de_passe():
    longueur = random.randint(8, 12)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def generer_adresse():
    numeros = ["10", "23", "56", "78", "42", "99", "5", "17"]
    rues = ["rue de la Paix", "avenue des Champs-Élysées", "boulevard Saint-Germain", "place de la Concorde"]
    villes = ["Paris", "Marseille", "Lyon", "Toulouse", "Bordeaux", "Nice"]
    adresse = random.choice(numeros) + " " + random.choice(rues) + ", " + random.choice(villes)
    return adresse

def generer_sexe():
    sexes = ["Masculin", "Féminin"]
    return random.choice(sexes)

def generer_age():
    age = random.randint(18, 80)
    return age

def generer_personne():
    nom = generer_nom()
    prenom = generer_prenom()
    mot_de_passe = generer_mot_de_passe()
    adresse = generer_adresse()
    sexe = generer_sexe()
    age = generer_age()
    
    personne = {
        "Nom": nom,
        "Prénom": prenom,
        "Mot de passe": mot_de_passe,
        "Adresse": adresse,
        "Sexe": sexe,
        "Âge": age
    }
    
    return personne

# Génération d'une personne aléatoire
personne_aleatoire = generer_personne()

# Affichage des caractéristiques de la personne
for cle, valeur in personne_aleatoire.items():
    print(cle + ": " + str(valeur))
