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


BASE_URL = "https://www.saucedemo.com"


class TestLogin:

    def test_valid_login(self, driver):
        """TC_LOGIN_001: Valid user can log in successfully."""
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "/inventory" in driver.current_url, "Login failed - inventory page not loaded"

    def test_invalid_password(self, driver):
        """TC_LOGIN_002: Login with wrong password shows error."""
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("wrongpassword")
        driver.find_element(By.ID, "login-button").click()
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert error.is_displayed(), "Error message not displayed for invalid password"

    def test_empty_credentials(self, driver):
        """TC_LOGIN_003: Login with empty fields shows error."""
        driver.get(BASE_URL)
        driver.find_element(By.ID, "login-button").click()
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert "Username is required" in error.text

    def test_locked_out_user(self, driver):
        """TC_LOGIN_004: Locked out user cannot log in."""
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert "locked out" in error.text.lower()

    def test_logout(self, driver):
        """TC_LOGIN_005: Logged-in user can log out."""
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        ).click()
        assert driver.current_url == BASE_URL + "/"
