#Your application must perform basic CRUD (Create, Read, Update, Delete) functionality with data stored in a database
#Your application must be able to read JSON or CSV files, and store the data contained within those files in a database
#Your application should have a CLI where users can interact with the application while it is running

from asyncio.windows_events import NULL
from queue import Empty
import re
import csv

class pokemon:

# Constructor/initializer of object
    def add_pokemon(self,poke_number,name,type1,type2):
        self.poke_number = poke_number
        self.pokename = name
        self.type1 = type1
        self.type2 = type2
    def add_pokemon(self):
        while True:
            try:
                print("\n\nEnter pokedex index number:")
                pokemon.poke_number = int(input(">>>"))
                break
            except ValueError:
                print("Oh no! You must enter a number for the pokedex index! Try again!")
        while True:
            try:
                print("\n\nEnter pokemon name:")
                self.pokename = input(">>>")
                if not re.search(r"[,\.\\\*\-]", self.pokename) == None:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Please do not use special characters in your name for your pokemon!")
        print("please enter type1 of pokemon \n")
        self.type1 = input (">>>")
        print("please enter type2 of pokemon \n")
        self.type2 = input (">>>")
        
#printing info of self

    def show_info(self):
        print(self.poke_number, "\n", self.pokename, "\n", self.type1, "\n", self.type2)
    def show_info():
        for obj in pokemon:
            print(obj.poke_number, ",", obj.pokename, ":", obj.type1, "/", obj.type2)

#reading info of self

#reading from csv
    def add_file_csv():
        print("please enter the full path and name of file:\n")
        name_of_csv_file = input (">>>")
        csvFile = csv.DictReader(name_of_csv_file)
        line_count = 0
        for row in csvFile:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} Name: {row[1]}, Type:{row[2]}. Subtype:{row[3]}.')
                line_count += 1

#updating values for b/c

    def change_b(self):
        while True:
                try:
                    print("input new value for ", self.b)
                    self.b = input(">>>")
                    if not re.search(r"[,\.\\\*\-]", self.b) == None:
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("Please do not use special characters for this value.")
        print(self, "'s b is now:", self.b)
        
    def change_c(self):
        while True:
                try:
                    print("input new value for ", self.c)
                    self.c = input(">>>")
                    if not re.search(r"[,\.\\\*\-]", self.c) == None:
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("Please do not use special characters for this value.")
        print(self, "'s c is now:", self.c)

#deleting entries

    def delete_info(self):
        self.poke_number = NULL
        self.pokename = NULL
        self.type1 = NULL
        self.type2 = NULL
        self = NULL

    while True:
        try:
            print("pokedex mockup, please select an action")
            print("\t a) add file")
            print("\t b) add file via csv")
            print("\t b) display file")
            print("\t c) delete file")
            print("\t q) quit program")
            user_input = input(">>>")

        
            if user_input == 'a':
                add_pokemon()
            elif user_input == 'b':
                add_file_csv()
            elif user_input == 'c':
                show_info()
            elif user_input =='d':
                print("input name of file you wish to delete:")
                user_input = input(">>>")
                delete_info(user_input)
            elif user_input == 'q':
                break
            elif user_input != 'a' and user_input != 'b' and user_input != 'c' and user_input!= 'q':
                raise ValueError('Invalid input for action')
        except ValueError:
            print("please select an action")
            continue
            