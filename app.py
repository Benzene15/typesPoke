from help import *
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return """
    <form action="https://bulbapedia.bulbagarden.net/wiki/Yanmega_(Pok%C3%A9mon)">
    <input type="submit" value="Go to Google" />
    </form>"""

@app.route("/load/<string:poke>")
def pokemon(poke):
    if(poke in pokemonNames):
        dataList = grabData(poke)
        return render_template("poke.html", dataList = dataList)
    else:
        return "This pokemon does not exist"

@app.route("/data/name/<string:poke>")
def data(poke):
    dataList = grabData(poke)
    #print(dataList)
    if(dataList == -1):
        return {poke: "Not found"}
    return dataList

@app.route("/data/number/<string:number>")
def getData(number):
    dataList = grabDataByNumber(number)
    #print(dataList)
    if(dataList == -1):
        return {number: "Not found"}
    return dataList


pokemonNames = ["Bulbasaur", "Ivysaur", "Venusaur", "Mega Venusaur", "Charmander", "Charmeleon", "Charizard", "Mega Charizard X", "Mega Charizard Y", "Squirtle", 
    "Wartortle", "Blastoise", "Mega Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Mega Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", 
    "Mega Pidgeot", "Rattata", "Rattata", "Raticate", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Raichu", "Sandshrew", "Sandshrew", 
    "Sandslash", "Sandslash", "Nidoran F", "Nidorina", "Nidoqueen", "Nidoran M", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Vulpix", "Ninetales", 
    "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Diglett", 
    "Dugtrio", "Dugtrio", "Meowth", "Meowth", "Meowth", "Persian", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", 
    "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Mega Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", 
    "Tentacruel", "Geodude", "Geodude", "Graveler", "Graveler", "Golem", "Golem", "Ponyta", "Ponyta", "Rapidash", "Rapidash", "Slowpoke", "Slowpoke", "Slowbro", 
    "Slowbro", "Mega Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Grimer", "Muk", "Muk", 
    "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Mega Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", 
    "Exeggutor", "Exeggutor", "Cubone", "Marowak", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", 
    "Tangela", "Kangaskhan", "Mega Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", 
    "Magmar", "Pinsir", "Mega Pinsir", "Tauros", "Magikarp", "Gyarados", "Mega Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", 
    "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Mega Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", 
    "Mewtwo", "Mega Mewtwo X", "Mega Mewtwo Y", "Mew", "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", 
    "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", 
    "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Mega Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", 
    "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet", 
    "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Mega Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Mega Scizor", "Shuckle", 
    "Heracross", "Mega Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Corsola", "Remoraid", "Octillery", 
    "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Mega Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", 
    "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Mega Tyranitar", "Lugia", 
    "Ho-Oh", "Celebi", "Treecko", "Grovyle", "Sceptile", "Mega Sceptile", "Torchic", "Combusken", "Blaziken", "Mega Blaziken", "Mudkip", "Marshtomp", "Swampert", 
    "Mega Swampert", "Poochyena", "Mightyena", "Zigzagoon", "Zigzagoon", "Linoone", "Linoone", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox", "Lotad", 
    "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry", "Taillow", "Swellow", "Wingull", "Pelipper", "Ralts", "Kirlia", "Gardevoir", "Mega Gardevoir", "Surskit", 
    "Masquerain", "Shroomish", "Breloom", "Slakoth", "Vigoroth", "Slaking", "Nincada", "Ninjask", "Shedinja", "Whismur", "Loudred", "Exploud", "Makuhita", "Hariyama", 
    "Azurill", "Nosepass", "Skitty", "Delcatty", "Sableye", "Mega Sableye", "Mawile", "Mega Mawile", "Aron", "Lairon", "Aggron", "Mega Aggron", "Meditite", "Medicham", 
    "Mega Medicham", "Electrike", "Manectric", "Mega Manectric", "Plusle", "Minun", "Volbeat", "Illumise", "Roselia", "Gulpin", "Swalot", "Carvanha", "Sharpedo", 
    "Mega Sharpedo", "Wailmer", "Wailord", "Numel", "Camerupt", "Mega Camerupt", "Torkoal", "Spoink", "Grumpig", "Spinda", "Trapinch", "Vibrava", "Flygon", "Cacnea", 
    "Cacturne", "Swablu", "Altaria", "Mega Altaria", "Zangoose", "Seviper", "Lunatone", "Solrock", "Barboach", "Whiscash", "Corphish", "Crawdaunt", "Baltoy", "Claydol", 
    "Lileep", "Cradily", "Anorith", "Armaldo", "Feebas", "Milotic", "Castform", "Castform", "Castform", "Castform", "Kecleon", "Shuppet", "Banette", "Mega Banette", 
    "Duskull", "Dusclops", "Tropius", "Chimecho", "Absol", "Mega Absol", "Wynaut", "Snorunt", "Glalie", "Mega Glalie", "Spheal", "Sealeo", "Walrein", "Clamperl", 
    "Huntail", "Gorebyss", "Relicanth", "Luvdisc", "Bagon", "Shelgon", "Salamence", "Mega Salamence", "Beldum", "Metang", "Metagross", "Mega Metagross", "Regirock", 
    "Regice", "Registeel", "Latias", "Mega Latias", "Latios", "Mega Latios", "Kyogre", "Primal Kyogre", "Groudon", "Primal Groudon", "Rayquaza", "Mega Rayquaza", 
    "Jirachi", "Deoxys", "Deoxys", "Deoxys", "Deoxys", "Turtwig", "Grotle", "Torterra", "Chimchar", "Monferno", "Infernape", "Piplup", "Prinplup", "Empoleon", 
    "Starly", "Staravia", "Staraptor", "Bidoof", "Bibarel", "Kricketot", "Kricketune", "Shinx", "Luxio", "Luxray", "Budew", "Roserade", "Cranidos", "Rampardos", 
    "Shieldon", "Bastiodon", "Burmy", "Burmy", "Burmy", "Wormadam", "Wormadam", "Wormadam", "Mothim", "Combee", "Vespiquen", "Pachirisu", "Buizel", "Floatzel", 
    "Cherubi", "Cherrim", "Cherrim", "Shellos", "Shellos", "Gastrodon", "Gastrodon", "Ambipom", "Drifloon", "Drifblim", "Buneary", "Lopunny", "Mega Lopunny", 
    "Mismagius", "Honchkrow", "Glameow", "Purugly", "Chingling", "Stunky", "Skuntank", "Bronzor", "Bronzong", "Bonsly", "Mime Jr.", "Happiny", "Chatot", 
    "Spiritomb", "Gible", "Gabite", "Garchomp", "Mega Garchomp", "Munchlax", "Riolu", "Lucario", "Mega Lucario", "Hippopotas", "Hippowdon", "Skorupi", "Drapion", 
    "Croagunk", "Toxicroak", "Carnivine", "Finneon", "Lumineon", "Mantyke", "Snover", "Abomasnow", "Mega Abomasnow", "Weavile", "Magnezone", "Lickilicky", "Rhyperior", 
    "Tangrowth", "Electivire", "Magmortar", "Togekiss", "Yanmega", "Leafeon", "Glaceon", "Gliscor", "Mamoswine", "Porygon-Z", "Gallade", "Mega Gallade", "Probopass", 
    "Dusknoir", "Froslass", "Rotom", "Rotom", "Rotom", "Rotom", "Rotom", "Rotom", "Uxie", "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas", "Giratina", 
    "Giratina", "Cresselia", "Phione", "Manaphy", "Darkrai", "Shaymin", "Shaymin", "Arceus", "Victini", "Snivy", "Servine", "Serperior", "Tepig", "Pignite", "Emboar", 
    "Oshawott", "Dewott", "Samurott", "Patrat", "Watchog", "Lillipup", "Herdier", "Stoutland", "Purrloin", "Liepard", "Pansage", "Simisage", "Pansear", "Simisear", 
    "Panpour", "Simipour", "Munna", "Musharna", "Pidove", "Tranquill", "Unfezant", "Blitzle", "Zebstrika", "Roggenrola", "Boldore", "Gigalith", "Woobat", "Swoobat", 
    "Drilbur", "Excadrill", "Audino", "Mega Audino", "Timburr", "Gurdurr", "Conkeldurr", "Tympole", "Palpitoad", "Seismitoad", "Throh", "Sawk", "Sewaddle", "Swadloon", 
    "Leavanny", "Venipede", "Whirlipede", "Scolipede", "Cottonee", "Whimsicott", "Petilil", "Lilligant", "Basculin", "Basculin", "Sandile", "Krokorok", "Krookodile", 
    "Darumaka", "Darumaka", "Darmanitan", "Darmanitan", "Darmanitan", "Darmanitan", "Maractus", "Dwebble", "Crustle", "Scraggy", "Scrafty", "Sigilyph", "Yamask", 
    "Yamask", "Cofagrigus", "Tirtouga", "Carracosta", "Archen", "Archeops", "Trubbish", "Garbodor", "Zorua", "Zoroark", "Minccino", "Cinccino", "Gothita", "Gothorita", 
    "Gothitelle", "Solosis", "Duosion", "Reuniclus", "Ducklett", "Swanna", "Vanillite", "Vanillish", "Vanilluxe", "Deerling", "Deerling", "Deerling", "Deerling", 
    "Sawsbuck", "Sawsbuck", "Sawsbuck", "Sawsbuck", "Emolga", "Karrablast", "Escavalier", "Foongus", "Amoonguss", "Frillish", "Jellicent", "Alomomola", "Joltik", 
    "Galvantula", "Ferroseed", "Ferrothorn", "Klink", "Klang", "Klinklang", "Tynamo", "Eelektrik", "Eelektross", "Elgyem", "Beheeyem", "Litwick", "Lampent", 
    "Chandelure", "Axew", "Fraxure", "Haxorus", "Cubchoo", "Beartic", "Cryogonal", "Shelmet", "Accelgor", "Stunfisk", "Stunfisk", "Mienfoo", "Mienshao", "Druddigon", 
    "Golett", "Golurk", "Pawniard", "Bisharp", "Bouffalant", "Rufflet", "Braviary", "Vullaby", "Mandibuzz", "Heatmor", "Durant", "Deino", "Zweilous", "Hydreigon", 
    "Larvesta", "Volcarona", "Cobalion", "Terrakion", "Virizion", "Tornadus", "Tornadus", "Thundurus", "Thundurus", "Reshiram", "Zekrom", "Landorus", "Landorus", 
    "Kyurem", "Kyurem", "Kyurem", "Keldeo", "Keldeo", "Meloetta", "Meloetta", "Genesect", "Chespin", "Quilladin", "Chesnaught", "Fennekin", "Braixen", "Delphox", 
    "Froakie", "Frogadier", "Greninja", "Greninja", "Bunnelby", "Diggersby", "Fletchling", "Fletchinder", "Talonflame", "Scatterbug", "Spewpa", "Vivillon", "Litleo", 
    "Pyroar", "Flabebe", "Floette", "Florges", "Skiddo", "Gogoat", "Pancham", "Pangoro", "Furfrou", "Espurr", "Meowstic M", "Meowstic F", "Honedge", "Doublade", 
    "Aegislash", "Aegislash", "Spritzee", "Aromatisse", "Swirlix", "Slurpuff", "Inkay", "Malamar", "Binacle", "Barbaracle", "Skrelp", "Dragalge", "Clauncher", 
    "Clawitzer", "Helioptile", "Heliolisk", "Tyrunt", "Tyrantrum", "Amaura", "Aurorus", "Sylveon", "Hawlucha", "Dedenne", "Carbink", "Goomy", "Sliggoo", "Goodra", 
    "Klefki", "Phantump", "Trevenant", "Pumpkaboo", "Pumpkaboo", "Pumpkaboo", "Pumpkaboo", "Gourgeist", "Gourgeist", "Gourgeist", "Gourgeist", "Bergmite", "Avalugg", 
    "Noibat", "Noivern", "Xerneas", "Yveltal", "Zygarde", "Zygarde", "Zygarde", "Diancie", "Mega Diancie", "Hoopa", "Hoopa", "Volcanion", "Rowlet", "Dartrix", 
    "Decidueye", "Litten", "Torracat", "Incineroar", "Popplio", "Brionne", "Primarina", "Pikipek", "Trumbeak", "Toucannon", "Yungoos", "Gumshoos", "Grubbin", 
    "Charjabug", "Vikavolt", "Crabrawler", "Crabominable", "Oricorio", "Oricorio", "Oricorio", "Oricorio", "Cutiefly", "Ribombee", "Rockruff", "Rockruff", "Lycanroc", 
    "Lycanroc", "Lycanroc", "Wishiwashi", "Wishiwashi", "Mareanie", "Toxapex", "Mudbray", "Mudsdale", "Dewpider", "Araquanid", "Fomantis", "Lurantis", "Morelull", 
    "Shiinotic", "Salandit", "Salazzle", "Stufful", "Bewear", "Bounsweet", "Steenee", "Tsareena", "Comfey", "Oranguru", "Passimian", "Wimpod", "Golisopod", "Sandygast", 
    "Palossand", "Pyukumuku", "Type: Null", "Silvally", "Minior", "Minior", "Komala", "Turtonator", "Togedemaru", "Mimikyu", "Bruxish", "Drampa", "Dhelmise", 
    "Jangmo-o", "Hakamo-o", "Kommo-o", "Tapu Koko", "Tapu Lele", "Tapu Bulu", "Tapu Fini", "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Nihilego", "Buzzwole", 
    "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord", "Necrozma", "Necrozma", "Necrozma", "Necrozma", "Magearna", "Marshadow", "Poipole", "Naganadel", 
    "Stakataka", "Blacephalon", "Zeraora", "Meltan", "Melmetal", "Grookey", "Thwackey", "Rillaboom", "Scorbunny", "Raboot", "Cinderace", "Sobble", "Drizzile", 
    "Inteleon", "Skwovet", "Greedent", "Rookidee", "Convisquire", "Conviknight", "Blipbug", "Dottler", "Orbeetle", "Nickit", "Thievul", "Gossifleur", "Eldegoss", 
    "Wooloo", "Dubwool", "Chewtle", "Drednaw", "Yamper", "Boltund", "Rolycoly", "Carkol", "Coalossal", "Applin", "Flapple", "Appletun", "Silicobra", "Sandaconda", 
    "Cramorant", "Arrokuda", "Barraskewda", "Toxel", "Toxtricity", "Toxtricity", "Sizzlipede", "Centiskorch", "Clobbopus", "Grapploct", "Sinistea", "Polteageist", 
    "Hatenna", "Hattrem", "Hatterene", "Impidimp", "Morgrem", "Grimmsnarl", "Obstagoon", "Perrserker", "Cursola", "Sirfetch'd", "Mr. Rime", "Runerigus", "Milcery", 
    "Alcremie", "Falinks", "Pincurchin", "Snom", "Frosmoth", "Stonjourner", "Eiscue", "Eiscue", "Indeedee M", "Indeedee F", "Morpeko", "Cufant", "Copperajah", 
    "Dracozolt", "Arctozolt", "Dracovish", "Arctovish", "Duraludon", "Dreepy", "Drakloak", "Dragapult", "Zacian", "Zacian", "Zamazanta", "Zamazanta", "Eternatus", 
    "Kubfu", "Urshifu", "Urshifu", "Zarude", "Regieleki", "Regidrago", "Glastrier", "Spectrier", "Calyrex", "Calyrex", "Calyrex"]