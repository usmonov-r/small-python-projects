from game_data import data
import random


num = random.randint(1,5)

#getting value throught calling dict key name
ran_data = data[num]["name"]
# print(ran_data)

names = {}

for n in  range(3):
    multimle_data = data[n]['name']
    names[f"{n}"] = multimle_data
    print(multimle_data)
print(names)

