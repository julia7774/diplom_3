from selenium.webdriver.common.by import By


class LocatorsOrderFeed:
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

    ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    IN_WORK = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady")]/li[contains(@class,"text_type_digits-default")]')
