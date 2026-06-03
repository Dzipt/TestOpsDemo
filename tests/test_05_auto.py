import allure
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

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

@allure.feature("API — Посты")
@allure.story("Создание поста")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_post():
    payload = {"title": "Demo", "body": "Allure TestOps", "userId": 1}

    with allure.step("Отправить POST /posts"):
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        allure.attach(str(payload), name="Request body", attachment_type=allure.attachment_type.JSON)
        allure.attach(response.text, name="Response body", attachment_type=allure.attachment_type.JSON)

    with allure.step("Статус код = 201"):
        assert response.status_code == 201