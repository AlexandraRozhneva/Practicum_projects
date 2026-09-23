import sys
import os
import pytest
import allure
from helpers.data_generators import generate_user_data, get_ingredient_hashes, get_invalid_hash
from helpers.api_requests import register_user, delete_user

# Добавляем корневую директорию проекта в sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture
def new_user_data():
    """Фикстура с данными для нового пользователя."""
    return generate_user_data()

@pytest.fixture
def registered_user(new_user_data):
    """Фикстура, которая регистрирует пользователя и возвращает его данные и токен."""
    response = register_user(new_user_data)
    assert response.status_code == 200, f"Не удалось создать пользователя: {response.text}"
    token = response.json().get("accessToken")
    
    yield {
        "user": new_user_data,
        "token": token
    }
    
    # Удаление пользователя после теста
    delete_user(token)

@pytest.fixture
def temp_user(new_user_data):
    """Фикстура для временного пользователя (удаляется после теста)."""
    response = register_user(new_user_data)
    assert response.status_code == 200, f"Не удалось создать пользователя: {response.text}"
    token = response.json().get("accessToken")
    
    yield {
        "user": new_user_data,
        "token": token
    }
    
    # Удаление пользователя после теста
    delete_user(token)

@pytest.fixture
def ingredient_hashes():
    """Фикстура с валидными хешами ингредиентов."""
    return get_ingredient_hashes()

@pytest.fixture
def invalid_ingredient_hash():
    """Фикстура с невалидным хешем."""
    return get_invalid_hash()