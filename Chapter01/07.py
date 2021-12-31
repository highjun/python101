# 주어진 숫자 2개의 사칙연산 결과를 모두 출력해주는 함수를 만들어봅시다.
# --------------

def print_operation_result(a,b):
    print(f"합은 {a+b}입니다.")
    print(f"곱은 {a*b}입니다.")
    print(f"차은 {a-b}입니다.")
    print(f"나누면 {a/b}입니다.")

a, b = input("두 숫자를 입력해주세요: ").split()
a, b = int(a), int(b)
print_operation_result(a,b)