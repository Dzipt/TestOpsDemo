import allure
from pytest_bdd import scenario, given, when, then

@allure.feature("Checkout")
@scenario("features/checkout.feature", "Успешная оплата картой")
def test_checkout_success():
    pass

@given("пользователь авторизован в системе")
def user_is_logged_in():
    allure.attach("user_id=42", name="Session", attachment_type=allure.attachment_type.TEXT)

@given('в корзине есть товар "Ноутбук" стоимостью 99990 рублей')
def cart_has_laptop():
    pass

@when("пользователь выбирает оплату картой")
def select_card_payment():
    pass

@when("вводит корректные данные карты")
def enter_card_details():
    allure.attach("4111 **** **** 1111", name="Card (masked)", attachment_type=allure.attachment_type.TEXT)

@then("заказ успешно создаётся")
def order_is_created():
    assert True

@then("пользователь получает email с подтверждением")
def confirmation_email_sent():
    assert True