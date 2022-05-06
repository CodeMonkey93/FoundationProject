# Parent class
from asyncio.windows_events import NULL

class pokemon:
    pokenumber = 'string'
    pokename = 'string'
    type1 = 'string'
    type2 = 'string'

    # Constructor/initializer of object
    def __init__(self, pknm, name, t1, t2):
        self.pokenumber = pknm
        self.pokename = name
        self.type1 = t1
        self.type2 = t2

    def __str__(self):
        return str(self.pokenumber) + "," + str(self.pokename) + "," + str(self.type1) + "," + str(self.type2)

    def __getitem__(self,index):
        return self.pokenumber[index]

def main():
    a1 = pokemon(1, 'i hate this', 'steel', 'dark')
    c1 = pokemon(2, 'what am i doing', 'ghost', 'dark')
    d1 = pokemon(3, 'i dont know', 'psychic', 'dark')

    lst_pkmn = [a1, c1, d1]

    for obj in lst_pkmn:
        print(obj)

if __name__ == '__main__':
    main()
