# Импортируем функции из модуля masks
from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(info: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""

    # Разделяем строку на части.
    parts = info.split()

    # Извлекаем номер
    number = parts[-1]

    # Сбор названия, т.е. склеиваем обратно изначальный ввод через пробел
    name = " ".join(parts[:-1])

    # Проверяем, счет это или карта
    if name.lower().replace("ё", "е") == "счет":
        # Используем функцию для счета из модуля masks
        return f"{name} {get_mask_account(number)}"
    else:
        # Используем функцию для карты из модуля masks
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Функция, которая принимает на вход строку с датой и возвращает её в формате ДД.ММ.ГГГГ"""

    # Извлекаем дату до символа 'T' и отсекаем время
    date_part = date_string.split("T")[0]

    # Разрезаем эту дату по дефису и получим год, месяц и день
    parts = date_part.split("-")

    # Собираем элементы в обратном порядке через точку
    formatted_date = f"{parts[2]}.{parts[1]}.{parts[0]}"

    return formatted_date

# Проверка, чтобы запустить файлы и проверить
if __name__ == "__main__":
    # Функция, которая умеет обрабатывать информацию как о картах, так и о счетах
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))

    # Функция, которая принимает на вход строку с датой и возвращает её в формате ДД.ММ.ГГГГ
    print(get_date("2024-03-11T02:26:18.671407"))
