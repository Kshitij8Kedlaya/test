dicta = {
    "Banana":"Yellow",
    "Apple" :"Red",
    "Guava" :"Green"
}

for x in dicta:
    print(f'{x} : {dicta[x]}')

for x in dicta.values():
    print(x)

for x,y in dicta.items():
    print(x,y)

print(len(dicta))

if "Guava" in dicta:
    print("Yay, Guavas")
else:
    print("No Guavas")
"""
    for i in range():
    a = input("Name of the Student:")
    b = input("Marks: ")
    if a not in B:
        marks[a]=b
    elif a == " ":
        print("Saved",end="")
    else:
        print("Value aldready Exists")
        """