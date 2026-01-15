from selenium.webdriver.common.by import By


class LocatorsMain:
    HEADER_CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    HEADER_ORDER_FEED_BUTTON = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")

    INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[1]")
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    INGREDIENT_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")

    BURGER_INGREDIENTS = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    ORDER_NUMBER_INCORRECT = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")
