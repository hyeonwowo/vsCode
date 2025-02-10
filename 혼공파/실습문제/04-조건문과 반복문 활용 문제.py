# 4. 조건문과 반복문을 활용한 문제
# 문제:

# n개의 숫자를 입력받아 짝수만 출력하는 함수 print_even_numbers(n)을 작성하세요.
# 1부터 n까지의 숫자 중 3과 5의 공배수는 "FizzBuzz", 3의 배수는 "Fizz", 5의 배수는 "Buzz"를 출력하는 fizz_buzz(n)을 작성하세요.

def print_even_numbers(n):
    listA = []
    for i in range(n):
        num = int(input("type num >> "))
        if num%2 == 0:
            listA.append(num)
    print(listA)
        
def fizz_buzz(n):
    
    for i in range(1,n+1):
        if i%3 == 0 and i%5 != 0:
            print(i,": 3의 배수")
        elif i%3 !=0 and i%5 == 0:
            print(i,": 5의 배수")
        elif i%3 == 0 and i%5 == 0:
            print(i, ": 3, 5, 15의 배수")
        else:
            print(i, ": -")

if __name__=="__main__":
    #print_even_numbers(10)
    fizz_buzz(15)