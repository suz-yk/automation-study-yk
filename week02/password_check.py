def check_password_strength(password):
    min_length = 8
    
    if len(password) < min_length:
        return False, f"비밀번호는 최소 {min_length}자 이상이어야 합니다."
    
    has_digit = False
    has_alpha = False
    
    for char in password:
        if "0" <= char <= "9":
            has_digit = True
        
        lower_char = char.lower()
        if "a" <= lower_char <= "z":
            has_alpha = True
            
    if not has_digit:
        return False, "비밀번호에 숫자가 최소 1개 이상 포함되어야 합니다."
    if not has_alpha:
        return False, "비밀번호에 영문자가 최소 1개 이상 포함되어야 합니다."
        
    return True, "유효한 비밀번호입니다."

def main():
    while True:
        user_pw = input("비밀번호를 입력하세요: ").strip()
        is_valid, message = check_password_strength(user_pw)
        
        if is_valid:
            print(f"성공: {message}")
            break
        else:
            print(f"실패: {message} 다시 입력해 주세요.\n")

if __name__ == "__main__":
    main()