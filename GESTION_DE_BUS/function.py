
import copy
import random
import copy



passager_model = {
    "id" : "empty",
    "nom" : "empty",
    "bagage" : 0
}
bus_model= {
    "id" : 0,
    "place_max" : 0,
    "place_oqp" : 0,
    "kg" : 1000,
    "passager" : []
}
count_table = []

# création des passagers 
def user_create(check_id_user):
    array = []
    while True:
        name = input("Entrer le nom du passager: ")
        if len(name) >= 4:
            bagage = input("entrer le poids des bagages: ")
            if bagage.isdigit():
                if int(bagage) >= 0:
                    id = input("veuillez entrer une chaine de 4 caractères: ")
                    if len(id) == 4 and id not in check_id_user:
                        a = random.randint(1,1547)
                        a = a + int(bagage)
                        id = id + str(a)
                        check_id_user.append(id)
                        the_passager = copy.deepcopy(passager_model)
                        the_passager["id"] = id   
                        the_passager["nom"] = name  
                        the_passager["bagage"] = bagage 
                        array.append(the_passager)
                        array.append(check_id_user)
                        return array
                    else:
                        print("voud devez entrer exactement 4 caractères")
                else:
                    print("vous devez entrer un nombre positif")
            else:
                print("vous devez entrer des nombres")
        else:
            print("le nom est trop court ")




# Création d'un bus (fonction)
def bus_create(check_id_bus):
    array = []
    while True:
        place_max = input("veuillez entrer le nombre de place maximun pour ce bus: ")
        if place_max.isdigit():
            if int(place_max) > 0:
                id = input(" veuillez entrer une chaine de 5 caractères: ") 
                if len(id) == 5 :
                    if id not in check_id_bus:
                        b = random.randint(1547, 5689)  
                        id= id + str(b)
                        check_id_bus.append(id) 
                        current_bus_model = copy.deepcopy(bus_model)
                        current_bus_model["place_max"] = place_max    
                        current_bus_model["id"] = id
                        array.append(current_bus_model)
                        array.append(check_id_bus)                      
                        return array
                    else:
                        print("cette identifiant existe déja")
                else:
                    print("vous devez entrer exactement 5 caractères")
            else:
                print("le nombre de place doit être supérieur à 0")
        else:
            print("le nombre de place doit être un nombre")
       


# Fonction pour ajouter un passager à un bus
def add_user_in_bus(choix,count_table,the_user,name,all_bus):
    while True:
        if choix in count_table:
            choix = choix - 1
            place_oqp = all_bus[choix]["place_oqp"]
            Place_max = all_bus[choix]["place_max"]
            r =int(Place_max) - int(place_oqp)
            idb = all_bus[choix]["id"]
            the_bus= all_bus[choix]
            kg = int(the_user["bagage"])
            kgs = 0
            kgb = int(the_bus["kg"])
            for passager in the_bus["passager"]:
                kgs = kgs + int(passager["bagage"]) 
            m = kgb - (kgs + int(kg))
            n = kgb - kgs
            if r > 0 and m >= 0:
                place_oqp = int(place_oqp) + 1
                all_bus[choix]["place_oqp"] = place_oqp
                all_bus[choix]["passager"].append(the_user)
                print(f"{name} a bien été ajouté au bus {idb}")
                return all_bus
            elif r <= 0: 
                print(" il n'y a plus de place disponible ")
                return False
            elif m < 0:
                print(f"Le bus ne peut pas contenir les bagages de ce passager. car il n'a que {n}kg de libre")
                return False
            else:
                print("plus de place disponible")
                return False
        else:
                print("ce bus n'existe pas")
                return False
                



# Ajouter un utilisateur existant
def add_existing_user_in_bus(the_user,all_bus):
    continuer = True
    while continuer:
        count_table=read_all_bus(all_bus)
        choix = input("veuillez choisir le bus dans le quel vous souhaitez l'ajouter: ")
        if choix.isdigit():
            if int(choix) in count_table:
                choix = int(choix) - 1
                place_oqp = all_bus[choix]["place_oqp"]
                Place_max = all_bus[choix]["place_max"]
                r =int(Place_max) - int(place_oqp)
                idb = all_bus[choix]["id"]
                the_bus= all_bus[choix]
                id_user = the_user["id"]
                name = the_user["nom"]
                check=existing_passager_in_bus(id_user,the_bus)
                if check == True:
                    kg = int(the_user["bagage"])
                    kgb = the_bus["kg"]
                    kgs = 0
                    for passager in the_bus["passager"]:
                        kgs = kgs + int(passager["bagage"]) 
                    n = kgb - kgs
                    m = kgb - (kgs + int(kg))
                    if r > 0 and m >=0:
                        place_oqp = int(place_oqp) + 1
                        all_bus[choix]["place_oqp"] = place_oqp
                        all_bus[choix]["passager"].append(the_user)
                        print(f"{name} a bien été ajouté au bus {idb}")
                        return all_bus
                    elif r <= 0: 
                        print(" il n'y a plus de place disponible")
                        return False
                    elif m < 0:
                        print(f"Le bus ne peut pas contenir les bagages de ce passager. car il n'a que {n}kg de libre")
                        return False
                    else:
                        print("plus de place disponible")
                        return False
                elif check == False:
                    print(f"{name} est déjà présent dans le bus {idb}")
                    return False
                        
            else: print("Ce bus n'existe pas")
        else:
            print("entrer une option valide")
                
            

