def readfile(Pokemon):
    import csv
    with open('pokedex.csv','rb') as pokedex:
        data=str(pokedex.read()).split(',')
        pokemons=[]
        try:
            for i in range(0, 1000):
                pokemons.append(Pokemon(data[36+(34*i)], data[37+(34*i)], data[45+(34*i)], data[47+(34*i)], data[52+(34*i)]))
        except IndexError:
            pass
        return pokemons
