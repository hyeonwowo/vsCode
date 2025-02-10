# 9. 스택을 활용한 중위 -> 후위 변환 (Shunting Yard 알고리즘)
# 문제: 중위 표기법의 수식을 후위 표기법(Reverse Polish Notation)으로 변환하는 함수 infix_to_postfix(expression)을 구현하세요.

# 입력 예시 : print(infix_to_postfix("3 + 5 * ( 2 - 8 )"))

# 출력 예시 : "3 5 2 8 - * +"

# 숫자 조우시 스택에 push
# 기호 조우시 pop(), pop() -> 연산 -> 해당 결과 다시 push()
def evaluate_postfix(expression):
    """후위 표기법을 계산하는 함수"""
    stack = []

    for char in expression.split():
        if char.isdigit():  # 숫자라면 스택에 push
            stack.append(int(char))
        else:  # 연산자라면 pop() 두 번 후 연산 결과를 다시 push
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)  # 나눗셈 결과는 실수형(float)

    return stack.pop()  # 최종 결과 반환


def infix_to_postfix(expression):
    """중위 표기법을 후위 표기법으로 변환하는 함수 (Shunting Yard 알고리즘)"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}  # 연산자 우선순위 - 높은게 더 큰 우선순위를 갖는다.
    stack = []
    output = []

    for char in expression.split():
        if char.isdigit():  # 숫자는 output에 추가
            output.append(char)

        elif char in precedence:  # 연산자라면
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[char]:
                output.append(stack.pop())  # 스택에서 pop 후 output에 추가
            stack.append(char)  # 현재 연산자를 스택에 push

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # '(' 제거

    while stack:
        output.append(stack.pop())  # 남아 있는 연산자 모두 pop 후 output에 추가

    return " ".join(output)  # 리스트를 문자열로 변환


if __name__ == "__main__":
    # 후위 표기법 계산 (Postfix Evaluation)
    expression_postfix = "3 4 + 2 * 7 /"
    print(evaluate_postfix(expression_postfix))  # 결과 : 2.0

    # 중위 표기법 → 후위 표기법 변환 (Infix to Postfix)
    expression_infix = "3 + 5 * ( 2 - 8 )"
    print(infix_to_postfix(expression_infix))  # 결과 : "3 5 2 8 - * +"
