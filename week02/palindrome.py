def is_palindrome(text):
    words = text.strip().lower().split()
    cleaned = "".join(words)
    return cleaned == cleaned[::-1]

def main():
    while True:
        target_text = input("회문 확인할 단어/문장을 입력: ").strip()
        
        if target_text:
            if is_palindrome(target_text):
                print(f"'{target_text}'은(는) 회문입니다.")
            else:
                print(f"'{target_text}'은(는) 회문이 아닙니다.")
            break
        else:
            print("빈 값은 입력할 수 없습니다. 다시 입력해 주세요.\n")

if __name__ == "__main__":
    main()