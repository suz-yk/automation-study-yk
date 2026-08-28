def get_word_frequencies(text):
    words = text.lower().strip().split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

def main():
    while True:
        sentence = input("분석할 문장 입력: ").strip()
        
        if sentence:
            result = get_word_frequencies(sentence)
            print("\n--- 단어 빈도 결과 ---")
            for word in result:
                print(f"'{word}': {result[word]}회")
            break
        else:
            print("문장을 입력하지 않았습니다. 다시 입력해 주세요.\n")

if __name__ == "__main__":
    main()