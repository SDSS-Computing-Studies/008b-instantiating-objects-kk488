#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""
class pet:
    animalType=""
    breed=""
    name=""
    owner=""
    birthdate=""

    def __init__(self,animalType,breed,name,owner,birthdate):
        self.animalType=animalType
        self.breed=breed
        self.name=name
        self.owner=owner
        self.birthdate=birthdate

    def display(self):
        print(self.name+" "+self.animalType)
        print(self.breed+" is owned by "+self.owner)
        
    def registerPet():
        print("type of animal?",end=" ")
        animalType=input()
        print("breed?",end=" ")
        breed=input()
        print("name?",end=" ")
        name=input()
        print("owner?",end=" ")
        owner=input()
        print("birthdate",end=" ")
        birthdate=input()
        return pet(animalType,breed.name,owner,birthdate)

    def retrievePet(petList):
        print("which pet",end=" ")
        name=input()
        for pet in petList:
            if pet.name==name:
                pet.display()

    def menu():
        print("1. enter a new pet")
        print("2. retrieve a pet")
        print("3. exit")

    def main():
        petList=[]
        while 1:
            menu()
            option=input()
            if option=="1":
                petList.append(registerPet())
            elif option=="2":
                retrievePet(petList)
            elif option=="3":
                break