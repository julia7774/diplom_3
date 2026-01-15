import allure

from pages.main import MainPage
from pages.order_feed import OrderFeedPage


class TestOrderFeed:
    @allure.title("Увеличение счетчика выполненных заказов")
    def test_increase_completed_counter(self, authenticated):
        main = MainPage(authenticated)
        order_feed = OrderFeedPage(authenticated)

        order_feed.open()
        orders = order_feed.get_orders_counter()

        main.open()
        main.add_ingredient()
        main.click_on_order()

        order_feed.open()
        assert int(order_feed.get_orders_counter()) > int(orders)

    @allure.title("Увеличение счетчика выполненных за сегодня заказов")
    def test_increase_completed_today_counter(self, authenticated):
        main = MainPage(authenticated)
        order_feed = OrderFeedPage(authenticated)

        order_feed.open()
        orders = order_feed.get_orders_today_counter()

        main.open()
        main.add_ingredient()
        main.click_on_order()

        order_feed.open()
        assert int(order_feed.get_orders_today_counter()) > int(orders)

    @allure.title("Появление номера заказа в разделе «В работе»")
    def test_show_order_number(self, authenticated):
        main = MainPage(authenticated)
        order_feed = OrderFeedPage(authenticated)

        main.open()
        main.add_ingredient()
        order = main.click_on_order()

        order_feed.open()
        in_work = order_feed.get_orders_counter()
        assert order in in_work, "Некорректно возвращается номер заказа при оформлении"
