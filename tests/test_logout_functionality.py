import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver


class TestLogoutPage:

    @pytest.fixture
    def login_to_saucedemo(self, login_to_saucedemo):
        expected_product_page_url = "https://www.saucedemo.com/inventory.html"
        current_url = driver.current_url
        assert current_url == expected_product_page_url, "User is not redirected to the product page."
        return login_to_saucedemo

    def test_logout_functionality(self, login_to_saucedemo):
        menu_button = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
        assert menu_button.is_displayed(), "The button is not visible"
        menu_button.click()

        logout_button = driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]')
        assert logout_button.is_displayed(), "The button is not visible"
        logout_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/"))

        restricted_page_url = "https://www.saucedemo.com/inventory.html"
        driver.get(restricted_page_url)
        WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/"))

        header = driver.find_element(By.XPATH, '//div[@class="login_logo"]')
        assert header.is_displayed(), "Page header is not displayed."

        logging.info("Test passed:User successfully log out of the application")

        driver.close()
