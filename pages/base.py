import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import urls
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @allure.step("Открыть страницу сайта")
    def open(self, path = None):
        if path is None:
            with allure.step("Открытие главной страницы сайта"):
                return self._driver.get(urls.TEST_URL)
        return self._driver.get(f"{urls.TEST_URL}/{path}")

    def compare_url(self, url):
        self._wait_for_url_site(url)
        return self._driver.current_url == url

    @allure.step("Подождать кликабельность элемента")
    def _wait_for_clickable(self, element):
        return WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(element))

    @allure.step('Ожидаем загрузки страницы URL')
    def _wait_for_url_site(self, url):
        return WebDriverWait(self._driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step("Подождать открытие элемента (локатор)")
    def _wait_for_visible_by_locator(self, locator):
        try:
            WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    @allure.step("Подождать закрытие элемента (локатор)")
    def _wait_for_invisible_by_locator(self, locator):
        try:
            WebDriverWait(self._driver, 10).until(expected_conditions.invisibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    @allure.step("Подождать открытие элемента")
    def _wait_for_visible(self, element):
        return WebDriverWait(self._driver, 20).until(expected_conditions.visibility_of(element))

    @allure.step("Подождать кликабельность элемента (локатор)")
    def _wait_for_clickable_by_locator(self, locator):
        return WebDriverWait(self._driver, 20).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Подождать открытие элемента (локатор, список)")
    def _wait_for_visible_list_by_locator(self, locator):
        return WebDriverWait(self._driver, 20).until(expected_conditions.visibility_of_all_elements_located(locator))
