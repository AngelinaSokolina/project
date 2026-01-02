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


# Проверка (можно запустить файл и проверить)
if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
