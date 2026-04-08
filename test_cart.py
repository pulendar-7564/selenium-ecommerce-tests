import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    return driver


class TestCart:

    def test_add_item_to_cart(self, logged_in_driver):
        """TC_CART_001: User can add an item to the cart."""
        logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        badge = logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "1", "Cart badge did not update after adding item"

    def test_add_multiple_items(self, logged_in_driver):
        """TC_CART_002: User can add multiple items to the cart."""
        logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        badge = logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "2", "Cart badge should show 2 items"

    def test_remove_item_from_cart(self, logged_in_driver):
        """TC_CART_003: User can remove an item from the cart."""
        logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        logged_in_driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        badges = logged_in_driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0, "Cart badge should disappear after removing item"

    def test_cart_page_shows_added_item(self, logged_in_driver):
        """TC_CART_004: Cart page displays the added item."""
        logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_items = logged_in_driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 1, "Cart page should show 1 item"

    def test_continue_shopping_from_cart(self, logged_in_driver):
        """TC_CART_005: User can continue shopping from the cart page."""
        logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        logged_in_driver.find_element(By.ID, "continue-shopping").click()
        assert "/inventory" in logged_in_driver.current_url, "Should return to inventory page"
