import random
import string
import logging

logger = logging.getLogger(__name__)


def generate_email():
    """Генерирует случайный email"""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    email = f"{username}@{domain}.ru"
    logger.info(f"Сгенерирован email: {email}")
    return email


def generate_password():
    """Генерирует случайный пароль (минимум 6 символов)"""
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    logger.info(f"Сгенерирован пароль: {password}")
    return password


def generate_name():
    """Генерирует случайное имя"""
    name = ''.join(random.choices(string.ascii_letters, k=6))
    logger.info(f"Сгенерировано имя: {name}")
    return name