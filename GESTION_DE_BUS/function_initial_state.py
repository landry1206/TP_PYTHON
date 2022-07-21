
import csv
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
all_bus=[]
all_passager = []
check_id_user = []
check_id_bus=[]

# création de bus initiaux
def create_bus():
    array = []
    with open('GESTION_DE_BUS/bus.csv') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=';')
            current_bus_model = copy.deepcopy(bus_model)   
            lineCount = 0 
            
            for item in csvReader:
                current_bus_model = copy.deepcopy(bus_model)  
                current_bus_model["id"] = item[0]    
                current_bus_model["place_max"] = item[1]    
                current_bus_model["place_oqp"] = item[2]    
                all_bus.append(current_bus_model)
                check_id_bus.append(item[0])
                lineCount += 1
            array.append(all_bus)
            array.append(check_id_bus)
            return array

# création de passager initiaux
def create_user():
    array = []
    with open('GESTION_DE_BUS/passager.csv') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            current_passager_model = copy.deepcopy(passager_model)   
            lineCount = 0 
            
            for item in csvReader:
                current_passager_model = copy.deepcopy(passager_model)  
                current_passager_model["id"] = item[0]    
                current_passager_model["nom"] = item[1]    
                current_passager_model["bagage"] = item[2]    
                all_passager.append(current_passager_model)
                check_id_user.append(item[0])
                lineCount += 1
            array.append(all_passager)
            array.append(check_id_user)
            return array

# 
def add_user_in_bus():
    array = create_bus()
    table = []
    bus= array[0]
    array1 = create_user()
    user = array1[0]
    b = 0
    for i in bus:
        for a in user:
            bus[b]["passager"].append(a)
        b = b + 1
    table.append(bus[0])
    table.append(bus[1])
    table.append(bus[2])
    table.append(bus[3])
    table.append(bus[4])
    return table


def add_user(all_passager):
    array_passager = create_user()
    n = 1
    m=1
    for i in array_passager[0]:
        if n != i["id"]:
            for item in array_passager[0]:
                if i["id"] != n:
                    n = item["id"]
                    all_passager.append(i)
                    m= m+1
                    break
                else:
                    continue
        else:
            continue
        if m == 6:
            return all_passager
        
def check_id_users(check_id_user):
    array_id = create_user()
    n = 0
    for i in array_id[1]:
        check_id_user.append(i)
        n = n + 1
        if n == 5:
            return check_id_user
        
def check_id_buses(check_id_bus):
    array_id = create_bus()
    n = 0
    for i in array_id[1]:
        check_id_bus.append(i)
        n = n + 1
        if n == 5:
            return check_id_bus

        