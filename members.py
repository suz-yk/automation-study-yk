# 회원 정보(이름, 나이, 지역)
members = [
    {"이름": "박인호", "나이": 27, "지역": "서울"},
    {"이름": "이영희", "나이": 36, "지역": "부산"},
    {"이름": "김철호", "나이": 47, "지역": "대구"}
]

# 전체 회원 정보 출력
print("전체 회원 정보")
for member in members:
    print("이름:", member["이름"], "/ 나이:",member["나이"],"세 / 지역:", member["지역"])

# 30세 이상 회원만  출력
print()
print("30세 이상 회원 명단")
for member in members:
    if member["나이"] >= 30:
        print("이름:", member["이름"], "/ 나이:",member["나이"],"세 / 지역:", member["지역"])