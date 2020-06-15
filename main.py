import csv


def new_filepath_maker(old_path, s_id):
    new_file_path = old_path.split('/')
    new_file_path.insert(-1, 'train')
    new_file_path.insert(-1, 'n' + s_id)
    return new_file_path


with open('./final_traindata.csv', newline='') as csvFile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvFile)

    # 以迴圈輸出每一列
    for row in rows:
        with open('./final_final_traindata.csv', 'a', newline='') as writtenCsvFile:
            writer = csv.writer(writtenCsvFile)
            newFilepath = new_filepath_maker(row[0], row[1])
            row[0] = '/'.join(newFilepath)
            print(row)
            writer.writerow(row)

            # row[0].split('/').insert(len(row[0].split('/')) -2, row[1])
            # print(row[0])
