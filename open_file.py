from pprint import pprint

file_name = 'poem.txt'
file = open(file_name, mode='rb')  # mode (режим): чтение бинарное
file_content = file.read()
file.close()
pprint(file_content)

#file = open(file_name, mode='r')  # mode (режим): чтение символьное
file = open(file_name, mode='r', encoding='utf8')
file_content = file.read()
file.close()
pprint(file_content)