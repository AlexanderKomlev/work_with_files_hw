with open('1.txt', encoding='utf-8') as f1, open('2.txt', encoding='utf-8') as f2, open('3.txt', encoding='utf-8') as f3:
    file_list = []

    for file in [f1, f2, f3]:
        file_list.append({'filename': file.name, 'lines': len(file.readlines()), 'id': file})
        print(file.read())
    file_list = sorted(file_list, key=lambda x: x['lines'])
    f1.seek(0)
    f2.seek(0)
    f3.seek(0)

    with open('result.txt', 'a') as result:
        for file in file_list:
            result.write(file['filename'])
            result.write('\n')
            result.write(str(file['lines']))
            result.write('\n')
            result.write(file['id'].read())
            result.write('\n')
