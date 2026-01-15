from selenium.webdriver.common.by import By


class LocatorsLogin:
    TITLE = (By.XPATH, './/h2[text()="Вход"]')
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    EMAIL = (By.XPATH, './/label[text()="Email"]//parent::*/input')
    PASSWORD = (By.XPATH, './/input[@type="password"]')
