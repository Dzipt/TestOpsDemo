import allure
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.id("6115")          # ← ID твоего тест-кейса из ТестОпс
@allure.title("GET /posts/1 — успешное получение поста")
@allure.feature("API — Посты")
@allure.story("Получение поста")
@allure.severity(allure.severity_level.NORMAL)
def test_get_post():
    with allure.step("Отправить GET /posts/1"):
        response = requests.get(f"{BASE_URL}/posts/1")
        allure.attach(
            response.text,
            name="Response body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Статус код = 200"):
        assert response.status_code == 200

    with allure.step("Тело содержит userId"):
        assert "userId" in response.json()