import string_utils

def run_string_utils_demo():
    print("=== 문자열 처리 모듈 실행 ===")
    
    sample_text = "  PyThOn ModuLE  "
    print(f"원본: '{sample_text}'")
    print(f"정리: '{string_utils.clean_string(sample_text)}'\n")
    
    email1 = "testqa@domain.com"
    email2 = "invalid_email.com"
    print(f"'{email1}' 유효성: {string_utils.is_valid_email(email1)}")
    print(f"'{email2}' 유효성: {string_utils.is_valid_email(email2)}\n")
    
    target_email = "mycode2026@github.com"
    print(f"원본 이메일: {target_email}")
    print(f"마스킹 이메일: {string_utils.mask_email(target_email)}\n")
    
    sentence = " Python code use for qa"
    print(f"문장: '{sentence}'")
    print(f"단어 개수: {string_utils.count_words(sentence)}개\n")
    
    original = "Python"
    print(f"원본: {original}")
    print(f"뒤집기: {string_utils.reverse_string(original)}")

if __name__ == "__main__":
    run_string_utils_demo()