# 사용자가 =를 입력할 때까지 숫자를 더하는 프로그램을 만들어봅시다.
# 사용자의 입력: 1\n 2\n 3\n 4\n \n
# 출력: 합은 10입니다.
# ------------------

total = 0
num = input("숫자를 입력해주세요: ")
while num!="=":
    total += int(num)
    num = input("숫자를 입력해주세요: ")
print(f"합은 {total}입니다.")
