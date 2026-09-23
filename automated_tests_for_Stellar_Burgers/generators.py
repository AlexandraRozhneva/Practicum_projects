import random
import string

def generate_email():
    """Генерирует случайный email"""
    domains = ["yandex.ru", "mail.ru", "gmail.com", "rambler.ru", "bk.ru"]
    username_length = random.randint(5, 15)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_password(min_length=6):
    """Генерирует случайный пароль"""
    length = random.randint(min_length, 12)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_name():
    """Генерирует случайное имя"""
    names = ["Александр", "Мария", "Иван", "Елена", "Дмитрий", "Анна", "Ольга", "Павел", "Екатерина", "Сергей"]
    return random.choice(names)

def generate_invalid_password():
    """Генерирует некорректный пароль (менее 6 символов)"""
    length = random.randint(1, 5)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))