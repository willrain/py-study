from requests import Request
from requests import Session
import pprint

# 파파고 번역
# https://developers.naver.com/docs/papago/papago-nmt-api-reference.md

headers = {
    'X-Naver-Client-Id': '5KofzjFZbfMZ9O5SJVQB',
    'X-Naver-Client-Secret': 'FeO3Bap6aT',
}

text = 'Since you are not doing anything special with the Request object, you prepare it immediately and modify the PreparedRequest object.'
payload = {
    'source': 'en',
    'target': 'ko',
    'text': text,
}

url = 'https://openapi.naver.com/v1/papago/n2mt'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()

s = Session()
res = s.send(prepped)
result_json = res.json()
pprint.pprint(result_json)

print('# 번역 요청 : ' + text)
print('# 번역 결과 : ' + result_json['message']['result']['translatedText'])

