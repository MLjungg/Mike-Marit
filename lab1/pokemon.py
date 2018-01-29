#Exercise one. Pokedex. Mikael Ljung & Marit. CINEK. VT18

class Pokemon:
    def __init__(self, name, hp, attack, defense, type1, mass):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.type1 = type1
        self.mass = mass

    def __str__(self):
        return str(self.type1) + ' type Pokemon ' + str(self.name)

    def __lt__(self, compare):
        return self.mass < compare.mass

    #Function that increases current pokemons hp. Indata self. No outdata.
    def motherload(self):
        self.hp = 1000000

    def suicide(self):
        self.hp = 0

class Gym:
    def __init__(self, type, pokelist):
        self.pokelist=pokelist
        self.type = type

    def __str__(self):
        return str(self.type) + 'type gym'

    def ismmember(self,searchedpokemon):
        pokemonexist=[]
        for eachpokemon in searchedpokemon:
            for gympokemon in self.pokelist:
                if eachpokemon == gympokemon:
                    pokemonexist.append(eachpokemon)
        return pokemonexist

    #Function that searches for the pokemon with highest hp. Indata self and outdata maxpokemon
    #So the pokemon with highest hp.
    def highesthp(self):
        maxpokemon = Pokemon('Maxpokemon',0,0,0,'None',0)
        if len(self.pokelist) == 0: #Check if list is empty
            return 'This gym has no pokemons'
        for pokemonininlist in self.pokelist:
            if pokemonininlist.hp > maxpokemon.hp:
                maxpokemon = pokemonininlist
        return maxpokemon

    #Function that adds pokemon to gym. Indata self and pokemon, pokemon is the pokemon that needs to be added.
    def addpokemon(self,pokemon):
        self.pokelist.extend(pokemon)

#Function that compairs different pokemons mass.
def exercise2():
    charmander = Pokemon('Charmander', 39, 52, 43, 'Fire', 8.5)
    squirtle = Pokemon('Squirtle', 44, 48, 65, 'Water', 9)

    #This executes the lt-function.
    if charmander < squirtle:
        print str(charmander) + ' is smaller than ' + str(squirtle)
    else:
        print str(charmander) + ' is not smaller than ' + str(squirtle)

#Function that reads file and creates a list with the files content
def exercise3():
    filename = 'pokedex.csv'
    pokelist = []
    with open(filename) as pokefile:
        next(pokefile) #Skip first line (headings)
        for row in pokefile:
            col = row.strip().split(',')
            pokemon = Pokemon(col[2], int(col[3]), int(col[4]), int(col[5]), col[10], float(col[16].split()[0]))
            pokelist.insert(0, pokemon) #Add pokemon to list
    return pokelist


#Function that tests created functions
def exercise6():
    #Creates pokemon-objects
    bulbasaur = Pokemon('Bulbasaur', 45, 49, 49, 'Grass', 6.9)
    charmander = Pokemon('Charmander', 39, 52, 43, 'Fire', 8.5)
    squirtle = Pokemon('Squirtle', 44, 48, 65, 'Water', 9)

    #Creates a list of pokemons for the gym
    grasspokelist = [bulbasaur, charmander]

    searched_pokemons=[bulbasaur, squirtle, charmander]

    gym1 = Gym('Grass', grasspokelist)
    foundpokemon=(gym1.ismmember(searched_pokemons))
    for i in range (0,len(foundpokemon)):
      print(foundpokemon[i].name)



def main():
    exercise2()
    exercise3()
    exercise6()
main()

