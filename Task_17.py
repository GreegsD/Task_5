import time
user_data = {
    "ID": 4,
    "прізвище": "Гуменюк",
    "Ім’я": "Артем",
    "Група": "ІПЗс-23-2",
    "Курс": 1,
    "Книги (борг)": [],
    "Статистика книг": []
}
while True:
    print("\nМеню:")
    print("1 - Вивести карту читача")
    print("2 - Взяти книгу в борг")
    print("3 - Повернути книгу")
    print("0 - Вихід")

    a = input("Виберіть опцію: ")

    if a == "1":
        time.sleep(3)
        print("Карта читача:")
        for key, value in user_data.items():
            if key not in ["Книги (борг)", "Статистика книг"]:
                print(f"{key}: {value}")
    elif a == "2":
        time.sleep(3)
        book = input("Введіть назву книги, яку бажаєте взяти в борг: ")
        user_data["Книги (борг)"].append(book)
        time.sleep(3)
        print(f"Книга '{book}' успішно взята в борг.")
    elif a == "3":
        if user_data["Книги (борг)"]:
            time.sleep(3)
            print("Список книг у боргу:")
            for book in user_data["Книги (борг)"]:
                print(book)
                time.sleep(3)
            book = input("Введіть назву книги, яку бажаєте повернути: ")
            if book in user_data["Книги (борг)"]:
                time.sleep(3)
                user_data["Книги (борг)"].remove(book)
                user_data["Статистика книг"].append(book)
                print(f"Книга '{book}' успішно повернута.")
            else:
                print(f"Книги '{book}' немає в боргу.")
        else:
            print("Немає книг у боргу.")
    elif a == "0":
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
