
import io

def custom_write(file_name, strings):
    strings_positions = {}
    line_number = 1
    file = open(file_name, 'w', encoding='utf-8')

    for string in strings:
        byte_position = file.tell()
        file.write(string + '\n')
        strings_positions[(line_number, byte_position)] = string
        line_number += 1

    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