# Vérifier si les bus peuvent contenir des passagers venant d'autre bus
def add_passager_in_other_bus(matricule,all_bus,check_id_bus):
    tru=True
    while tru:
        if matricule in check_id_bus:
            for bus in all_bus:
                if bus['id'] == matricule:
                    x=bus["place_oqp"]
                    x = int(x)
                    for buses in all_bus:
                        y=buses["place_max"]
                        z=buses["place_oqp"]
                        xids = buses["id"]
                        r = int(y) - int(z)
                        if r > x:
                            print(f"le bus avec l'identifiant {xids} peut prendre les passagers transférer car il a encore {r} place libre")
                        else:
                            print(f"le bus avec l'identifiant {xids} ne peut prendre les paasagers car il n'a plus assez de place libre")
                    print("souhaitez-vous vérifier si vous pouvez transférer les passagers d'un autre bus?")
                    third_admin_choice= input(" oui = continuer -------- n'importe quel autre caractère pour revenir au menu: ")
                    if third_admin_choice.lower() == "oui":
                        print("")
                        continue
                    else:
                        tru=False
                        break
                else:
                        continue
        else: 
                print("ce matricule n'existe pas") 
                break
        



              
# afficher la liste des passagers d'un bus
def read_passager_in_bus(matricule,check_id_bus,all_bus):
    if matricule in check_id_bus:
        for bus in all_bus:
            if bus['id'] == matricule:
                if len (bus["passager"]) > 0:
                    for i in bus["passager"]:
                        passager_name= i["nom"]
                        passager_bage= i["bagage"]
                        print(f"{passager_name} poids des bagages: {passager_bage}") 
                elif len (bus["passager"]) == 0:   
                    print("ce bus n'a pas de passager pour pour le moment")    
            else:
                continue
    else:
        print(f"Il n'existe pas de bus portant le matricule {matricule}")
        print(f"voici les matricules des bus existant: {check_id_bus}")  



        
# fonction pour afficher tous bus
def read_all_bus(all_bus):
    if len(all_bus) <= 0:
        print("il n'y pas de bus disponible")
    elif len(all_bus) > 0:
        recount = 1
        rerecount = 0
        count_table.clear()
        for i in all_bus:
            count_table.append(recount)
            info_id=all_bus[rerecount]["id"]
            info_place_oqp=all_bus[rerecount]["place_oqp"]
            info_place_max=all_bus[rerecount]["place_max"]
            info_kg = all_bus[rerecount]["kg"]
            kgs = 0
            for passager in all_bus[rerecount]["passager"]:
                kgs = kgs + int(passager["bagage"]) 
            m = info_kg - int(kgs)
            place = int(info_place_max) - int(info_place_oqp)
            print(f"{recount}: identifiant {info_id} && place disponible {place} && peut encore supporter {m}kg")
            recount = recount + 1
            rerecount= rerecount + 1
        return count_table




# afficher tous passagers
def read_and_add_passager(all_passager):
    while True:
        print("")
        print("voici la liste des passagers présent dans votre flotte")
        count = 1
        for passager in all_passager:
            name = passager["nom"]
            id = passager["id"]
            print(f"{count}: {name} identifiant: {id}")
            count = count + 1
        a=input("saisisissez le numéro du passager que vous souhaitez mettre dans un bus: ")
        if a.isdigit(): 
            if int(a) > 0 and int(a) <= len(all_passager):
                a = int(a) - 1
                the_passager = all_passager[a]
                return the_passager
            else: 
                print("veuiller choisir une option correcte")
        else:
            print("choix incorrecte")

# fonction pour vérifier qu'un passager existe dans un bus
def existing_passager_in_bus(id_user,the_bus):
    list_passager = the_bus["passager"]
    if len (list_passager) == 0:
        return True
    if len (list_passager) > 0:
        i = 0
        for passager in list_passager:
            if id_user == passager["id"]:
                return False  
            else:
                i = i + 1
                continue
        return True
    else:
        print("une erreur est survenue")


