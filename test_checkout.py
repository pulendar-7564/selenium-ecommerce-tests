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
def cart_ready_driver(driver):
    """Login and add an item to cart, ready for checkout."""
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    return driver


class TestCheckout:

    def test_checkout_page_loads(self, cart_ready_driver):
        """TC_CHK_001: Checkout page loads after clicking checkout."""
        assert "checkout-step-one" in cart_ready_driver.current_url

    def test_checkout_with_valid_details(self, cart_ready_driver):
        """TC_CHK_002: User can proceed with valid checkout details."""
        cart_ready_driver.find_element(By.ID, "first-name").send_keys("Pulendar")
        cart_ready_driver.find_element(By.ID, "last-name").send_keys("Golla")
        cart_ready_driver.find_element(By.ID, "postal-code").send_keys("500001")
        cart_ready_driver.find_element(By.ID, "continue").click()
        assert "checkout-step-two" in cart_ready_driver.current_url

    def test_checkout_empty_first_name(self, cart_ready_driver):
        """TC_CHK_003: Error shown when first name is missing."""
        cart_ready_driver.find_element(By.ID, "last-name").send_keys("Golla")
        cart_ready_driver.find_element(By.ID, "postal-code").send_keys("500001")
        cart_ready_driver.find_element(By.ID, "continue").click()
        error = cart_ready_driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert "First Name is required" in error.text

    def test_order_summary_shows_item(self, cart_ready_driver):
        """TC_CHK_004: Order summary page shows the item in cart."""
        cart_ready_driver.find_element(By.ID, "first-name").send_keys("Pulendar")
        cart_ready_driver.find_element(By.ID, "last-name").send_keys("Golla")
        cart_ready_driver.find_element(By.ID, "postal-code").send_keys("500001")
        cart_ready_driver.find_element(By.ID, "continue").click()
        items = cart_ready_driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items) > 0, "Order summary should show at least one item"

    def test_complete_order(self, cart_ready_driver):
        """TC_CHK_005: User can complete the order successfully."""
        cart_ready_driver.find_element(By.ID, "first-name").send_keys("Pulendar")
        cart_ready_driver.find_element(By.ID, "last-name").send_keys("Golla")
        cart_ready_driver.find_element(By.ID, "postal-code").send_keys("500001")
        cart_ready_driver.find_element(By.ID, "continue").click()
        cart_ready_driver.find_element(By.ID, "finish").click()
        confirmation = cart_ready_driver.find_element(By.CLASS_NAME, "complete-header")
        assert "Thank you" in confirmation.text, "Order completion message not shown"
