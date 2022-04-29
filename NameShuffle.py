prenom = input("Qu’elle est le prenom? ") + " "
nom = input("Qu’elle est le nom? ") + " "
nom_famille = input("Qu’elle est le nom de famille? ") + " "

prenom_initial = prenom[0] + " "
nom_initial = nom[0] + " "
nom_famille_initial = nom_famille[0] + " "

prenom_initial_period = prenom_initial + " "
nom_initial_period = nom_initial + " "
nom_famille_initial_period = nom_famille_initial + " "

nom_liste = [
prenom + nom + nom_famille,
prenom + nom + nom_famille_initial,
prenom + nom_initial + nom_famille,
prenom + nom_initial + nom_famille_initial,
prenom + nom_famille + nom,
prenom + nom_famille + nom_initial,
prenom + nom_famille_initial + nom,
prenom + nom_famille_initial + nom_initial,
nom_famille + prenom + nom,
nom_famille + prenom + nom_initial,
nom_famille + prenom_initial + nom,
nom_famille + prenom_initial + nom_initial,
nom_famille + nom + prenom,
nom_famille + nom + prenom_initial,
nom_famille + nom_initial + prenom,
nom_famille + nom_initial + prenom_initial,
nom + prenom + nom_famille,
nom + prenom + nom_famille_initial,
nom + prenom_initial + nom_famille,
nom + prenom_initial + nom_famille_initial,
nom + nom_famille + prenom,
nom + nom_famille + prenom_initial,
nom + nom_famille_initial + prenom,
nom + nom_famille_initial + prenom,
prenom_initial + nom + nom_famille,
prenom_initial + nom + nom_famille_initial,
prenom_initial + nom_initial + nom_famille,
prenom_initial + nom_initial + nom_famille_initial,
prenom_initial + nom_famille + nom,
prenom_initial + nom_famille + nom_initial,
prenom_initial + nom_famille_initial + nom,
prenom_initial + nom_famille_initial + nom_initial,
nom_initial + prenom + nom_famille,
nom_initial + prenom + nom_famille_initial,
nom_initial + prenom_initial + nom_famille,
nom_initial + prenom_initial + nom_famille_initial,
nom_initial + nom_famille + prenom,
nom_initial + nom_famille + prenom_initial,
nom_initial + nom_famille_initial + prenom,
nom_initial + nom_famille_initial + prenom_initial,
nom_famille_initial + prenom + nom,
nom_famille_initial + prenom + nom_initial,
nom_famille_initial + prenom_initial + nom,
nom_famille_initial + prenom_initial + nom_initial,
nom_famille_initial + nom + prenom,
nom_famille_initial + nom + prenom_initial,
nom_famille_initial + nom_initial + prenom,
nom_famille_initial + nom_initial + prenom_initial,
]

print(*nom_liste, sep="\n")
with open("nomvariation.csv", 'w') as output:
    for row in nom_liste:
        output.write(str(row) + '\n')
with open("nomvariation.txt", 'w') as output:
    for row in nom_liste:
        output.write(str(row) + '\n')
