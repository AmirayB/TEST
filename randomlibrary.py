import random
print(round(random.random()* 10))
print(random.randint(10,20))
print(random.seed(5))
print(random.randint(10,20))
print(random.randint(10,20))
#choice
print(random.choice(["salam","necesen","yaxsiyam",]))
print(random.choice(["salam","necesen","yaxsiyam",]))
#shuffle list qaytarir
lst=[1,2,3,4,5,6]
random.shuffle(lst)
print(lst)