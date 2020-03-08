#!/usr/bin/python3
import sys

#generates 2 dictionaries:
#entries in map are formatted as follows: {Named entity: [Type, Occurence of the entity]}
#entries in typeMap are formatted as follows: {Type: occurence of the type}
def genMap(file):
    map = {}
    typeMap = {}
    for line in file:
        lineTable=line.split(' ') #isolation of couples 'Entité nommée/type'
        for word in lineTable:
            couple = word.split('/') #splitting of the couples
            if (len(couple)>1):
                #if named entity aldready exists in map, increment the occurence of the entity
                if couple[0] in map:
                    map[couple[0]] = [map.get(couple[0])[0],map.get(couple[0])[1]+1]
                else: #creation of the entry in map dictionary
                    map[couple[0]] = [couple[1],1]
                if couple[1] in typeMap: #if type aldready exists in typeMap, increment the occurence of the type
                    typeMap[couple[1]] += 1
                else: #creation of the entry in typeMap dictionary
                    typeMap[couple[1]] = 1
    return (map, typeMap)

#generates a dictionary with entries formatted as follows : {Named entity: [Type, Occurence of the NE, Proportion of the NE among same type]}
def stats(entryMap, typeMap):
    map = {}
    for EN,type in entryMap.items():
        proportion = 1/typeMap.get(type[0])
        occurence = type[1]
        map[EN] = [type[0], occurence, proportion]
    return map

def display(map):
    print("Entité nommée\t\tType\t\tNb occurences\t\tProportion dans le texte")
    for EN in map:
        print(EN + "\t\t" + map.get(EN)[0]+ "\t\t" + str(map.get(EN)[1])+ "\t\t" + str(map.get(EN)[2]))


if __name__ == "__main__":
  with open(sys.argv[1], 'r') as f:
      (map,typeMap) = genMap(f)
      table = stats(map, typeMap)
      display(table)
