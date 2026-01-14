import allure
import data
from locators import LocatorsLogin
from pages.base import BasePage
import urls


class LoginPage(BasePage):
    @allure.step("Открыть страницу авторизации")
    def open(self, path = None):
        return self._driver.get(f"{urls.TEST_URL}/login")

    @allure.step("Залогиниться")
    def authenticate(self):
        self._wait_for_visible_by_locator(LocatorsLogin.TITLE)
        self._set_form_login()
        self._set_form_password()
        self._click_on_login()
        self._wait_for_invisible_by_locator(LocatorsLogin.LOGIN_BUTTON)

    @allure.step("Заполнить поле Логин")
    def _set_form_login(self):
        name = self._driver.find_element(*LocatorsLogin.EMAIL)
        self._wait_for_visible(name)
        name.clear()
        name.send_keys(data.LOGIN)

    @allure.step("Заполнить поле Пароль")
    def _set_form_password(self):
        name = self._driver.find_element(*LocatorsLogin.PASSWORD)
        self._wait_for_visible(name)
        name.clear()
        name.send_keys(data.PASSWORD)

    @allure.step("Нажать на войти")
    def _click_on_login(self):
        element = self._wait_for_clickable_by_locator(LocatorsLogin.LOGIN_BUTTON)
        element.click()
