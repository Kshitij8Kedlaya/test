flower = ["sunflower","rose","daffodil","orchid","dandelion"]
#print(flower[-4],flower[3],flower[1:4],flower[:3])
#print(flower[2:-1])
#print(flower[-4:-1])
#flower[3]="lotus"
#print(flower)
#for i in flower:
#    print(i)

#print(len(flower))
#print(len(flower[4]))
flower.append("lily")
flower.remove(flower[2])
flower.remove("rose")
flower.pop(2)
flower.clear()
print(flower)
