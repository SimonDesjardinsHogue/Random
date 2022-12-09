# Importer la bibliothèque turtle
import turtle

# Créer un objet turtle
my_turtle = turtle.Turtle()

# Définir la taille et la couleur du crayon
my_turtle.pensize(5)
my_turtle.pencolor("red")

# Dessiner un carré en utilisant la tortue
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Afficher la fenêtre graphique
turtle.mainloop()
