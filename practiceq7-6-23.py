marks = {
}
a = " "
while a != "":
    a = input("Name of the Student:")
    if a == "":
        break
    b = input("Marks: ")



for x in marks:
    print(f'{x} : {marks[x]}')


"""
while True:
    a = input("Name of the Student:")
    b = input("Marks: ")
    if a not in marks:
        marks[a]=b
    elif a == "":
        break
    else:
        print("Value aldready Exists")   

 """
        
    




