from pylenium.driver import Pylenium


class TestSauceDemo:
    def test_land_on_products_page_after_login(self, pys: Pylenium):
        pys.config.custom["user"] = "standard_user"  # Set a value in one test...

        pys.visit("https://www.saucedemo.com/")
        pys.get("#user-name").type("standard_user")
        pys.get("#password").type("secret_sauce")
        pys.get("#login-button").click()
        assert pys.contains("Products").should().be_visible()

    def test_add_item_to_cart_increments_counter_by_1(self, pys: Pylenium):
        print(pys.config.custom.get("user"))  # And use it in another test
        pys.get("[id*='add-to-cart']").click()
        assert pys.get("a.shopping_cart_link").should().have_text("1")