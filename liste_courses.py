import sys
import json
import os

#récupérer le chemin où sauvegarder la liste de courses
CUR_DIR = os.path.dirname(__file__)
CHEMIN = os.path.join(CUR_DIR, "liste_courses.json")
#vérifier si une liste de courses existe déjà, sinon en créer une
if os.path.exists(CHEMIN) == False :
    LISTE_COURSES = []
else :
    with open(CHEMIN, "r", encoding="utf-8") as f :
        LISTE_COURSES = json.load(f)

while True: #boucle infinie pour que le programme ne se termine que lorsqu'on le demande

#demander à l'utilisateur son choix en affichant les options disponibles
    choix = input("""Choisissez parmi les 5 options suivantes \U0001F447 :
1. Ajouter un élément à la liste de courses
2. Retirer un élément de la liste de courses
3. Afficher les éléments de la liste de courses
4. Vider la liste de courses
5. Quitter le programme
\U0001F449 Votre choix ? : """)

#vérification que le choix donné par l'utilisateur est correct
    if not (choix.isdigit() and 1 <= int(choix) <= 5) : #vérifie que le choix est un nombre compris entre 1 et 5 inclus
        print("Veuillez entrer un choix valide...") #tant que le choix n'est pas valide redemander à l'utilisateur
        continue

#1. Ajouter un élément à la liste de courses
    if choix == "1" :
        element = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE_COURSES.append(element)
        print(f"L'élément {element} a bien été ajouté à la liste de courses \U0001F609.")

#2. Retirer un élément de la liste de courses
    elif choix == "2" :
        #demander à l'utilisateur quel élément de la liste retirer
        retrait_element = input("Entrez l'élément à retirer de la liste de courses : ")
#vérifier que l'élément est présent dans la liste de courses sans tenir compte de la casse
        element_lower = retrait_element.lower()
        recherche_liste = " ".join(LISTE_COURSES)
        recherche_liste = recherche_liste.lower()
        recherche_liste = recherche_liste.split(" ")
        #vérifier si l'élément est présent dans la liste et le signaler à l'utilisateur si ce n'est pas le cas
        if element_lower not in recherche_liste :
            print(f"L'élément {retrait_element} n'est pas dans la liste \U0001F641.")
        #sinon retirer l'élément de la liste de courses
        else :
            retrait_element_index = recherche_liste.index(element_lower) #récupérer l'index de l'élément à retirer dans la liste de courses
            retrait_element = LISTE_COURSES[retrait_element_index] #récupérer la casse d'origine de l'élément à supprimer
            LISTE_COURSES.remove(LISTE_COURSES[retrait_element_index]) #retirer l'élément à l'aide de son emplacement afin de s'affranchir de la casse
            print(f"L'élément {retrait_element} a bien été supprimé de la liste de courses \U0001F609.")

#3. Afficher les éléments de la liste de courses
    elif choix == "3" :
        #Si la liste de courses n'est pas vide l'afficher
        if LISTE_COURSES :
            for i, element in enumerate(LISTE_COURSES, 1):
                print(f"{i}. {element}")
        #sinon indiquer que la liste est vide
        else : print("Votre liste ne contient aucun élément \U0001F615.")

#4. Vider la liste de courses
    elif choix == "4" :
        LISTE_COURSES.clear()
        print("La liste de courses a été vidée de son contenu \U0001F609.")

#5. Quitter le programme
    elif choix == "5" :
        print("À bientôt \U0001F44B !")
        # mettre à jour le fichier JSON avec la nouvelle liste de courses
        with open(CHEMIN, "w", encoding="utf-8") as f :
            json.dump(LISTE_COURSES, f, indent=4, ensure_ascii=False)
        sys.exit()
    print("-" * 50)