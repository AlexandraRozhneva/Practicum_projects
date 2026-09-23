import pytest
from pages.main_page import MainPage
from data.test_data import TestData

class TestFAQ:
    """Тесты для раздела Вопросы о важном"""
    
    @pytest.mark.parametrize("question_index", range(8))
    def test_faq_question(self, driver, wait, question_index):
        """
        Проверка, что при клике на вопрос открывается соответствующий ответ
        """
        main_page = MainPage(driver, wait)
        main_page.open()
        main_page.close_cookie_banner()
        
        main_page.click_faq_question(question_index)
        
        actual_answer = main_page.get_faq_answer_text(question_index)
        expected_answer = TestData.FAQ_EXPECTED_ANSWERS[question_index]
        
        assert actual_answer == expected_answer, \
            f"Неверный ответ на вопрос {question_index + 1}\nОжидалось: {expected_answer}\nПолучено: {actual_answer}"