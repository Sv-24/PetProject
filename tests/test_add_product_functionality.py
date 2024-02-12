from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver


class TestAddProduct:

    def test_add_product_functionality(self, login_to_saucedemo):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
        add_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
        add_button.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="shopping_cart_container"]')))
        container_button = driver.find_element(By.CLASS_NAME, "shopping_cart_container")
        container_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="cart_list"]')))
        item = driver.find_element(By.XPATH, '//div[@class="inventory_item_name" and text() = "Sauce Labs Backpack"] ')
        assert item.is_displayed(), " item is not displayed in the cart_list."

        print("Test passed: The item is present in the cart.")

        driver.close()