# fonction pour supprimer un bus
def delete_bus(matricule,check_id_bus,all_bus):
    array = []
    print(matricule)
    if matricule in check_id_bus:
        for bus in all_bus:
            if bus['id'] == matricule:
                while True:
                    okay=input("Etes vous sur de vouloir retirer ce bus de la liste de vos bus? O/N: ")
                    if okay.upper() == "O":
                        print(f"le bus avec le matricule {matricule} a bien été rétiré")
                        all_bus.remove(bus)
                        check_id_bus.remove(matricule)
                        array.append(all_bus)
                        array.append(check_id_bus)
                        return array
                    elif okay.upper() == "N":
                        break
                    else:
                        continue
                
            else:
                continue
        print("Il n'existe pas de bus portant ce matricule")
        print(f"voici les matricules des bus existant: {check_id_bus}") 
        return False
    else:
        print(f"voici les matricules des bus existant: {check_id_bus}") 
        return False
        

# fonction pour supprimer un passager dans un bus
def remove_one_user_in_bus(id_user,choix,all_bus,check_id_user):
    array = []
    if id_user in check_id_user:
        the_bus = all_bus[choix]
        i = 0   
        for passager in the_bus["passager"]:
            if id_user == passager["id"]:
                print(f"le passager avec le matricule {id_user} a bien été rétiré de ce bus ")
                all_bus[choix]["passager"].remove(passager)
                all_bus[choix]["place_oqp"] = int(all_bus[choix]["place_oqp"]) - 1
                array.append(all_bus)
                array.append(check_id_user)
                return array
            else: 
                continue
        print("le passager n'exixte pas")
        return False   
    else:
        print(f"le passager avec l'identifiant {id_user} n'existe pas dans ce bus ")
        return False

# afficher tous les passagers d'un bus          
def read_all_passager(all_passager):
    print("voici la liste des passagers de votre flotte de bus")
    count = 1
    for item in all_passager:
        name=item["nom"]
        id = item["id"]
        bagage = item["bagage"]
        print(f"{count}: {name} identifiant: {id} poids des bagages: {bagage} ")
        count = count + 1 
  

# fonction pour determiner l'existence d'un passager dans un bus          
def user_existing(all_bus,check_id_user,id_user):
    if id_user in check_id_user:
        print(f"le passager avec l'dentifiant {id_user} fait parti de votre flotte")
        for bus in all_bus:
            for passager in bus["passager"]:
                if id_user == passager["id"]:
                    idb = bus["id"]
                    oqp = bus["place_oqp"]
                    max = bus["place_max"]
                    name = passager["nom"]
                    print(f" le passager {name} identifiant: {id_user} se trouve dans le bus {idb}: place_max: {max} et place_oqp: {oqp}")
                else:
                    continue
    else:
        print("cet identifiant ne correspond à aucun passager")   


# Supprimer un passager dans ma flotte                   
def remove_passager_in_flotte(all_bus,check_id_user,id_user):
    array = []
    if id_user in check_id_user:
        i = 0
        for bus in all_bus:
            for passager in bus["passager"]:
                if id_user == passager["id"]:
                    idb = bus["id"]
                    print(f"le passager avec le matricule {id_user} a bien été rétiré du bus: {idb} ")
                    all_bus[i]["passager"].remove(passager)
                    all_bus[i]["place_oqp"] = int(all_bus[i]["place_oqp"]) - 1
                    array.append(all_bus)
                    array.append(check_id_user)
                else:
                    continue   
            i = i + 1
        check_id_user.remove(id_user)
        print(f" le passager {id_user} a été retiré de flotte de bus")
        return array   
    else:
        print(f" Il n'existe pas de passager avec l' identifiant {id_user}")
        return False


# supprimer un passager dans la liste des passagers    
def remove_in_passager(id_user,all_passager):
    
    for i in all_passager:
        if id_user == i["id"]:
            all_passager.remove(i)
            return all_passager
        else:
            continue


def poids_du_bus(all_bus,check_id_bus):
  
    t = True
    while t:
        kg = 0
        id_bus= input("Entrer l'id du bus: ")
        if id_bus in check_id_bus:
            for bus in all_bus:
                if id_bus == bus["id"]:
                    kgb = int(bus["kg"])
                    for passager in bus["passager"]:
                        kg = kg + int(passager["bagage"]) 
                    break
                else: 
                    continue
          
            print(f"Le nombre de kg reservé pour ce bus est de {kgb}. le poids occupé par les bagages est de: {kg}")
        else: 
            print(" identifiant invalid")
        while True:
            choix = input(" Souhaitez vous vérifier le poids  d'un autre bus O/N: ")
            if choix.upper() == "O":
                break
            elif choix.upper() == "N":
                t = False
                break
            else:
                continue
            
                    
                
    
    