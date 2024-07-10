def copy_line(source_file, target_file, line_number):
    # Открываем файлы
    with open(source_file, 'r') as source, open(target_file, 'a') as target:
        # Читаем строки и выбираем нужную
        lines = source.readlines()
        if 1 <= line_number <= len(lines):
            line_to_copy = lines[line_number - 1].strip()  # -1 для перевода из 1-based в 0-based
            # Записываем выбранную строку в другой файл
            target.write(line_to_copy + '\n')
            print(f"Строка {line_number} из файла {source_file} скопирована в файл {target_file}.")
        else:
            print(f"Номер строки {line_number} выходит за пределы файла {source_file}. Нет такой строки.")

# Пример использования:
source_file = 'source.txt'
target_file = 'target.txt'

try:
    line_number = int(input("Введите номер строки для копирования из файла: "))
    copy_line(source_file, target_file, line_number)
except ValueError:
    print("Ошибка: Номер строки должен быть целым числом.")