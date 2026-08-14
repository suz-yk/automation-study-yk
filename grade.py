# 5명 점수
scores = [98, 83, 74, 67, 90]

#점수별 등급
print("학생별 등급")
for score in scores:
    if score >= 90:
        print(score, "점 -> A등급")
    elif score >= 80:
        print(score, "점 -> B등급")
    elif score >= 70:
        print(score, "점 -> C등급")
    else:
        print(score, "점 -> D등급")

# 평균, 최고점, 최저점
average = sum(scores) / len(scores)
max_score = max(scores)
min_score = min(scores)

print("\n전체 결과")
print("전체 평균:", average)
print("최고점:", max_score)
print("최저점:", min_score)