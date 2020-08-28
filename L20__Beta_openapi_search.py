import re
import requests
import pprint


def get_naver_news(keyword):
    headers = {
        'X-Naver-Client-Id': '5KofzjFZbfMZ9O5SJVQB',
        'X-Naver-Client-Secret': 'FeO3Bap6aT',
        'sotr': 'date'
    }

    payload = {
        'query': keyword,
        'display': 10
    }

    url = 'https://openapi.naver.com/v1/search/news.json'

    res = requests.get(url, headers=headers, params=payload)
    #print('==> request send!\n')
    #print('==> request result : ')
    request_items = res.json()['items']

    for item in request_items:
        if keyword in item['title']:
            print('{} : {} : \n{} \n{} \n'.format(item['pubDate'],  item['title'], item['link'], item['description']))

    # TODO 현재 시간 1시간 데이터만 추출


def main():
    keyword_list = ['영림원소프트랩', '엘엠에스', '제넥신']
    for keyword in keyword_list:
        print('=====================================================')
        print(keyword)
        print('=====================================================')
        get_naver_news(keyword)


if __name__ == '__main__':
    main()
