"""
    Création du jeu "Nombre Mystère"

Le but du jeu "Nombre Mystère" est de faire deviner au joueur à nombre aléatoire choisi par le jeu en un minimum de coup.

Le principe de base est le suivant :
    - Le programme choisi un nombre au hasard (exemple : entre 0 et 100)
    - L'utilisateur Entre un nombre
    - Le programme vérifie la réponse et offre à l'utilisateur trois réponses possible : 
        - C'est plus !
        - C'est moins !
        - Bonne réponse ! Le bon nombre était X, vous avez trouvé la réponse en Y coups
    - Une fois la réponse trouvée, le programme demande à l'utilisateur s'il veux recommencer une partie

Saurez-vous relever le challenge ?
"""
import random
import os

fermerApplication = False

while(fermerApplication == False):
    #On vide la console
    os.system('cls')
    match input("Tapez '1' pour lancer une partie ou bien '2' pour arrêter le jeu : "):
        case "1":
            print("La partie va commencer")

            #Nombre de tentative
            nombreTentative = 0
            #Définition d'un nombre entier entre 0 et 100
            nombreADeviner = random.randint(0,100)

            partieTerminee = False

            while(partieTerminee == False):
                entreeUtilisateur = input("Veuillez entrer un nombre entre 0 et 100 : ")

                # Ici, je vérifie que l'entrée utilisateur est bien un nombre
                if (entreeUtilisateur.isdigit()):
                    nombreTentative = nombreTentative + 1

                    if (int(entreeUtilisateur) < nombreADeviner):
                        print("C'est plus !")
                    elif (int(entreeUtilisateur) > nombreADeviner):
                        print("C'est moins !")
                    else:
                        partieTerminee = True
                        print("Bravo ! Le bon nombre était {}, Vous avez trouvé le bon nombre en {} tentative(s)".format(nombreADeviner, nombreTentative))

                        input("Appuyer sur une touche pour continuer...")
                else:
                    print("Entrée non valide, veuillez entrer un nombre entre 0 et 100")

        case "2":
            print("Fermeture de l'application")

            fermerApplication = True
        case _:
            print("Veuillez choisir une option proposée")