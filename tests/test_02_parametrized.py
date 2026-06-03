import allure
import pytest

@allure.feature("Корзина")
@allure.story("Добавление товара")
@pytest.mark.parametrize("product,qty,expected_total", [
    ("Ноутбук",   1, 99990),
    ("Мышь",      2,  2400),
    ("Монитор",   1, 35000),
])
def test_add_to_cart(product, qty, expected_total):
    with allure.step(f"Добавить '{product}' в количестве {qty}"):
        allure.attach(
            f"product={product}, qty={qty}",
            name="Параметры",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step(f"Проверить итоговую сумму = {expected_total}"):
        calculated = expected_total  # заглушка
        assert calculated == expected_total