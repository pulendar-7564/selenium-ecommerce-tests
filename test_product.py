import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
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


class TestProductListing:

    def test_products_displayed(self, logged_in_driver):
        """TC_PROD_001: Products are displayed on the inventory page."""
        products = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No products found on inventory page"

    def test_product_has_name_and_price(self, logged_in_driver):
        """TC_PROD_002: Each product has a name and price."""
        names = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        prices = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        assert len(names) == len(prices), "Mismatch between product names and prices"
        for price in prices:
            assert "$" in price.text, f"Price format invalid: {price.text}"

    def test_sort_by_price_low_to_high(self, logged_in_driver):
        """TC_PROD_003: Products can be sorted by price low to high."""
        Select(logged_in_driver.find_element(By.CLASS_NAME, "product_sort_container")) \
            .select_by_value("lohi")
        prices = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        price_values = [float(p.text.replace("$", "")) for p in prices]
        assert price_values == sorted(price_values), "Products not sorted by price (low to high)"

    def test_sort_by_name_a_to_z(self, logged_in_driver):
        """TC_PROD_004: Products can be sorted alphabetically A to Z."""
        Select(logged_in_driver.find_element(By.CLASS_NAME, "product_sort_container")) \
            .select_by_value("az")
        names = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        name_texts = [n.text for n in names]
        assert name_texts == sorted(name_texts), "Products not sorted A to Z"

    def test_product_detail_page(self, logged_in_driver):
        """TC_PROD_005: Clicking a product opens its detail page."""
        first_product = logged_in_driver.find_element(By.CLASS_NAME, "inventory_item_name")
        product_name = first_product.text
        first_product.click()
        detail_name = logged_in_driver.find_element(By.CLASS_NAME, "inventory_details_name")
        assert detail_name.text == product_name, "Product detail page shows wrong product"
