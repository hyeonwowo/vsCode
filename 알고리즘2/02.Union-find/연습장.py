import random

n = 5

rand_ele = [i+1 for i in range(n*n)]
rand_element = random.shuffle(rand_ele)
index_count = 0

print(rand_ele)
print(rand_element)