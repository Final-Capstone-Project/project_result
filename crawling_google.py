# created by : keun young
# 구글에서 이미지 긁어오기

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
import os

base_dir_img = './data/train'  # 저장을 위한 기본 주소
targets = ['화재', '화재연기', '불']  # 검색을 위한 키워드

for target in targets:
    # 폴더 경로 및 생성
    img_path = base_dir_img + '/' + str(target)
    if os.path.exists(img_path):
        # shutil.rmtree(csv_path)
        # os.makedirs(csv_path)
        pass
    else:
        os.makedirs(img_path)

    # 검색 URL
    url = 'https://www.google.com/search?q=' + str(target)
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    # 주소로 이동
    driver.get(url)
    time.sleep(2)
    # 이미지 클릭
    driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()
    time.sleep(2)

    SCROLL_PAUSE_SEC = 1
    # 스크롤 높이 가져옴
    last_height = driver.execute_script("return document.body.scrollHeight")
    for x in range(15):
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 1초 대기
        time.sleep(SCROLL_PAUSE_SEC)
        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            except:
                break
            # break
        last_height = new_height

    rcv_data = driver.page_source  # 검색한 웹페이지 소스코드 긁어오기
    soupData = BeautifulSoup(rcv_data, 'html.parser')  # html이라는 부분 데이터를 가져옴
    datas = soupData.find('div', {'id': 'islmp'})  # 긁어오고자 하는 데이터들이 담긴 div~ 데이터들

    try:
        # 이미지 저장하기
        # 사진이 담겨있는 태그데이터를 긁어오기
        img_datas = datas.find('div', {'id': 'islrg'})
        img_datas = img_datas.findall('img', {'class': 'rg_i Q4LuWd'})
        # print(img_data)
        for i, img_data in enumerate(img_data):
            img_url = img_data.get('src')
            if img_url[:2] == '//':
                img_url = 'https:' + img_url
            urllib.request.urlretrieve(img_url, img_path + '/' + str(target) + '_' + str(i) + '.jpg')  # 폴더에 사진 저장
    except:
        pass

    driver.close()
