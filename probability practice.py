import random
coin = [0, 1]
a = random.choices(coin, k=20)
print(a)
print(sum(a)/len(a))