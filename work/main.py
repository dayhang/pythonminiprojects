from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 웹 드라이버 초기화
driver = webdriver.Chrome()

# 웹사이트 열기
url = "https://www.naver.com"
driver.get(url)

# 로그인 정보 입력
wait = WebDriverWait(driver, 10)

username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#id")))
password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button")))

username_input.send_keys("user")
password_input.send_keys("1234")
login_button.click()

# 로그인 후 작업 수행
# 여기에 로그인 후 수행할 작업을 추가하면 됩니다.

# 작업이 완료되면 브라우저 종료
