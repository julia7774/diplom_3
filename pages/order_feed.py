import allure

import urls
from locators.order_feed import LocatorsOrderFeed
from pages.base import BasePage


class OrderFeedPage(BasePage):
    @allure.step("Открыть страницу лента заказов")
    def open(self, path = None):
        return self._driver.get(f"{urls.TEST_URL}/feed")

    @allure.step("Получить счетчик заказов")
    def get_orders_counter(self):
        self._wait_for_visible_by_locator(LocatorsOrderFeed.ORDERS_COUNTER)
        element = self._driver.find_element(*LocatorsOrderFeed.ORDERS_COUNTER)
        return element.text

    @allure.step("Получить счетчик заказов (сегодня)")
    def get_orders_today_counter(self):
        self._wait_for_visible_by_locator(LocatorsOrderFeed.TODAY_ORDERS_COUNTER)
        element = self._driver.find_element(*LocatorsOrderFeed.TODAY_ORDERS_COUNTER)
        return element.text

    @allure.step("Получить список заказов в работе")
    def get_orders_in_work(self):
        self._wait_for_visible_by_locator(LocatorsOrderFeed.IN_WORK)
        element = self._wait_for_visible_list_by_locator(LocatorsOrderFeed.IN_WORK)
        return list(map(lambda x: int(x.text[1:]), element))
