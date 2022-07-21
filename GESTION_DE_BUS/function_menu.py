def bienvenue():
    print("")
    print("_"*75)
    print("BIENVENUE DANS NOTRE PROGRAMME DE GESTION DE BUS")
    print("Nous vous remercions d' utiliser notre programme...")
    print("_"*75)
    
def menu():
    print("")   
    print("1: Ajouter un passager")
    print("2: créer un bus")
    print("3: Pour ajouter un passager dans un bus")
    print("4: monitoring des bus ")
    print("5: monitoring des passagers")
    print("q: pour quitter")
    first_admin_choice = input("veuiller choisir votre option: ")
    return first_admin_choice

def monitoring_for_bus():
    print("_"*20)
    print("")
    print("1: consulter la liste des bus disponible")
    print("2: afficher la liste des passagers d'un bus")
    print("3: vérifier si un bus peut acceuillir les passagers d'un autre bus")
    print("4: Contrôler le nombre de kg reservé pour un bus")
    print("5: retirer un bus de ma flotte de bus")
    print("6: retirer un passager dans un bus")
    print("r: retour")

def monitoring_for_passager():
    print("_"*20)
    print("")
    print("1: afficher la liste des passagers de ma flotte")
    print("2: vérifier si un passager est présent dans ma flotte de bus")
    print("3: retirer un passager de ma flotte")
    print("r: retour")