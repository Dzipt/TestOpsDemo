import allure
import pytest

@allure.title("Авторизация пользователя")
@allure.description("""
## Проверка авторизации

Тест проверяет, что пользователь может войти в систему
с **валидными** учётными данными.

### Шаги:
1. Открыть страницу логина
2. Ввести логин и пароль
3. Нажать «Войти»
""")
@allure.feature("Auth")
@allure.story("Успешный вход")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success():
    with allure.step("Открыть страницу логина"):
        url = "https://example.com/login"
        allure.attach(url, name="URL", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Ввести учётные данные"):
        credentials = {"login": "user@demo.com", "password": "secret"}
        allure.attach(
            str(credentials),
            name="Credentials (JSON)",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверить результат"):
        # Здесь была бы реальная проверка
        allure.attach(
            open("attachments/sample.png", "rb").read(),
            name="Screenshot after login",
            attachment_type=allure.attachment_type.PNG
        )
        assert True