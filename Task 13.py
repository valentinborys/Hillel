main_string = "Это строка, в которой мы будем искать подстроку."

# Определяем подстроку, которую будем искать
sub_string = "которой"

# Используем метод find() для поиска подстроки в строке
index = main_string.find(sub_string)

# Проверяем результат
if index != -1:
    print("Подстрока найдена в позиции:", index)
else:
    print("Подстрока не найдена.")