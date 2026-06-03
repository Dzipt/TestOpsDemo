import allure
from steps.common_steps import open_page, login_as, assert_page_title

@allure.feature("Профиль")
@allure.story("Просмотр профиля")
def test_view_profile():
    open_page("https://example.com/login")
    login_as("admin@demo.com", "secret")
    open_page("https://example.com/profile")
    assert_page_title("Мой профиль")

@allure.feature("Настройки")
@allure.story("Открытие настроек")
def test_open_settings():
    open_page("https://example.com/login")
    login_as("admin@demo.com", "secret")
    open_page("https://example.com/settings")
    assert_page_title("Настройки")