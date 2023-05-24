from selenium import webdriver

# 크롬 웹드라이버 경로 설정
driver_path = 'chromedriver'

def click_id_search():
    # WebDriver 초기화
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    # 네이버 웹사이트 열기
    driver.get("https://www.naver.com")

    # '아이디 찾기' 버튼 요소 찾기
    id_search_button = driver.find_element("css selector", ".MyView-module__link_more___sbxGh")

    # '아이디 찾기' 버튼 클릭
    id_search_button.click()

# '아이디 찾기' 버튼 클릭하여 페이지로 이동
click_id_search()
