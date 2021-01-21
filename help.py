import csv
#Type effectiveness
typeEffectiveness= {"Normal" : {"Normal": 1.0, "Fire": 1.0, "Water":1.0, "Electric":1.0, "Grass":1.0, "Ice":1.0, "Fighting": 2.0, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0, "Psychic": 1.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 0, "Dragon": 1.0,"Dark": 1.0, "Steel": 1.0, "Fairy":1.0},
"Fire" : {"Normal": 1.0, "Fire": .5, "Water":2.0, "Electric":1.0, "Grass":.5, "Ice":.5, "Fighting": 1, "Poison": 1.0, "Ground": 2.0, "Flying": 1.0, "Psychic": 1.0, "Bug": .5, "Rock": 2.0, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": .5, "Fairy":.5},
"Water" : {"Normal": 1.0, "Fire": .5, "Water":.5, "Electric":2.0, "Grass":2.0, "Ice":.5, "Fighting": 1.0, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0, "Psychic": 1.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": .5, "Fairy":1.0},
"Electric" : {"Normal": 1.0, "Fire": 1.0, "Water":1.0, "Electric":.5, "Grass":1.0, "Ice":1.0, "Fighting": 1.0, "Poison": 1.0, "Ground": 2.0, "Flying": .5, "Psychic": 1.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": .5, "Fairy":1.0},
"Grass" : {"Normal": 1.0, "Fire": 2.0, "Water":.5, "Electric":.5, "Grass":.5, "Ice":2.0, "Fighting": 1.0, "Poison": 2.0, "Ground": .5, "Flying": 2.0, "Psychic": 1.0, "Bug": 2.0, "Rock": 1.0, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": 1.0, "Fairy":1.0},
"Ice" : {"Normal": 1.0, "Fire": 2.0, "Water":1.0, "Electric":1.0, "Grass":1.0, "Ice":.5, "Fighting": 2.0, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0, "Psychic": 1.0, "Bug": 1.0, "Rock": 2.0, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": 2.0, "Fairy":1.0},
"Fighting" : {"Normal": 1.0, "Fire": 1.0, "Water":1.0, "Electric":1.0, "Grass":1.0, "Ice":1.0, "Fighting": 1.0, "Poison": 1.0, "Ground": 1.0, "Flying": 2.0, "Psychic": 2.0, "Bug": .5, "Rock": .5, "Ghost": 1.0, "Dragon": 1.0,"Dark": .5, "Steel": 1.0, "Fairy":2.0},
"Poison" : {"Normal": 1.0, "Fire": 1.0, "Water":1.0, "Electric":1.0, "Grass":.5, "Ice":1.0, "Fighting": .5, "Poison": .5, "Ground": 2.0, "Flying": 1.0, "Psychic": 2.0, "Bug": .5, "Rock": 1.0, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": 1.0, "Fairy":.5},
"Ground" : {"Normal": 1.0, "Fire": 1.0, "Water":2.0, "Electric":0, "Grass":2.0, "Ice":2.0, "Fighting": 1.0, "Poison": .5, "Ground": 1.0, "Flying": 1.0, "Psychic": 1.0, "Bug": 1.0, "Rock": .5, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": 1.0, "Fairy":1.0},
"Flying" : {"Normal": 1.0, "Fire": 1.0, "Water":1.0, "Electric":2.0, "Grass":.5, "Ice":2.0, "Fighting": .5, "Poison": 1.0, "Ground": 0, "Flying": 1.0, "Psychic": 1.0, "Bug": .5, "Rock": 2.0, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": 1.0, "Fairy":1.0},
"Psychic" : {"Normal": 1.0, "Fire": 1.0, "Water":1.0, "Electric":1.0, "Grass":1.0, "Ice":1.0, "Fighting": .5, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0, "Psychic": .5, "Bug": 2.0, "Rock": 1.0, "Ghost": 2.0, "Dragon": 1.0,"Dark": 2.0, "Steel": 1.0, "Fairy":1.0},
"Bug" : {"Normal": 1.0, "Fire": 2.0, "Water":1.0, "Electric":1.0, "Grass":.5, "Ice":1.0, "Fighting": .5, "Poison": 1.0, "Ground": .5, "Flying": 2.0, "Psychic": 1.0, "Bug": 1.0, "Rock": 2.0, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": 1.0, "Fairy":1.0},
"Rock" : {"Normal": .5, "Fire": .5, "Water":2.0, "Electric":1.0, "Grass":2.0, "Ice":1.0, "Fighting": 2.0, "Poison": .5, "Ground": 2.0, "Flying": .5, "Psychic": 1.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": 2.0, "Fairy":1.0},
"Ghost" : {"Normal": 0, "Fire": 1.0, "Water":1.0, "Electric":1.0, "Grass":1.0, "Ice":1.0, "Fighting": 0, "Poison": .5, "Ground": 1.0, "Flying": 1.0, "Psychic": 1.0, "Bug": .5, "Rock": 1.0, "Ghost": 2.0, "Dragon": 1.0,"Dark": 2.0, "Steel": 1.0, "Fairy":1.0},
"Dragon" : {"Normal": 1.0, "Fire": .5, "Water":.5, "Electric":.5, "Grass":.5, "Ice":2.0, "Fighting": 1.0, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0, "Psychic": 1.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 1.0, "Dragon": 2.0,"Dark": 1.0, "Steel": 1.0, "Fairy":2.0},
"Dark" : {"Normal": 1.0, "Fire": 1.0, "Water":1.0, "Electric":1.0, "Grass":1.0, "Ice":1.0, "Fighting": 2.0, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0, "Psychic": 0, "Bug": 2.0, "Rock": 1.0, "Ghost": .5, "Dragon": 1.0,"Dark": .5, "Steel": 1.0, "Fairy":2.0},
"Steel" : {"Normal": .5, "Fire": 2.0, "Water":1.0, "Electric":1.0, "Grass":.5, "Ice":.5, "Fighting": 2.0, "Poison": 0, "Ground": 2.0, "Flying": .5, "Psychic": .5, "Bug": .5, "Rock": .5, "Ghost": 1.0, "Dragon": .5,"Dark": 1.0, "Steel": .5, "Fairy":.5},
"Fairy" : {"Normal": 1.0, "Fire": 1.0, "Water":1.0, "Electric":1.0, "Grass":1.0, "Ice":1.0, "Fighting": .5, "Poison": 2.0, "Ground": 1.0, "Flying": 1.0, "Psychic": 1.0, "Bug": .5, "Rock": 1.0, "Ghost": 1.0, "Dragon": 0,"Dark": .5, "Steel": 2.0, "Fairy":1.0}}
#Keeping none below if needed
Nill = {"Normal": 1.0, "Fire": 1.0, "Water":1.0, "Electric":1.0, "Grass":1.0, "Ice":1.0, "Fighting": 1.0, "Poison": 1.0, "Ground": 1.0, "Flying": 1.0, "Psychic": 1.0, "Bug": 1.0, "Rock": 1.0, "Ghost": 1.0, "Dragon": 1.0,"Dark": 1.0, "Steel": 1.0, "Fairy":1.0}

def grabData(poke):
    file = open("pokemon.csv","r")
    reader = csv.reader(file, delimiter=',')
    wantedPoke = []
    for row in reader:
        if row[3] == "NAME":
            categories = row
        #print(row)
        if row[3] == poke:
            wantedPoke = row
            #print("Found it")
            break
    if not wantedPoke:
        return -1
    else:
        index = 0
        pokeDict = {}
        stats = {}
        abilities = {}
        types = {}
        for cat in categories:
            if cat in ('HP','ATK','DEF','SP_ATK','SP_DEF','SPD','TOTAL'):
                stats[cat] = wantedPoke[index]
            elif "TYPE" in cat:
                types[cat] = wantedPoke[index]
            elif "ABILITY" in cat:
                abilities[cat] = wantedPoke[index]
            elif cat == "":
                pass
            else:
                pokeDict[cat] = wantedPoke[index]
            index+=1
            
        pokeDict["STATS"] = stats
        pokeDict["ABILITIES"] = abilities
        pokeDict["TYPES"] = types
        pokeDict["EFFECTIVENESS"] = calcEffectiveness(pokeDict["TYPES"]["TYPE1"], pokeDict["TYPES"]["TYPE2"])
        return pokeDict

def grabDataByNumber(number):
    file = open("pokemon.csv","r")
    reader = csv.reader(file, delimiter=',')
    wantedPoke = []
    for row in reader:
        if row[0] == "NUMBER":
            categories = row
        #print(row)
        if row[0] == number:
            wantedPoke = row
            print("Found it")
            break
    if not wantedPoke:
        return -1
    else:
        index = 0
        pokeDict = {}
        stats = {}
        abilities = {}
        types = {}
        for cat in categories:
            if cat in ('HP','ATK','DEF','SP_ATK','SP_DEF','SPD','TOTAL'):
                stats[cat] = wantedPoke[index]  
            elif "TYPE" in cat:
                types[cat] = wantedPoke[index]
            elif "ABILITY" in cat:
                abilities[cat] = wantedPoke[index]
            elif cat == "":
                pass
            else:
                pokeDict[cat] = wantedPoke[index]
            index+=1
            
        pokeDict["STATS"] = stats
        pokeDict["ABILITIES"] = abilities
        pokeDict["TYPES"] = types
        pokeDict["EFFECTIVENESS"] = calcEffectiveness(pokeDict["TYPES"]["TYPE1"], pokeDict["TYPES"]["TYPE2"])
        return pokeDict

def calcEffectiveness(type1,type2):
    if type1 in typeEffectiveness:
        t1 = typeEffectiveness[type1]
    else:
        t1=Nill
    if type2 in typeEffectiveness:
        t2 = typeEffectiveness[type2]
    else:
        t2 = Nill
    tempDict={}
    for t in t1:
        tempDict[t]=t1[t]*t2[t]
    
    effectiveness={"4":[],"2":[],"1":[],"1/2":[],"1/4":[], "0": []}
    for i in tempDict:
        if tempDict[i] == 4.0:
            effectiveness["4"].append(i)
        elif tempDict[i] == 2.0:
            effectiveness["2"].append(i)
        elif tempDict[i] == 1.0:
            effectiveness["1"].append(i)
        elif tempDict[i] == .5:
            effectiveness["1/2"].append(i)
        elif tempDict[i] == .25:
            effectiveness["1/4"].append(i)
        elif tempDict[i] == 0:
            effectiveness["0"].append(i)
    return effectiveness



#file = open("pokemon.csv","r")
#reader = csv.reader(file, delimiter=',')
#for row in reader:
#    
#    temp = calcEffectiveness(row[4],row[5])
#    if(temp["0"]):
#        print(row[3]+": ("+row[4]+","+row[5]+")")
#        for i in temp:
#            print(i +" "+ str(temp[i]))

#file = open("pokemon.csv","r")
#reader = csv.reader(file, delimiter=',')
#end = "["
#for row in reader:
#    end += ("\""+row[3]+"\""+", ")
#end+="]"
#print(end)