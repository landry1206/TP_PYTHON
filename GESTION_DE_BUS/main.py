
import function_initial_state
import function_menu
import function

# initialisation des variables globales
#variable de vérification
name_content = []
check_id_user = []
check_id_bus = []
# variable de recupération des bus et passager initiaux
array_bus = []
array_passager = []
all_bus = []
all_passager = []
# variable pour boucler sur le menu
true = True

# création de bus initiaux
array_bus = function_initial_state.create_bus()
all_bus = function_initial_state.add_user_in_bus()
check_id_bus = function_initial_state.check_id_buses(check_id_bus)


#création de passager initiaux
all_passager=function_initial_state.add_user(all_passager)

    

check_id_user= function_initial_state.check_id_users(check_id_user) 
 
print("Les données initiales ont bien été enregistré avec succès")


# Debut du programme
function_menu.bienvenue()
while true:
    print("_"*50)
    first_admin_choice = function_menu.menu()

    if first_admin_choice == "1":
        while True:
            print("bien vouloir...")
            user = function.user_create(check_id_user)
            all_passager.append(user[0])
            check_id_user.append(user[1])
            one_user = all_passager[-1]["nom"]
            print(f"{one_user} a bien été créé ")
            print("")
            user_choix= input("souhaiter vous créer un autre bus? oui= continuer ------- un autre caractère pour revenir: ")
            if user_choix.upper() == "OUI":
                    continue
            else:
                break
    elif first_admin_choice == "2":
        while True:
            print("bien vouloir...")
            one_bus = function.bus_create(check_id_bus)
            all_bus.append(one_bus[0])
            check_id_bus.append(one_bus[1])
            id_bus = all_bus[-1]["id"]
            print(f"le bus avec l'identifiant {id_bus} a été créé avec succès")
            print("")
            user_choix= input("souhaiter vous créer un autre bus? oui= continuer ------- un autre caractère pour revenir: ")
            if user_choix.upper() == "OUI":
                continue
            else:
                break 
    elif first_admin_choice == "3":
        while True:
            print("_"*20)
            print("")
            print("1: Ajouter un passager existant ")
            print("2: créer un passager et l'ajouter à un bus")
            print("r: pour revenir en arriere")
            user_choix = input("Bien vouloir choisir une option: ")
            if user_choix =="1":
                while True:
                    the_user=function.read_and_add_passager(all_passager)
                    the_bus=function.add_existing_user_in_bus(the_user,all_bus)
                    if the_bus== False:
                        print("souhaitez-vous ajouter un autre utilisateur dans un bus")
                        continuer = input("oui=continuer ------ n'importe quel autre caractère pour sortir: ")
                        if continuer.lower() == "oui":
                            continue
                        else:
                            break
                    else:
                        all_bus = the_bus
                        print("souhaitez-vous ajouter un autre utilisateur dans un bus")
                        continuer = input("oui=continuer ------ n'importe quel autre caractère pour sortir: ")
                        if continuer.lower() == "oui":
                            continue
                        else:
                            break
            elif user_choix =="2":
                while True:
                    user = function.user_create(check_id_user)
                    all_passager.append(user[0])
                    check_id_user.append(user[1])
                    name = user[0]["nom"]
                    the_user= user[0]
                    print("voici la liste des bus")
                    count_table=function.read_all_bus(all_bus)
                    choix= input("veuiller choisir votre bus: ")
                    if choix.isdigit():
                        choix=int(choix)
                        if choix in count_table:
                            the_bus=function.add_user_in_bus(choix,count_table,the_user,name,all_bus)
                            if the_bus == False:
                                print("souhaitez-vous ajouter un autre utilisateur dans un bus")
                                continuer = input("oui=continuer ------ n'importe quel autre caractère pour sortir: ")
                                if continuer.lower() == "oui":
                                    continue
                                else:
                                    break
                            else:
                                all_bus= the_bus
                                print("souhaitez-vous ajouter un autre utilisateur dans un bus")
                                continuer = input("oui=continuer ------ n'importe quel autre caractère pour sortir: ")
                                if continuer.lower() == "oui":
                                    continue
                                else:
                                    break
                        else:
                            print("veuillez entrer une option valide") 
                    else: 
                        print("veuillez entrer une option valide")
            elif user_choix == "r":
                break
    elif first_admin_choice == "4":
        while True:
            function_menu.monitoring_for_bus()
            secund_admin_choice = input("veuillez saisir votre choix: ")
            if secund_admin_choice == "1":
                function.read_all_bus(all_bus)
                print("")
            elif secund_admin_choice == "2":
                matricule= input(("veuillez entrer l'identifiant du bus dont vous souhaiter extraire la liste des passagers: "))
                function.read_passager_in_bus(matricule,check_id_bus,all_bus)
            elif secund_admin_choice =="3":
                matricule= input(("entrer l'identifiant du bus dont vous souhaiter transferer les passagers: "))
                function.add_passager_in_other_bus(matricule,all_bus,check_id_bus)
            elif secund_admin_choice == "4":
                function.poids_du_bus(all_bus,check_id_bus)
            elif secund_admin_choice =="5":
                matricule= input(("veuillez entrer l'identifiant du bus que vous souhaitez retirer de votre flotte de bus: "))
                buse=function.delete_bus(matricule,check_id_bus,all_bus)
                while True:
                    if buse == False:
                        break
                    else:
                        all_bus = buse[0]
                        check_id_bus = buse[1]
                        break
            if secund_admin_choice == "6":
                count_table=function.read_all_bus(all_bus)
                choix= input("veuiller choisir votre bus: ")
                if choix.isdigit():
                    choix=int(choix)
                    if choix in count_table:
                        choix = int(choix) - 1
                        while True:
                            id_user=input("veuillez entrer l'identifiant du passager que vous souhaitez retirer de ce bus: ")
                            the_bus=function.remove_one_user_in_bus(id_user,choix,all_bus,check_id_user)
                            if the_bus == False:
                                break
                            else:
                                all_bus= the_bus[0]
                                check_id_user = the_bus[1]
                                break
            elif secund_admin_choice == "r":
                break                
    elif first_admin_choice == "5":
        while True:
            function_menu.monitoring_for_passager()
            fourth_admin_choice = input("Entrer votre choix: ")
            if fourth_admin_choice == "1":
                function.read_all_passager(all_passager)
            elif fourth_admin_choice == "2":
                b = True
                while b:
                    id_user=input("veuillez entrer l'identifiant du passager dont vous souhaitez vérifier l'existence: ")
                    function.user_existing(all_bus,check_id_user,id_user)
                    while True:
                        choix = input("Vérifier l'existence d'un autre utilisateur? O/N: ")
                        if choix.upper() =="O":
                            break
                        elif choix.upper() == "N":
                            b = False
                            break
                        else:
                            continue
            elif fourth_admin_choice == "3":
                b = True
                while b:
                    id_user=input("veuillez entrer l'identifiant du passager que vous retirer de votre flotte: ")
                    delete=function.remove_passager_in_flotte(all_bus,check_id_user,id_user)
                    if delete == False:
                        print("1: pour essayer de nouveau")
                        print("r: retour")
                        while True:
                            des = input(" Entrer votre choix: ")
                            if des == "1":
                                break
                            if des == "r":
                                b = False
                                break
                            else: 
                                continue
                    else:
                        delet=function.remove_in_passager(id_user,all_passager)
                        all_passager = delet
                        all_bus = delete[0]
                        check_id_user = delete[1]
                        b = False
            elif fourth_admin_choice == "r":
                break
    elif first_admin_choice == "q":
        true = False
    else:
        continue
                    
            
                
            
        
       
       
        
