import re

MAX_NAME_LENGTH = 50
MIN_NAME_LENGTH = 2

def validate_username(username):
    if not username or not isinstance(username, str):
        raise ValueError("Username обязателен")
    if len(username) < 3 or len(username) > 30:
        raise ValueError("Username от 3 до 30 символов")
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValueError("Только буквы, цифры и подчёркивание")
    return True

def validate_name(name):
    if not name or not isinstance(name, str):
        raise ValueError("Имя обязательно")
    name = name.strip()
    if len(name) < MIN_NAME_LENGTH or len(name) > MAX_NAME_LENGTH:
        raise ValueError(f"Имя от {MIN_NAME_LENGTH} до {MAX_NAME_LENGTH} символов")
    if not re.match(r'^[А-Яа-яЁёA-Za-z\s-]+$', name):
        raise ValueError("Только буквы, пробел и дефис")
    return True

def validate_url(url):
    if not url or not isinstance(url, str):
        raise ValueError("URL обязателен")
    pattern = r'^https?://[\w\.-]+\.[a-zA-Z]{2,}(/.*)?$'
    if not re.match(pattern, url):
        raise ValueError("Неверный формат URL")
    return True

def validate_ip(ip):
    if not ip or not isinstance(ip, str):
        raise ValueError("IP обязателен")
    parts = ip.split('.')
    if len(parts) != 4:
        raise ValueError("IP должен содержать 4 части")
    for part in parts:
        if not part.isdigit():
            raise ValueError("Каждая часть — число")
        if int(part) < 0 or int(part) > 255:
            raise ValueError("Каждая часть от 0 до 255")
    return True
