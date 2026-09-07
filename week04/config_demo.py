import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

def get_env_variable(key, is_required=True, default_value=None):
    """환경변수를 안전하게 읽어오는 함수"""
    value = os.getenv(key, default_value)
    
    if is_required and not value:
        raise ValueError(f"필수 환경변수 '{key}'가 설정되지 않았습니다. .env 파일을 확인해 주세요.")
    
    return value

def mask_password(password):
    """비밀번호 마스킹 처리"""
    if not password:
        return ""
    if len(password) <= 2:
        return "*" * len(password)
    return password[0] + "*" * (len(password) - 2) + password[-1]

def main():
    print("=== 4주차 환경설정 테스트 ===")
    
    try:
        # 필수 환경변수 읽기
        login_id = get_env_variable("LOGIN_ID", is_required=True)
        login_password = get_env_variable("LOGIN_PASSWORD", is_required=True)
        
        # 선택 환경변수 (기본값 처리)
        base_url = get_env_variable("BASE_URL", is_required=False, default_value="https://default-service.com")
        
        print("\n[환경변수 로드 성공]")
        print(f"- 접속 URL: {base_url}")
        print(f"- 아이디: {login_id}")
        print(f"- 비밀번호: {mask_password(login_password)} (보안 마스킹 완료)")

    except ValueError as e:
        print(f"\n[설정 오류 발생] {e}")

if __name__ == "__main__":
    main()