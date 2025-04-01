from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

# 카카오톡 Web URL
KAKAOTALK_WEB_URL = 'https://accounts.kakao.com/login'

# 메시지 보내기 함수
def send_kakao_message(recipient, message):
    # WebDriver 초기화 (ChromeDriver 사용)
    driver = webdriver.Chrome()

    try:
        # 카카오톡 웹 로그인 페이지로 이동
        driver.get(KAKAOTALK_WEB_URL)

        # 로그인 처리 (카카오 계정 입력)
        print("카카오 계정 정보를 입력하세요.")
        kakao_id = "821022297094"
        kakao_pw = "sho08061"

        # ID와 비밀번호 입력
        driver.find_element(By.ID, "loginKey--1").send_keys(kakao_id)
        driver.find_element(By.ID, "password--2").send_keys(kakao_pw)
        driver.find_element(By.CLASS_NAME, "btn_g.highlight").click()

        time.sleep(5)  # 로그인 후 대기 (2단계 인증이 있는 경우 추가 처리 필요)

        # 메시지 전송 페이지로 이동 (채팅방 선택 등 로직 구현 필요)
        print(f"{recipient}님에게 메시지를 전송 중입니다.")
        # TODO: 여기에서 실제 카카오톡 대화방 이동 로직 구현
        
        # 메시지 입력 및 전송
        chat_box = driver.find_element(By.CLASS_NAME, "chat_box_class_name")  # 정확한 요소 입력
        chat_box.send_keys(message)
        chat_box.send_keys(Keys.ENTER)

    finally:
        # WebDriver 종료
        driver.quit()

# 예약 시간까지 대기
def wait_until(target_time):
    while True:
        now = datetime.now()
        if now.hour == target_time.hour and now.minute == target_time.minute:
            break
        time.sleep(1)

# 실행 예제
if __name__ == "__main__":
    recipient_name = "신현우"
    message_content = "멋진헛간 \n월 6-8\n 월 8-10\n 수 8-10"
    target_time = datetime.now().replace(hour=23, minute=44, second=0, microsecond=0)

    print(f"{target_time.strftime('%H:%M')}에 메시지를 전송합니다.")
    wait_until(target_time)
    send_kakao_message(recipient_name, message_content)
