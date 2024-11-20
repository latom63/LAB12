import json

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def display_json(file_path):
    data = load_json(file_path)
    print(json.dumps(data, ensure_ascii=False, indent=4))

def add_record(file_path):
    data = load_json(file_path)
    name = input("Введіть ім'я: ")
    gender = input("Введіть стать (ч/ж): ")
    height = int(input("Введіть зріст (см): "))
    data.append({"name": name, "gender": gender, "height": height})
    save_json(file_path, data)
    print("Запис додано.")

def delete_record(file_path):
    data = load_json(file_path)
    name = input("Введіть ім'я учня для видалення: ")
    data = [record for record in data if record['name'] != name]
    save_json(file_path, data)
    print("Запис видалено.")

def search_record(file_path):
    data = load_json(file_path)
    search_field = input("Введіть поле для пошуку (name/gender/height): ")
    search_value = input("Введіть значення для пошуку: ")
    if search_field == 'height':
        search_value = int(search_value)
    results = [record for record in data if record.get(search_field) == search_value]
    print(json.dumps(results, ensure_ascii=False, indent=4))

def analyze_heights(file_path, output_path):
    data = load_json(file_path)
    girls_height = sum(record['height'] for record in data if record['gender'] == 'ж')
    boys_height = sum(record['height'] for record in data if record['gender'] == 'ч')
    result = {
        "girls_height": girls_height,
        "boys_height": boys_height,
        "girls_exceed_boys": girls_height > boys_height
    }
    save_json(output_path, result)
    print("Результати аналізу збережено в", output_path)

def main():
    input_file = "students.json"
    output_file = "analysis.json"

    while True:
        print("\nМеню:")
        print("1. Вивести вміст JSON файлу")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Пошук записів")
        print("5. Аналіз зросту (результат в інший файл)")
        print("6. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            display_json(input_file)
        elif choice == '2':
            add_record(input_file)
        elif choice == '3':
            delete_record(input_file)
        elif choice == '4':
            search_record(input_file)
        elif choice == '5':
            analyze_heights(input_file, output_file)
        elif choice == '6':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
1