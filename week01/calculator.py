# 숫자 입력
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 더하기, 빼기, 곱하기 출력
print("더하기:", num1 + num2)
print("빼기:", num1 - num2)
print("곱하기:", num1 * num2)

# 0 나누기 예외 처리
if num2 == 0:
    print("나누기: 0 나누기 불가")
else:
    print("나누기:", num1 / num2)