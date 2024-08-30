from pylenium.driver import Pylenium


class TestSauceDemo:
    def test_land_on_products_page_after_login(self, pyc: Pylenium):
        pyc.visit("https://www.saucedemo.com/")
        pyc.get("#user-name").type("standard_user")
        pyc.get("#password").type("secret_sauce")
        pyc.get("#login-button").click()
        assert pyc.contains("Products").should().be_visible()

    def test_add_item_to_cart_increments_counter_by_1(self, pyc: Pylenium):
        pyc.get("[id*='add-to-cart']").click()
        assert pyc.get("a.shopping_cart_link").should().have_text("1")