import openpyxl

def find_parks_not_in_us():
    # 엑셀파일(워크북) 열기
    wb = openpyxl.load_workbook('L17_test.xlsx')

    # 워크시트 열기
    sheet = wb['Sheet1']

    # 결과를 저장할 리스트
    park_list = []

    # 파일을 로우 단위로 읽어 국가가 US가 아닌 로우를 파일로 쓴다.
    # 1. 파일을 읽을 범위를 결정
    # 2. 로우를 순회하면서 US가 아닌 로우를 리스트로 만든다
    for row in sheet[1:sheet.max_row]:
        print(row)
        if row[5].value != 'US':
            park_list.append(row)

    # 파일 닫기
    wb.close()
    return park_list


def make_file(park_list):
    with open('park_list.txt', 'w', encoding='UTF-8') as file:
        for item in park_list:
            park_str = make_park_str(item)
            file.write(park_str + '\n')


def make_park_str(t):
    result_str = ''

    for item in t:
        result_str += str(item.value) + '\t'
    return result_str


def main():
    park_list = find_parks_not_in_us()
    make_file(park_list)
    print('park_list.txt 파일이 생성되었습니다.')


if __name__ == '__main__':
    main()