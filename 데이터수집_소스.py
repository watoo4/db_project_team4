# 사용전 필수 패키지들입니다
# pip install selenium // cmd 창에서 입력
# pip install pandas // cmd 창에서 입력
# https://chromedriver.chromium.org/downloads  // 자신의 크롬 버전과 맞는 드라이버 다운 후 소스파일과 같은 디렉터리 안에 exe 파일을 저장해주세요
# 크롬 버전은 우측 상단의 점 3개 -> 도움말 -> chrome 정보에서 확인 가능합니다

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
result =[]
store_id=0
try:
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_experimental_option('excludeSwitches',['enable-logging'])
    wd = webdriver.Chrome('./chromedriver.exe',options=op)
    typelist =['한식','중식','일식','양식','분식']
    for food_type in typelist:
        wd.get('https://www.google.com/webhp?hl=ko&sa=X&ved=0ahUKEwjLr7Dl9dz3AhW1g1YBHeZLDxIQPAgI')
        wd.implicitly_wait(10)
        search=wd.find_element_by_class_name('gLFyf.gsfi')
        search.send_keys('충주식당 %s'%food_type)
        search.send_keys(Keys.RETURN)
        wd.implicitly_wait(10)
        wd.find_element_by_class_name('wUrVib.OSrXXb').click()
        wd.implicitly_wait(10)
        for page in range(1,6):
            storelist=wd.find_elements_by_class_name('rllt__details')
            for store in storelist:
                store.click()
                time.sleep(1)
                try:
                    store_name =wd.find_element_by_class_name('SPZz6b').find_element_by_tag_name('div>h2>span').text
                except:continue
                try:
                    wd.find_element_by_class_name('BTP3Ac').click()
                    store_hour =wd.find_element_by_class_name('K7Ltle').find_elements_by_tag_name('tr>td')[1].text
                except:store_hour = '정보 없음'
                try:
                    store_address=wd.find_element_by_class_name('LrzXr').text
                except:store_address='정보 없음'
                try:
                    store_phone_num = wd.find_element_by_class_name('LrzXr.zdqRlf.kno-fv').find_element_by_tag_name('span>a>span').text
                except:store_phone_num = '정보 없음'
                result.append([store_id]+[store_name]+[store_hour]+[store_address]+[store_phone_num]+[food_type])
                store_id+=1
            wd.find_elements_by_class_name('fl')[page].click()
            time.sleep(3)
except:pass
table=pd.DataFrame(result,columns=('식당ID','식당명','영업시간','주소','전화번호','종류'))
table.to_csv('./DB_restaurant_info.csv',mode='w',encoding='utf-8-sig',index=False)