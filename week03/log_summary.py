import json

def analyze_logs(filename):
    """로그 파일을 읽고 결과를 분석합니다."""
    total_count = 0
    pass_count = 0
    fail_count = 0
    failed_tests = []
    error_logs = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"오류: '{filename}' 파일을 찾을 수 없습니다.")
        return None

    for line_num, line in enumerate(lines, 1):
        cleaned_line = line.strip()
        if not cleaned_line:
            continue

        try:
            parts = cleaned_line.split(",")
            if len(parts) != 3:
                raise ValueError("데이터 필드 개수 불일치 (날짜, 테스트명, 결과 필요)")

            date = parts[0].strip()
            test_name = parts[1].strip()
            result = parts[2].strip().upper()

            if not date or not test_name:
                raise ValueError("날짜 또는 테스트명이 비어 있음")

            if result == "PASS":
                pass_count += 1
                total_count += 1
            elif result == "FAIL":
                fail_count += 1
                total_count += 1
                failed_tests.append({"date": date, "test_name": test_name})
            else:
                raise ValueError(f"알 수 없는 테스트 결과 값 ('{result}')")

        except ValueError as e:
            print(f"[경고] {line_num}번째 줄 손상된 데이터: '{cleaned_line}' (사유: {e})")
            error_logs.append({"line": line_num, "data": cleaned_line, "reason": str(e)})

    success_rate = 0.0
    if total_count > 0:
        success_rate = round((pass_count / total_count) * 100, 2)

    summary = {
        "total_tests": total_count,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "success_rate_percent": success_rate,
        "failed_tests": failed_tests,
        "error_logs": error_logs
    }
    return summary

def save_summary_json(data, output_filename):
    """분석 결과를 JSON으로 저장합니다."""
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"\n분석 결과가 '{output_filename}'에 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"저장 중 오류 발생: {e}")

def main():
    log_file = "week03/test_log.txt"
    output_file = "week03/summary.json"
    
    print("--- 자동화 테스트 로그 분석 시작 ---")
    summary = analyze_logs(log_file)

    if summary is not None:
        print("\n=== 분석 요약 ===")
        print(f"전체 테스트: {summary['total_tests']}개")
        print(f"성공(PASS): {summary['pass_count']}개")
        print(f"실패(FAIL): {summary['fail_count']}개")
        print(f"성공률: {summary['success_rate_percent']}%")
        
        if summary['failed_tests']:
            print("\n[실패한 테스트 목록]")
            for ft in summary['failed_tests']:
                print(f"- {ft['test_name']} ({ft['date']})")

        save_summary_json(summary, output_file)

if __name__ == "__main__":
    main()