import re

def separate_and_sort_words(text):
    # Знайти всі слова в тексті
    words = re.findall(r'\b\w+\b', text)

    # Відсортувати українські слова
    ukrainian = sorted(
        [word for word in words if re.search(r'[а-яА-ЯїЇєЄіІ]', word)],
        key=str.casefold
    )

    # Відсортувати англійські слова
    english = sorted(
        [word for word in words if re.search(r'[a-zA-Z]', word)],
        key=str.casefold
    )

    return ukrainian + english

def process_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line = file.readline().strip()
            print("Перше речення:", line)

            sorted_list = separate_and_sort_words(line)
            print("Відсортовані слова:", sorted_list)
            print(f"Кількість слів: {len(sorted_list)}")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as error:
        print(f"Виникла помилка: {error}")

# Основна частина програми
if __name__ == "__main__":
    filename = "1.txt"
    process_file(filename)
