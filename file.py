# Открываем файл для чтения и создаем новый файл для записи



import os

# Определите путь к файлу, в который нужно записать данные
output_file_path = 'C:/Users/vivap/Desktop/seq/16S.fas'
output2 = 'C:/Users/vivap/Desktop/seq/co1.fa'
# Пройдитесь по всем файлам в указанной директории
for filename in os.listdir("C:/Users/vivap/Desktop/seq"):
    if filename.endswith(".seq") and '16S' in filename:
        input_file_path = os.path.join("C:/Users/vivap/Desktop/seq", filename)
        with open(input_file_path, 'r') as file_in, open(output_file_path, 'a') as file_out:
            for line in file_in:
                # Удаление символов конца строки
                line = line.strip()

                # Добавление символа ">" к каждой строке
                modified_line = '>' + filename +  '\n' + line

                # Вывод модифицированной строки в консоль
                print(modified_line)

                # Запись модифицированной строки в файл
                file_out.write(modified_line + '\n')
    elif filename.endswith(".seq") and 'CO1' in filename:
        input_file_path = os.path.join("C:/Users/vivap/Desktop/seq", filename)
        with open(input_file_path, 'r') as file_in, open(output2, 'a') as file_out:
            for line in file_in:
                # Удаление символов конца строки
                line = line.strip()

                # Добавление символа ">" к каждой строке
                modified_line = '>' + filename + '\n' + line

                # Вывод модифицированной строки в консоль
                print(modified_line)

                # Запись модифицированной строки в файл
                file_out.write(modified_line + '\n')



