# 이번 글에서는 동아일보와 한겨레신문에서 특정 키워드를 포함하는 기사를 긁어오기 전 예제로 
# http://cleanair.seoul.go.kr/main.htm : 기상청 미세먼지 사이트

from bs4 import BeautifulSoup # urllib을 통해 받은 RESPONSE(HTML)를 파싱하기 위한 Beautiful Soup
import urllib.request # HTTP REQUEST를 보내고 HTTP RESPONSE를 받기 위한 urllib
import re
import string
import time
# cmd 창 : pip install bs4
# cmd 창 : pip install lxml


# 출력 파일 명 상수로 할당
OUTPUT_FILE_NAME = r'C:\Users\JB\Desktop\Crawling\output.txt' # 기사내용을 긁어와 저장할 파일명
# 경로 앞에 r을 붙이지 않으면 unicodeescape error가 발생한다.

# 긁어 올 URL 주소 상수로 할당
URL = 'http://cleanair.seoul.go.kr/main.htm'
 
 
# 크롤링 함수 : 해당 URL주소로 요청을 보내고 받아 기사 내용을 파싱해 하나의 문자열로 저장하는 함수
def get_text(URL):
    # urlopen메소드를 통해 URL주소에 대한 요청을 보내 source_code_from_URL 변수에 그 결과를 저장
    source_code_from_URL = urllib.request.urlopen(URL)
    
    # HTML코드를 파싱하기 위해 16번째 줄에서 source_code_from_URL을 이용, BeautifulSoup객체를 생성해 soup에 할당
    # BeautifulSoup객체 생성자의 2번째 인자로 'lxml'을 사용해 기존 'html'방식 대신 'lxml'방식으로 파싱을 했고, 
    # 한글 내용이 포함된 기사이기 때문에 from_encoding 키워드 인자로 'utf-8'을 넣어 'UTF-8'방식으로 인코딩
    # soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8') => 라즈에서 lxml 설치가 안되서 위 코드로 대체
    soup = BeautifulSoup(source_code_from_URL, 'html', from_encoding='utf-8')

    text = '' # 본문 내용을 저장하기 위해 text에 빈 문자열을 할당
    
    # soup객체의 find_all 메소드를 이용해 id가 'articleBodyContents'인 'div'클래스를 모두 뽑아내고
    # for문을 통해 뽑힌 요소 하나하나에 다시 한번 직접 접근
    
    for item in soup.find_all('script', type="text/javascript"):
        # for문으로 뽑혀진 각 요소 item에 find_all 메소드를 사용, text 키워드 인자에 True를 
        # 넣어 텍스트 요소만 뽑아 문자열로 치환한 후, text 문자열에 이어 붙였습니다. 
        text = text + str(item.find_all(text=True))
        
    # for문은 들여쓰기로 끝남을 표기.
    # text_new = text.strip()
    text_list = text.split(";")
    # 세미콜론으르 기준으로 문자열을 split하여 list로 만들기

    # matching = [s for s in text_list if "종로구" in s]
    # print(matching)  
    
    # areaList[idx][1] = '종로구';
    # areaList[idx][2] = '111123';
    # areaList[idx][3] = chgText('111');
    # areaList[idx][8] = chgText('68'); => 우리가 원하는 미세먼지 농도

    index_dust = text_list.index("\\r\\n      areaList[idx][1] = \\'성북구\\'") + 3
    # areaList[idx][8] = chgText('68') 추출
    text_dust = text_list[index_dust].split()
    text_dust_value = text_dust[3]
    # 공백을 기준으로 다시 한번 추출한 값을 split하여 chgText('68') 만 추출
    index_start = text_dust_value.index("(") + 3
    index_final = len(text_dust_value) - 3
    # 수치만 추출할 index값 찾기.
    # print(text_dust_value[index_start:index_final])
    dust_value = text_dust_value[index_start:index_final]

    # 추출 기준 시간 뽑기
    index_time = text_list.index("\\r\\n      areaList[idx][1] = \\'성북구\\'") - 1
    text_time = text_list[index_time].split()
    text_time_value = text_time[3]

    index_start = 2
    index_final = len(text_time_value) - 2
    time_value = text_time_value[index_start:index_final]
    #for i in range(0,12) :
    #    print(i)
    #    print(time_value[i])
    year = ' '
    for i in range(0,4) : # 0부터 3 까지
        year = year + time_value[i]
    
    month = time_value[4] + time_value[5]
    date = time_value[6] + time_value[7]
    hour = time_value[8] + time_value[9]
    minute = time_value[10] + time_value[11]
    
    print("성북구의 "+year+"년 "+month+"월 "+date+"일 "+hour+"시 "+minute+"분 기준 미세먼지 농도 ="+dust_value+"㎍/㎥")

    return text # text를 반환
    
 
# 메인 함수 : 메인 함수를 별도로 만들고 __name__을 이용해 main함수를 실행시켰습니다.
def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w')
    # result_text = get_text(URL) => 주기적으로 값을 보여주기 위해 while문 안에 넣기.
    while True:
        result_text = get_text(URL)
        time.sleep(5)
    open_output_file.write(result_text)
    open_output_file.close()

# OUTPUT_FILE_NAME상수를 통해 txt파일을 생성하고, get_text함수를 사용해 기사내용을 result_text에 할당했습니다. 
# 이 후, 오픈한 output_file에 기사를 쓰고 닫았습니다
    
 
if __name__ == '__main__':
    main()
