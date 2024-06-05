class Zoo:

    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

    def zookeepers(self, keeper:str):
        self.zoo_keepers.append(keeper)
    
    def _fences(self, fence):
        self.fences.append(fence)
    
    def describe_zoo(self):
        for keepers in self.zoo_keepers:
            print("\nGuardians:")
            print(keepers)
            for fence in self.fences:
                if fence in keepers.fences:
                    print("\nFences:")
                    print(fence)
                    print("with animal:")
                    for animal in fence.animals:
                        print(animal)
                    print("\n##############################")



class Fence:
    
    def __init__(self, area:float, temperature:int, habitat:str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
    
    def _animals(self,animal:str):
        self.animals.append(animal)

    def __str__(self):
        print()
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"
    

class Animal:

    def __init__(self, name:str, species:str, age:int, height:int, width:int, preferred_habitat:str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age),3)

    def __str__(self):
        print()
        return f"Animal(name={self.name}, species={self.species}, age={self.age}, height={self.height}, width={self.width}, preferred_habitat={self.preferred_habitat})"

    

class ZooKeeper:
        
    def __init__(self,  name:str, surname:str, id:int):
        self.name = name
        self.surname = surname
        self.id = id
        self.fences = []
    
    def __str__(self):
        print()
        return f"Zookeeper(name={self.name}, surname={self.surname}, id={self.id})" 

    def add_fences(self, fence):
        self.fences.append(fence)
    
    def add_animals(self,animal:Animal,fence:Fence):
        self.animal = animal
        self.fence = fence
        if fence.area >= animal.height * animal.width and animal.preferred_habitat == fence.habitat:
            fence.animals.append(animal)
            fence.area -= animal.height * animal.width 
        

    def remove_animal(self, animal:Animal, fence:Fence):
        self.animal = animal
        self.fence = fence 
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += animal.height * animal.width
           
    
    def feed_animal(self,animal:Animal):
        self.animal = animal
        for fence in self.fences:
            if animal in fence.animals:
                if fence.area >= animal.height * animal.width:
                    animal.health *= (1 + 1/100)
                    animal.height *= (1 + 2/100)
                    animal.width *= (1 + 2/100)
                    fence.area -= animal.height * animal.width 
                    
    
    def clean(self,fence:Fence):
        self.fence = fence
        if fence.area == 0:
            return fence.area
        cleaning_time:float = sum(animal.height * animal.width for animal in fence.animals) / fence.area 
        return cleaning_time
    
    def describe_zoo(self, zoo:Zoo):
        zoo.describe_zoo()













 


    
