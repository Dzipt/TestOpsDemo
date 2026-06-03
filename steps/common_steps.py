import allure

def open_page(url: str):
    with allure.step(f"Открыть страницу: {url}"):
        allure.attach(url, name="URL", attachment_type=allure.attachment_type.TEXT)

def login_as(user: str, password: str):
    with allure.step(f"Войти как {user}"):
        pass

def assert_page_title(expected: str):
    with allure.step(f"Заголовок страницы = '{expected}'"):
        assert True