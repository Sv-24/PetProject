import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestAddProduct:

    def test_add_product_functionality(self, login_to_saucedemo):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="inventory_list"]')))
        add_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
        assert add_button.is_displayed(), "The button is not visible"
        add_button.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="shopping_cart_container"]')))
        container_button = driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
        assert container_button.is_displayed(), "The button is not visible"
        container_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="cart_list"]')))
        item = driver.find_element(By.XPATH, '//div[@class="inventory_item_name" and text() = "Sauce Labs Backpack"] ')
        assert item.is_displayed(), " item is not displayed in the cart_list."

        logging.info("Test passed: The item is present in the cart.")

        driver.close()
