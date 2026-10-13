from playwright.sync_api import Page, expect

URL = "https://v369.dev.l-walk.com"

# 1) 스토어 페이지 타이틀 검사
def test_스토어_페이지_타이틀(page: Page):
    page.goto(URL)
    page.get_by_role("link", name="스토어").click()
    expect(page).to_have_title("소프트웨어 테스팅 라이프 사이클")

# 2) 버튼 확인 ("프로젝트 등록" 버튼)
def test_프로젝트_등록_버튼(page: Page):
    page.goto(URL)
    expect(page.get_by_role("button", name="프로젝트 등록")).to_be_visible()

# 3) 화면 이동 확인
def test_스토어_페이지로_이동(page: Page):
    page.goto(URL)
    page.get_by_role("link", name="스토어").click()
    # 스토어 주소인 /solution으로 이동했는지 검증
    expect(page).to_have_url(f"{URL}/solution")

# 4) 실패케이스 ("QMeet 홈화면" 의도적 오류) > 정상으로 변경
def test_실패_케이스_QMeet_홈_확인(page: Page):
    page.goto("https://dev.l-walk.com")
    expect(page.get_by_role("link", name="QMeet 홈")).to_be_visible()