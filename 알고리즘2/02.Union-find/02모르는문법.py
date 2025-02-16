# 해당 페이지에서 모르는 문법 정리


# random.shuffle(lista) : 해당 문법 사용시, lista 자체가 뒤섞여 리스트에 저장된다.
# 헷갈렸던 내용 : 새로운 리스트에 받아줄 필요 없이, 원본 리스트 자체가 뒤섞여 리스트에 저장
import random

n = 5

rand_ele = [i+1 for i in range(n*n)]
rand_element = random.shuffle(rand_ele)
index_count = 0

print(rand_ele)
print(rand_element)