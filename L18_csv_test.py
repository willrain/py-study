import os
import csv
import pprint


def save_and_remove_header(filename):
    # csv 파일을 읽어 헤더를 제거하고 저장

    # csv 파일을 리스트로 만든다
    csv_rows = []
    with open(os.path.join('baseballdatabank-master', 'core', filename), 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if reader.line_num == 1:
                continue
            csv_rows.append(row)

    # 리스트를 파일로 쓴다
    with open(os.path.join('baseballdatabank-master', 'header_remove', filename), 'w') as file:
        writer = csv.writer(file)

        for row in csv_rows:
            writer.writerow(row)




def main():
    # 레더가 제거된 파일이 저장될 폴더를 만든다.
    os.makedirs(os.path.join('baseballdatabank-master', 'header-removed'), exist_ok=True)

    # 작업 디렉토리의 모든 csv 파일을 순회
    for filename in os.listdir(os.path.join('baseballdatabank-master', 'core')):
        if not filename.endswith('.csv'):
            continue

        print('saving file: ', filename)
        # 레더가 제거된 파일을 저장한다.
        save_and_remove_header(filename)

    print('job completed..')