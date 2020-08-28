import requests
from bs4 import BeautifulSoup
import csv
import pprint

# CSS 셀렉터로 찾기
BASE_URL = 'http://www.pythonscraping.com'
BASE_URL = 'http://example.webscraping.com'


def create_list_from_table(table_tag):
    # CSV 파일로 만들기 위해서 2중 리스트 생성
    gifts = []

    # 레더에 해당하는 1번째 로우 작성
    headers = []
    headers_tag = table_tag.find('tr')  # 첫번재 tr 반환
    for th_tag in headers_tag.find_all('th'):
        headers.append(th_tag.text.strip())

    gifts.append(headers)

    # 선물 레코드 작성
    for tr_tag in table_tag.find_all('tr'):
        gift = []
        for td_tag in tr_tag.find_all('td'):
            if td_tag.text.strip() != '':
                # 좌우 공백을 제거하고 텍스트 속게 \n문자를 공백으로 변경
                gift.append(td_tag.text.strip().replace('\n', ' '))
            else:
                gift.append(BASE_URL + td_tag.find('img').get('src')[2:])

        if not gift:
            continue

        gifts.append(gift)

    return gifts


def create_csv_file(lol, filename):
    with open(filename, 'w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file)
        for line in lol:
            writer.writerow(line)


def main():
    res = requests.get(BASE_URL + '/pages/page3.html')
    soup = BeautifulSoup(res.text, 'lxml')

    # 테이블 테그 확보
    table_tag = soup.find(id='giftList')

    gifts = create_list_from_table(table_tag)
    create_csv_file(gifts, 'L21_gifts.csv')

    print('job completed..')


if __name__ == '__main__':
    main()
