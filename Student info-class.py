class info:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age
    
    def values(self):
        print("Student Name:",self.name)
        print("Grade:",self.grade)
        print("Age:",self.age)

Road = info("Rohit",8,13)
Toad = info("Tanmay",10,15)
Load = info("Sara",9,14)

Road.values()
Toad.values()
Load.values()