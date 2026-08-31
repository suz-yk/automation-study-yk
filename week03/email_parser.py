import json

def read_emails_from_file(filename):
    """파일을 읽은 후 리스트로 반환"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            cleaned_lines = []
            for line in lines:
                cleaned_lines.append(line.strip())
            return cleaned_lines
    except FileNotFoundError:
        print(f"오류: '{filename}' 파일을 찾을 수 없습니다.")
        return []

def parse_emails(email_list):
    """이메일을 검증 및 도메인별 개수 분석"""
    valid_emails = []
    invalid_emails = []
    domain_counts = {}

    for item in email_list:
        if not item:
            continue
            
        try:
            # 이메일 기본 유효성 검사 (@ 및 . 포함 여부 및 split)
            if "@" not in item or "." not in item:
                raise ValueError("유효하지 않은 이메일 형식")
                
            parts = item.split("@")
            if len(parts) != 2 or not parts[0] or not parts[1]:
                raise ValueError("유효하지 않은 이메일 구조")
                
            user_id = parts[0]
            domain = parts[1]
            
            if "." not in domain:
                raise ValueError("도메인에 점(.) 부재")

            valid_emails.append({"email": item, "id": user_id, "domain": domain})
            
            if domain in domain_counts:
                domain_counts[domain] += 1
            else:
                domain_counts[domain] = 1

        except ValueError as e:
            invalid_emails.append({"data": item, "reason": str(e)})

    return valid_emails, invalid_emails, domain_counts

def save_to_json(data, filename):
    """분석 결과를 JSON 파일로 저장"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"성공적으로 '{filename}'에 저장되었습니다.")
    except Exception as e:
        print(f"JSON 저장 중 오류 발생: {e}")

def main():
    input_file = "week03/emails.txt"
    output_file = "week03/parsed_emails.json"
    
    raw_emails = read_emails_from_file(input_file)
    if not raw_emails:
        print("분석할 이메일 데이터가 없습니다.")
        return

    valid, invalid, counts = parse_emails(raw_emails)
    
    result = {
        "total_count": len(raw_emails),
        "valid_count": len(valid),
        "invalid_count": len(invalid),
        "domain_counts": counts,
        "valid_emails": valid,
        "invalid_emails": invalid
    }
    
    save_to_json(result, output_file)

if __name__ == "__main__":
    main()