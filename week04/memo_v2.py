import json
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경변수에서 저장 위치를 가져오되, 없을 경우 기본값("week04/memos.json") 사용
FILENAME = os.getenv("MEMO_FILE_PATH", "week04/memos.json")

def load_memos():
    """memos.json 파일에서 메모 목록을 불러옵니다."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[{FILENAME}] 파일이 없어 새로 생성합니다.")
        return []
    except json.JSONDecodeError:
        print(f"경고: [{FILENAME}] 저장 파일의 JSON 형식이 올바르지 않아 초기화합니다.")
        return []

def save_memos(memos):
    """메모 목록을 JSON 파일에 저장합니다."""
    try:
        # 파일이 저장될 폴더 경로가 없으면 생성
        folder_path = os.path.dirname(FILENAME)
        if folder_path and not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)

        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(memos, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"메모 저장 중 오류 발생: {e}")

def add_memo(memos):
    """새 메모를 작성하여 추가합니다."""
    while True:
        content = input("등록할 메모 내용을 입력하세요: ").strip()
        if content:
            break
        print("빈 메모는 등록할 수 없습니다. 다시 입력해 주세요.\n")

    while True:
        date_str = input("작성일을 입력하세요 (예: 2026-09-01): ").strip()
        if date_str:
            break
        print("작성일은 필수 입력 항목입니다. 다시 입력해 주세요.\n")

    next_id = 1
    if memos:
        max_id = max(m.get("id", 0) for m in memos)
        next_id = max_id + 1

    new_memo = {
        "id": next_id,
        "content": content,
        "date": date_str
    }
    memos.append(new_memo)
    save_memos(memos)
    print(f"메모(ID: {next_id})가 성공적으로 저장되었습니다. (저장 경로: {FILENAME})")

def view_all_memos(memos):
    """전체 메모 목록을 조회합니다."""
    print("\n--- 전체 메모 목록 ---")
    if not memos:
        print("등록된 메모가 없습니다.")
        return

    for m in memos:
        print(f"[{m['id']}] {m['content']} (작성일: {m['date']})")

def search_memo(memos):
    """키워드로 메모를 검색합니다."""
    if not memos:
        print("\n검색할 메모가 없습니다.")
        return

    while True:
        keyword = input("검색할 단어를 입력하세요: ").strip().lower()
        if keyword:
            break
        print("검색어를 입력해 주세요.\n")

    found_list = [m for m in memos if keyword in m["content"].lower()]

    print(f"\n--- '{keyword}' 검색 결과 ---")
    if not found_list:
        print("검색 결과가 없습니다.")
    else:
        for m in found_list:
            print(f"[{m['id']}] {m['content']} (작성일: {m['date']})")

def main():
    print(f"현재 설정된 메모 저장 파일: {FILENAME}")
    memos = load_memos()

    while True:
        print("\n=== 메모 관리 프로그램 v2 ===")
        print("1. 메모 추가")
        print("2. 전체 메모 조회")
        print("3. 메모 검색")
        print("4. 프로그램 종료")
        
        choice = input("메뉴를 선택하세요 (1-4): ").strip()

        if choice == "1":
            add_memo(memos)
        elif choice == "2":
            view_all_memos(memos)
        elif choice == "3":
            search_memo(memos)
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 1~4 사이의 숫자를 다시 입력해 주세요.")

if __name__ == "__main__":
    main()