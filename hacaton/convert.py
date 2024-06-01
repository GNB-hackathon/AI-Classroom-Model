from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib import request
from selenium.common import NoSuchElementException
import time
import os

browser_url = r'https://2605d617a5427ae92c.gradio.live/'

def convert_file(url, model_name, path, file_name, save_name ):
    #브라우저 꺼지는거 방지
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    #브라우저 크기
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    #잠시 대기
    driver.implicitly_wait(3)
    time.sleep(3)

    #새로 고침해야하는데, 브라우저가 초기화 될 때까지 잠시 기다려야 하니까,
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="component-8"]').click()
            print("변환 가동")
            break
        except NoSuchElementException:
            print("대기중....")
            continue

    driver.find_element(By.XPATH, '//*[@id="component-8"]').click()
    time.sleep(3)

    #모델이름을 쓰는 element 클릭
    driver.find_element(By.XPATH,'//*[@id="component-7"]/label/div/div[1]/div/input').click()

    #model_name 입력
    driver.find_element(By.XPATH,'//*[@id="component-7"]/label/div/div[1]/div/input').send_keys(model_name)
    driver.find_element(By.XPATH,'//*[@id="component-7"]/label/div/div[1]/div/input').send_keys(Keys.ENTER)

    #파일 변환하기 위해서 경로 설정
    change_file = path + '\\' + file_name

    #변환 하고 싶은 파일 넣기
    driver.find_element(By.XPATH, '//*[@id="component-16"]/div[3]/input').send_keys (change_file)

    #모델이 업로드 될 때가지 대기
    while True:
        try:
            c = driver.find_element(By.XPATH, '//*[@id="component-16"]/div[4]/table/tbody/tr/td[3]/a' )
            print('모델 업로드 성공')
            break
        except NoSuchElementException:
            time.sleep(10)
            print("모델 업로드중.....")
            continue

    #이건 새로고침. 파일 새로운거 들어온거 확인하는
    driver.find_element(By.XPATH,'//*[@id="component-21"]').click()

    #파일 업로드 하기위해서
    upload_file = './' + 'audios' + '/' + file_name


    print(file_name)
    driver.find_element(By.XPATH, '//*[@id="component-21"]').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="component-21"]').click()

    #파일 이름 넣기
    driver.find_element(By.XPATH,'//*[@id="component-20"]/label/div/div[1]/div/input').send_keys(upload_file)
    driver.find_element(By.XPATH,'//*[@id="component-20"]/label/div/div[1]/div/input').send_keys(Keys.ENTER)

    #convert 버튼 누르기
    driver.find_element(By.XPATH,'//*[@id="component-11"]').click()

    #convert가 다 될때까지 대기
    while True:
        try:
            c = driver.find_element(By.XPATH, '//*[@id="component-48"]/audio' )
            print('convert 완료')
            break
        except NoSuchElementException:
            time.sleep(10)
            print("converting......")
            continue

    #다운 받을 링크들을 가져오고
    element = driver.find_element(By.XPATH, '//*[@id="component-48"]/audio')
    src = element.get_attribute("src")
    print("이미지 URL:", src)

    request.urlretrieve(src,save_name)
    print("저장되었습니다.")

    driver.find_element(By.XPATH, '//*[@id="component-16"]/div[3]/button/div')
    print("올린 파일 다시 없애봄")


path = r'C:\Users\user\PycharmProjects\hacaton\cut_file'

files = os.listdir(r'C:\Users\user\PycharmProjects\hacaton\cut_file')

for i,file in enumerate(files):
    save_name = '.\\' + 'output' + '\\' + "test" + str(i) + ".mp3"
    convert_file('https://bd8d36553ad6aacfa1.gradio.live/', 'a.pth', path, file, save_name)


waiting = input("잠시만 대기 해봐")