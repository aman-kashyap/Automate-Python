# city population using dictionary, nested data structure


population = {'Delhi':{'Male':5000000,'female':49999923,'children':20000000},
                'Mumbai':{'Male':788000000,'female':494857999923,'children':2000329870000},
                'Kolkata':{'Male':50437686200000,'female':4324359999923,'children':20000000,'other':4859934}}


def totalPopulation(cities,item):
    numPopulation=0
    for  _, v in cities.items():        # for k,v
        numPopulation=numPopulation + v.get(item, 0)
    return numPopulation

print ("total poulation in cities: ")
print('- Male   '+ str(totalPopulation(population,'Male')))
print('- Female   '+ str(totalPopulation(population,'female')))
print('- Children   '+ str(totalPopulation(population,'children')))
print('- Others   '+ str(totalPopulation(population,'other')))
print('- Total Population   '+ str(totalPopulation(population,'Male')+totalPopulation(population,'female')+totalPopulation(population,'children')+totalPopulation(population,'other')))
