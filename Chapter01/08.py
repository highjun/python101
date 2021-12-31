# 숫자와 연산자에 따라 그 결과를 반환해봅시다.
# -----------------

def print_operation_result(a, op, b):
    if op == '+':
        print(f" {a} + {b} = {a+b}")
        return a+b
    elif op == '-':
        print(f" {a} - {b} = {a-b}")
        return a-b
    elif op =='*':
        print(f" {a} * {b} = {a*b}")
        return a*b
    elif op == '/':
        print(f" {a} / {b} = {a/b}")
        return a/b

a, op, b = input("두 숫자와 연산을 입력해주세요: ").split()
a, b = int(a), int(b)
print(f"반환 결과는 {print_operation_result(a, op, b)} 입니다.")