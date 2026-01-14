import allure
from pages.base import BasePage
from locators import LocatorsMain, LocatorsOrderFeed


class MainPage(BasePage):
    @allure.step("Нажать на кнопку «Конструктор»")
    def click_on_constructor(self):
        element = self._wait_for_clickable_by_locator(LocatorsMain.HEADER_CONSTRUCTOR_BUTTON)
        element.click()

    @allure.step("Проверить открытие конструктора")
    def constructor_is_opened(self):
        return (
            self._wait_for_visible_by_locator(LocatorsMain.CONSTRUCTOR_TITLE)
            and self._wait_for_visible_by_locator(LocatorsMain.BUNS_SECTION)
            and self._wait_for_visible_by_locator(LocatorsMain.SAUCES_SECTION)
            and self._wait_for_visible_by_locator(LocatorsMain.FILLINGS_SECTION)
        )

    @allure.step("Нажать на кнопку Лента Заказов")
    def click_on_order_feed(self):
        element = self._wait_for_clickable_by_locator(LocatorsMain.HEADER_ORDER_FEED_BUTTON)
        element.click()

    @allure.step("Проверить открытие ленты заказов")
    def order_feed_is_opened(self):
        return self._wait_for_visible_by_locator(LocatorsOrderFeed.ORDER_FEED_TITLE)

    @allure.step("Нажать на ингредиент")
    def click_on_ingredient(self):
        element = self._wait_for_clickable_by_locator(LocatorsMain.INGREDIENT)
        element.click()

    @allure.step("Проверить открытие модального окна ингредиента")
    def ingredient_is_opened(self):
        return self._wait_for_visible_by_locator(LocatorsMain.INGREDIENT_MODAL)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_on_ingredient_modal(self):
        element = self._wait_for_clickable_by_locator(LocatorsMain.INGREDIENT_MODAL_CLOSE)
        element.click()

    @allure.step("Проверить закрытие модального окна ингредиента")
    def ingredient_is_closed(self):
        return self._wait_for_invisible_by_locator(LocatorsMain.INGREDIENT_MODAL)

    @allure.step("Добавить ингредиент")
    def add_ingredient(self):
        # actions = ActionChains(self._driver)

        source = self._wait_for_clickable_by_locator(LocatorsMain.INGREDIENT)
        # actions.click_and_hold(source)

        target = self._driver.find_element(*LocatorsMain.BURGER_INGREDIENTS)
        # actions.move_to_element(target)
        # actions.release(target)
        # actions.perform()

        self._driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();
            const dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragStartEvent);

            const dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dragOverEvent);

            const dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dropEvent);

            const dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragEndEvent);
            """,
            source,
            target
        )

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        self._wait_for_visible_by_locator(LocatorsMain.INGREDIENT_COUNTER)
        element = self._driver.find_element(*LocatorsMain.INGREDIENT_COUNTER)
        return element.text

    @allure.step("Оформить заказ")
    def click_on_order(self):
        element = self._wait_for_clickable_by_locator(LocatorsMain.ORDER_BUTTON)
        element.click()
        return self._get_order_number()

    @allure.step("Закрыть окно офрмления заказа")
    def close_on_order_modal(self):
        element = self._wait_for_clickable_by_locator(LocatorsMain.ORDER_MODAL)
        element.click()

    @allure.step("Получить номер заказа")
    def _get_order_number(self):
        self._wait_for_visible_by_locator(LocatorsMain.ORDER_NUMBER)
        element = self._driver.find_element(*LocatorsMain.ORDER_NUMBER)
        return element.text
