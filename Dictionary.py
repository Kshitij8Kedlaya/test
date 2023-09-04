dicta = {
    "Banana":"Yellow",
    "Apple" :"Red",
    "Guava" :"Green"
}
print(dicta["Banana"])

dicta["Apple"] = "Green"
print(dicta["Apple"])

dicta["Rose"]="Pink"
print(dicta)

del dicta["Apple"]
print(dicta)

for x in dicta:
    print(x)

dicta.pop("Banana")
dicta.popitem()
print(dicta)

dictb = dicta.copy
dictc = dict(dicta)
print(dictb)
print(dictc)
