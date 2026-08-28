def print_9x9(dan):
    print(f"\n--- {dan}단 ---")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")

def main():
    while True:
        user_input = input("출력할 구구단 숫자를 입력 (1~9): ").strip()
        
        # 1. 숫자 여부 및 범위(1~9) 검사
        is_valid = True
        if not user_input or len(user_input) != 1:
            is_valid = False
        else:
            # 학습 범위 내의 한 글자 범위 비교 ("1" ~ "9")
            if not ("1" <= user_input <= "9"):
                is_valid = False
                    
        # 2. 결과 처리
        if is_valid:
            dan = int(user_input)
            print_9x9(dan)
            break
        else:
            print("잘못된 입력입니다. 1부터 9 사이의 숫자만 입력해 주세요.\n")

if __name__ == "__main__":
    main()