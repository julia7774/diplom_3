import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.main import MainPage
import urls


class TestMainPage:
    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor(self, driver: WebDriver):
        page = MainPage(driver)
        page.open("feed")
        assert page.compare_url(f"{urls.TEST_URL}/feed")

        page.click_on_constructor()
        assert page.compare_url(f"{urls.TEST_URL}/")
        assert page.constructor_is_opened()

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_click_order_feed(self, driver: WebDriver):
        page = MainPage(driver)
        page.open()
        assert page.compare_url(f"{urls.TEST_URL}/")

        page.click_on_order_feed()
        assert page.compare_url(f"{urls.TEST_URL}/feed")
        assert page.order_feed_is_opened()

    @allure.title("Нажатие на ингредиент")
    def test_click_ingredient(self, driver: WebDriver):
        page = MainPage(driver)
        page.open()
        assert page.compare_url(f"{urls.TEST_URL}/")

        page.click_on_ingredient()
        assert page.ingredient_is_opened()

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver: WebDriver):
        page = MainPage(driver)
        page.open()
        assert page.compare_url(f"{urls.TEST_URL}/")
        page.click_on_ingredient()

        page.close_on_ingredient_modal()
        assert page.ingredient_is_closed()

    @allure.title("Увеличение счетчика ингредиента")
    def test_increase_ingredient_counter(self, driver: WebDriver):
        page = MainPage(driver)
        page.open()
        assert page.compare_url(f"{urls.TEST_URL}/")

        assert page.get_ingredient_counter() == '0'
        page.add_ingredient()
        assert page.get_ingredient_counter() == '2'
