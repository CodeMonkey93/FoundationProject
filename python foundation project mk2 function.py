#Your application must perform basic CRUD (Create, Read, Update, Delete) functionality with data stored in a database
#Your application must be able to read JSON or CSV files, and store the data contained within those files in a database
#Your application should have a CLI where users can interact with the application while it is running

# Importing pokemon module
from asyncio.windows_events import NULL
from pickle import NONE
import pokemon
import re
from pymongo import MongoClient

# a)
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

# b)
# funciton to update element

def update_pokemon():
    print("please give the index number of the file you wish to change")
    user_file_choice = int(input(">>>"))
    with open("saved_pokemon.txt", "r+") as f:
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
        f.close()

# d)            
# function to delete element

def delete_pokemon():
    print("please give index number of pokemon file you wish to remove")
    user_input = int(input(">>>"))
    print("deleting entry:", user_input)
    with open("saved_pokemon.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if re.match(str(user_input), i) == NONE:
                f.write(i)
        f.close()

# e)
# temporarilly store and display pokemon from saved_pokemon.txt
def display_from_file():
    f = open('saved_pokemon.txt', 'r')
    lst_from_file = []
    for line in f:
        if line == '':
            break

        pokemon_data = line.split(',')
        newPokemon = pokemon.pokemon(pokemon_data[0], pokemon_data[1], pokemon_data[2], pokemon_data[3])

        lst_from_file.append(newPokemon)
    f.close()
    for pokemon in lst_from_file:
        print(pokemon, type(pokemon))

# f)
# Save pokemon list to saved_pokemon.txt
def save_pokemon(lst_pokemon):
    f = open('saved_pokemon.txt', 'w')

    for pokemon in lst_pokemon:
        f.write(str(pokemon.pokenumber) + ',' + str(pokemon.pokename) + ', ' + str(pokemon.type1) + ',' + str(pokemon.type2) + "\n")

    f.close()

# Load pokemon from saved_pokemon.txt
def load_pokemon():
    f = open('saved_pokemon.txt', 'r')
    lst_pokemon = []
    for line in f:
        if line == '':
            break
        pokemon_data = line.split(',')
        newPokemon = pokemon.pokemon(pokemon_data[0], pokemon_data[1], pokemon_data[2], pokemon_data[3])
        lst_pokemon.append(newPokemon)
    f.close()
    return lst_pokemon

# s)
# Function to save a pokemon to collection in MongoDB
def save_to_db(pokemon, pokedex):
    dict_pokemon = {
        "index" : pokemon.pokenumber,
        "name" : pokemon.name,
        "type" : pokemon.type1,
        "subtype" : pokemon.type2
    }
    pokedex.pokemon.insert_one(dict_pokemon)

#MDisplay)
#function to display data from collection in MongoDB
def display_info_from_db(pokedex):
    print("please give index number of pokemon file you wish to display from MongoDB")
    user_index = int(input(">>>"))
    pokedex.find_one({"index": user_index })
    
#MUpdate)
#Function to manipulate data from collection in MongoDB
def Edit_from_db(pokedex):
    print("please give index number of pokemon file you wish to edit in MongoDB")
    user_index = int(input(">>>"))
    print("please give the attribute of pokemon file you wish to edit in MongoDB")
    print("\n 1)name of pokemon \n 2) primary attribute \n 3) sub attribute \n")
    user_choice = int(input(">>>"))
    if (user_choice == 1):
        print("please enter new name for pokemon")
        user_entry = (input(">>>"))
        pokedex.update_one({"index": user_index}, { "$set": {"pokename": user_entry}})
    if (user_choice == 2):
        print("please enter new primary type for pokemon")
        user_entry = (input(">>>"))
        pokedex.update_one({"index": user_index}, { "$set": {"type1": user_entry}})
    if (user_choice == 3):
        print("please enter new sub type for pokemon")
        user_entry = (input(">>>"))
        pokedex.update_one({"index": user_index}, { "$set": {"type2": user_entry}})
    elif:
        print("sorry, invalid selection")

#MDelete)
#Function to delete data rom collection in mongoDB
def delete_from_db(pokedex):
   print("please give index number of pokemon file you wish to delete from ongoDB")
   user_input = int(input(">>>"))
   pokedex.delete_one({"index": user_input})

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
            print("\t c) display all files currently in console")
            print("\t d) delete file")
            print("\t e) display all files currently in saved text file")
            print("\t f) save file to saved_pokemon.txt")
            print("\t s) Save all Pokemon to MongoDB (only run once!)")
            print("\t MDisplay) Display a file from MongoDB")
            print("\t MUpdate) Update a file from MongoDB")
            print("\t MDelete) Delete a file from MongoDB")
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
    
            elif user_input == 'e':
                display_from_file()

            elif user_input == 'f':
                save_pokemon(lst_pokemon)

            elif user_input == 's' and check_conn:
                try:
                    for pokemon in lst_pokemon:
                        save_to_db(pokemon, pokedex)
                except BaseException:
                    print("Sorry, could not make a good connection to db!")

            elif user_input == 'MDisplay' and check_conn:
                try:
                    display_info_from_db(pokedex)
                except BaseException:
                    print("Sorry, could not make a good connection to db!")

            elif user_input == 'MUpdate' and check_conn:
                try:
                    Edit_from_db(pokedex)
                except BaseException:
                    print("Sorry, could not make a good connection to db!")
            
            elif user_input == 'MDelete' and check_conn:
                try:
                    delete_from_db(pokedex)
                except BaseException:
                    print("Sorry, could not make a good connection to db!")

            elif user_input == 's' and not check_conn:
                print("Sorry! Connection to db not established")

            elif user_input == 'q':
                break

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
