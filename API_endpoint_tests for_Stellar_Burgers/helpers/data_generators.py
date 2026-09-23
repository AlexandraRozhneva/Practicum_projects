from datetime import datetime
import requests

BASE_URL = "https://stellarburgers.education-services.ru/api"

def generate_user_data():
    """Генерирует уникальные данные для регистрации пользователя."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return {
        "email": f"user_{timestamp}@test.com",
        "password": f"pass_{timestamp}",
        "name": f"Name_{timestamp}"
    }

def get_ingredient_hashes():
    """Получает реальные хеши ингредиентов через API."""
    try:
        response = requests.get(f"{BASE_URL}/ingredients", timeout=5)
        if response.status_code == 200:
            ingredients = response.json().get("data", [])
            if len(ingredients) >= 2:
                return [ingredients[0]["_id"], ingredients[1]["_id"]]
    except requests.RequestException as e:
        print(f"Ошибка при получении ингредиентов: {e}")
    
    # Fallback хеши (проверенные рабочие)
    return ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]

def get_invalid_hash():
    """Возвращает заведомо невалидный хеш."""
    return ["invalid_hash_123"]