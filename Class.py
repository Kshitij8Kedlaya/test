class animal:
    name = "Dog"
    def __init__(self,color,breed):
        self.color=color
        self.breed=breed
    
    def values(self):
        print("I have a",self.name)
        print("Color:",self.color)
        print("Breed:",self.breed)

Rodger = animal("Brown","Afghan Hound")
Lodger = animal("White","Golden Retriever")
Dodger = animal("Black","Alaskan Husky")

Rodger.values()
Lodger.values()
Dodger.values()
