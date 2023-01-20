import itertools


size = (100,200)

cities = []

a = ['a', 'b', 'c']
b = [1 , 2 , 3] 

print("##############################################")
# this section is for finding the routes between all the cities 

combinations = itertools.combinations(b, 2)
print(list(combinations))

print("##############################################")

for a_combination in itertools.combinations(a,2):
    print(a_combination)

print("##############################################")
import random
print( random.randint(1,100) )

print("##############################################")

print("Random Cities and their coordinates: ")
for i in range(4, 15):
     y = random.randrange(100)
     x = random.randrange(100)
     print(x,y)
