import re

def validate_email(email):
    if not email or not isinstance(email, str):
        raise ValueError("Email обязателен")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise ValueError("Неверный формат email")
    return True

def validate_phone(phone):
    if not phone or not isinstance(phone, str):
        raise ValueError("Телефон обязателен")
    digits = re.sub(r'\D', '', phone)
    if len(digits) < 10 or len(digits) > 15:
        raise ValueError("Неверная длина телефона")
    return True

def validate_password(password):
    if not password or not isinstance(password, str):
        raise ValueError("Пароль обязателен")
    if len(password) < 8:
        raise ValueError("Пароль минимум 8 символов")
    if not re.search(r'[A-Z]', password):
        raise ValueError("Пароль должен содержать заглавную букву")
    if not re.search(r'\d', password):
        raise ValueError("Пароль должен содержать цифру")
    return True

def validate_age(age):
    if age is None:
        raise ValueError("Возраст обязателен")
    if not isinstance(age, int):
        raise ValueError("Возраст должен быть числом")
    if age < 0 or age > 120:
        raise ValueError("Возраст от 0 до 120")
    return True

def validate_birth_date(date_str):
    if not date_str:
        raise ValueError("Дата обязательна")
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, date_str):
        raise ValueError("Формат даты: YYYY-MM-DD")
    year = int(date_str[:4])
    if year < 1900 or year > 2025:
        raise ValueError("Год от 1900 до 2025")
    return True
