def clean_string(text):
    """앞뒤 공백 제거 / 소문자로 변환"""
    return text.strip().lower()


def is_valid_email(email):
    """이메일 형태(@ 및 . 포함 여부)를 확인"""
    cleaned = clean_string(email)
    return "@" in cleaned and "." in cleaned


def mask_email(email):
    """이메일 일부 마스킹 처리"""
    if not is_valid_email(email):
        return "유효하지 않은 이메일입니다."
    
    cleaned = clean_string(email)
    user_id, domain = cleaned.split("@")
    
    if len(user_id) <= 2:
        masked_id = user_id[0] + "*"
    else:
        masked_id = user_id[:2] + "*" * (len(user_id) - 2)
        
    return f"{masked_id}@{domain}"


def count_words(sentence):
    """문장 내 단어의 개수를 계산"""
    words = sentence.strip().split()
    return len(words)


def reverse_string(text):
    """문자열 반대로 변환"""
    return text[::-1]


if __name__ == "__main__":
    print("--- string_utils 테스트 ---")
    print(clean_string("  Hello World  "))
    print(is_valid_email("user@example.com"))
    print(mask_email("python123@example.com"))
    print(count_words("Python study week two"))
    print(reverse_string("hello"))