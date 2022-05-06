#Your application must perform basic CRUD (Create, Read, Update, Delete) functionality with data stored in a database
#Your application must be able to read JSON or CSV files, and store the data contained within those files in a database
#Your application should have a CLI where users can interact with the application while it is running

# Importing pokemon module
from asyncio.windows_events import NULL
from pickle import NONE
import pokemon
import re
from pymongo import MongoClient

# Used to create pokemon object from user-inputted values
def add_pokemon() -> pokemon.pokemon:
    # Input verification
    while True:
        try:
            print("\n\nEnter pkmn number:")
            pokenumber = (input(">>>"))
            if not re.search(r"[,\.\\\*\-]", pokenumber) == None:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please do not use special characters in pokemon number")

    while True:
        try:
            print("\n\nEnter pkmn name:")
            pokename = str(input(">>>"))
            if not re.search(r"[,\.\\\*\-]", pokename) == None:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please do not use special characters in pokemon name")

    while True:
        try:
            print("\n\nEnter first type:")
            type1 = str(input(">>>"))
            if not re.search(r"[,\.\\\*\-]", type1) == None:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please do not use special characters in pokemon type")

    while True:
        try:
            print("\n\nEnter sub type:")
            type2 = str(input(">>>"))
            if not re.search(r"[,\.\\\*\-]", type2) == None:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please do not use special characters in pokemon type")

    newPokemon = pokemon.pokemon(pokenumber, pokename, type1, type2)
    return newPokemon

# Save pokemon list to saved_pokemon.txt
def save_pokemon(lst_pokemon):
    f = open('C:/Users/pqppe/OneDrive/Desktop/PortableGit/2022 revature/220404-big-data/foundation project/saved_pokemon.txt', 'w')

    for pokemon in lst_pokemon:
        f.write(str(pokemon.pokenumber) + ',' + str(pokemon.pokename) + ', ' + str(pokemon.type1) + ',' + str(pokemon.type2) + "\n")

    f.close()

# Load pokemon from saved_pokemon.txt
def load_pokemon():
    f = open('C:/Users/pqppe/OneDrive/Desktop/PortableGit/2022 revature/220404-big-data/foundation project/saved_pokemon.txt', 'r')
    lst_pokemon = []
    for line in f:
        if line == '':
            break

        pokemon_data = line.split(',')
        newPokemon = pokemon.pokemon(pokemon_data[0], pokemon_data[1], pokemon_data[2], pokemon_data[3])

        lst_pokemon.append(newPokemon)
    f.close()
    return lst_pokemon

# Function to save an pokemon to collection in MongoDB
def save_to_db(pokemon, pokedex):
    dict_pokemon = {
        "index" : pokemon.pokenumber,
        "name" : pokemon.name,
        "type" : pokemon.type1,
        "subtype" : pokemon.type2
    }

    pokedex.pokemon.insert_one(dict_pokemon)

# funciton to update element

def update_pokemon():
    print("please give the index number of the file you wish to change")
    user_file_choice = int(input(">>>"))
    with open("C:/Users/pqppe/OneDrive/Desktop/PortableGit/2022 revature/220404-big-data/foundation project/saved_pokemon.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if re.match(str(user_file_choice), i) != NONE:
                while True:
                    try:
                        print(i)
                        print("select attribute you wish to change \n a) name \n b) primary type \n c) secondary type")
                        user_attribute_change = str(input(">>>"))
                        if user_attribute_change == 'a':
                            print("to confirm name change, please print original name: \n")
                            orig_name = input(">>>")
                            print("please give a new name: \n")
                            namechange = str(input(">>>"))
                            f.replace(orig_name , str(namechange))
                            print("pokemon is renamed to ", namechange)
                        
                        elif user_attribute_change == 'b':
                            print("to confirm type change, please print original type1: \n")
                            orig_type1 = input(">>>")
                            print("please give a primary type: \n")
                            primarytype = str(input(">>>"))
                            f.replace(orig_type1 , str(namechange))
                            print("pokemon's primary type is reclassified as ", primarytype)
                        
                        elif user_attribute_change == 'c':
                            print("to confirm type change, please print original type2: \n")
                            orig_type2 = input(">>>")
                            print("please give a secondary type: \n")
                            secondarytype = str(input(">>>"))
                            f.replace(orig_type2 , str(namechange))
                            print("pokemon's secondary type is reclassified as ", secondarytype)
                        else:
                            raise ValueError('Invalid menu option')

                    except ValueError as ve:
                        print(ve)
                        print("Please enter a valid command")
                        pass

    f.truncate()
            
# function to delete element

def delete_pokemon():
    print("please give index number of pokemon file you wish to remove")
    user_input = int(input(">>>"))
    print("deleting entry:", user_input)
    with open("C:/Users/pqppe/OneDrive/Desktop/PortableGit/2022 revature/220404-big-data/foundation project/saved_pokemon.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if re.match(str(user_input), i) == NONE:
                f.write(i)
        f.truncate()
        f.close()
    return

#Main function
def main():
    check_conn = True
    try:
        client = MongoClient("127.0.0.1", 27017)

        pokedex = client.pokemon
    except BaseException:
        print("Sorry, could not connect!")
        check_conn = False

    lst_pokemon = load_pokemon()
    while True:
        try:
            print("Hello! Please select action")
            print("\t a) add file")
            print("\t b) change information in a file")
            print("\t c) display all files")
            print("\t d) delete file")
            print("\t e) save file to saved_pokemon.txt")
            print("\t s) Save all Pokemon to MongoDB (only run once!)")
            print("\t q) quit program")
            user_input = input(">>>")

            if user_input == 'a':
                print("adding pokemon")
                lst_pokemon.append(add_pokemon())

            #updating entry in list
            elif user_input == 'b':
                update_pokemon()

            elif user_input == 'c':
                for pokemon in lst_pokemon:
                    print(pokemon, type(pokemon))

            #deleting entry from list
            elif user_input == 'd':
                delete_pokemon()
    
            elif user_input == 'q':
                break

            elif user_input == 'e':
                save_pokemon(lst_pokemon)

            elif user_input == 's' and check_conn:
                try:
                    for pokemon in lst_pokemon:
                        save_to_db(pokemon, pokedex)
                except BaseException:
                    print("Sorry, could not make a good connection to db!")

            elif user_input == 's' and not check_conn:
                print("Sorry! Connection to db not established")

            else:
                raise ValueError('Invalid menu option')

        except ValueError as ve:
            print(ve)
            print("Please enter a valid command ('a', 'b', 'c', 'd', 's', 'q')")
            pass
            
            
    for pokemon in lst_pokemon:
        print(pokemon, type(pokemon))
    
    save_pokemon(lst_pokemon)


if __name__ == '__main__':
    main()





