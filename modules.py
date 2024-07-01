import random


random_num = random.random()
print("Random float:", random_num)

random_int=random.randint(1,100)
print("random integer:",random_int)


list=["deepika","lali","megha","sindhu"]
random_choice = random.choice(list)
print("Random choice:", random_choice)

random.shuffle(list)
print("suffle list:",list)

random_sample=random.sample(list,2)

print(random_sample)