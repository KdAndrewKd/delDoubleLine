#!/usr/bin/python3

# Версия: 2024.03.05

# Удаление повторяющихся строк в списке
# Скпипт принимает название фаила в качестве ключа. Например: ">python delDoubleLine.py nameFile.txt"
# Результат сохронит в фаил "nameFile.txt"


import os
import sys

t_Y="\033[33m"
d_c="\033[0m" 

try:
    fileName = sys.argv[1] # получаем 1й элемент списка (в примерах выше именно он отвечает за имя файла)
except IndexError: 

    print(f"{t_Y}Нужно передать название фаила в качестве аргумента{d_c}")
    print('Например: "$ python delDoubleLine.py nameFile.txt"')
    exit()
     
fileName_fpart = fileName.split(".")
file_tmp = str(fileName_fpart[0]) + ".tmp"

with open(fileName , "r", encoding="utf-8") as content_file:
    with open(file_tmp , "w", encoding="utf-8") as save_file:
        list_content = content_file.readlines()

        set_content = set(list_content)
        list_content = list(set_content)
        list_content.sort()
        
        for i in list_content:
            i = i.replace("\n", "")
            if i != "":
                save_file.write(i + "\n")
        


os.system(f'mv {file_tmp} {fileName}')