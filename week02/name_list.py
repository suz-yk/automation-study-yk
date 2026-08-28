import string_utils

def clean_and_sort_names(raw_names):
    cleaned_list = []
    for name in raw_names:
        cleaned_name = string_utils.clean_string(name)
        if cleaned_name and cleaned_name not in cleaned_list:
            cleaned_list.append(cleaned_name)
            
    # 기본 반복문 및 위치 교환 정렬
    n = len(cleaned_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cleaned_list[j] > cleaned_list[j + 1]:
                cleaned_list[j], cleaned_list[j + 1] = cleaned_list[j + 1], cleaned_list[j]
                
    return cleaned_list

def main():
    raw_name_list = ["  철수 ", "영희", "  경태", "KIrt", "  JAcK"]
    print("원본 이름 목록:", raw_name_list)
    
    result = clean_and_sort_names(raw_name_list)
    print("정리된 이름 목록:", result)

if __name__ == "__main__":
    main()