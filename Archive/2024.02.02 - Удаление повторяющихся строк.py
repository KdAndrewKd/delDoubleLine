# Удаление повторяющихся строк в списке
# Результат сохронит в фаил "result.txt"

count = 0

with open("info.txt" , "r", encoding="utf-8") as content_file:
    with open("result.txt" , "w", encoding="utf-8") as save_file:
        list_content = content_file.readlines()
        
        set_content = set(list_content)
        
        for i in set_content:
            i = i.replace("\n", "")
            if i != "":
                count += 1
                save_file.write(i + "\n")
        
print("count", count)
