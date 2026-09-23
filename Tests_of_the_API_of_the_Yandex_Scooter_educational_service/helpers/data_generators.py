import random
import string


def generate_random_string(length=10):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_login():
    return generate_random_string(10)


def generate_random_password():
    return generate_random_string(10)


def generate_random_first_name():
    return generate_random_string(10)