def scalar_multiply(vec, scalar):
    return [x * scalar for x in vec]

def vector_add(a, b):
    if len(a) != len(b):
        return "벡터 길이가 다릅니다."
    return [x + y for x, y in zip(a, b)]

def dot_product(a, b):
    if len(a) != len(b):
        return "벡터 길이가 다릅니다."
    return sum(x * y for x, y in zip(a, b))

def cross_product(a, b):
    if len(a) != 3 or len(b) != 3:
        return "외적은 3차원 벡터에만 정의됩니다."
    return [
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
    ]

def elementwise_multiply(a, b):
    if len(a) != len(b):
        return "벡터 길이가 다릅니다."
    return [x * y for x, y in zip(a, b)]

def vector_operation(a, b=None, op='add', scalar=None):
    try:
        if op == 'scalar':
            if scalar is None:
                return "스칼라 값이 필요합니다."
            return scalar_multiply(a, scalar)
        elif op == 'add':
            return vector_add(a, b)
        elif op == 'dot':
            return dot_product(a, b)
        elif op == 'cross':
            return cross_product(a, b)
        elif op == 'elementwise':
            return elementwise_multiply(a, b)
        else:
            return "지원하지 않는 연산입니다."
    except Exception as e:
        return f"오류 발생: {str(e)}"

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]

    print(vector_operation(a, scalar=3, op='scalar'))       # [3, 6, 9]
    print(vector_operation(a, b, op='add'))                 # [5, 7, 9]
    print(vector_operation(a, b, op='dot'))                 # 32
    print(vector_operation(a, b, op='cross'))               # [-3, 6, -3]
    print(vector_operation(a, b, op='elementwise'))         # [4, 10, 18]
    print(vector_operation(a, [1,2], op='add'))             # 벡터 길이가 다릅니다.
