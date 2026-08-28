def main():
    data_list = []
    
    while True:
        print("\n=== 데이터 관리 프로그램 ===")
        print("1. 데이터 추가")
        print("2. 데이터 조회")
        print("3. 프로그램 종료")
        
        choice = input("원하는 메뉴 번호를 선택하세요 (1-3): ").strip()
        
        if choice == "1":
            while True:
                new_item = input("추가할 데이터를 입력하세요: ").strip()
                if new_item:
                    data_list.append(new_item)
                    print(f"'{new_item}' 데이터가 추가되었습니다.")
                    break
                else:
                    print("빈 값은 추가할 수 없습니다. 다시 입력해 주세요.")
                
        elif choice == "2":
            print("\n--- 현재 데이터 목록 ---")
            if not data_list:
                print("저장된 데이터가 없습니다.")
            else:
                num = 1
                for item in data_list:
                    print(f"{num}. {item}")
                    num += 1
                    
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
            
        else:
            print("잘못된 메뉴 번호입니다. 1, 2, 3 중에서 다시 선택해 주세요.")

if __name__ == "__main__":
    main()