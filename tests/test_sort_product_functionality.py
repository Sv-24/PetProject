from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver


class TestSortProduct:

    def test_sort_product_a_z_functionality(self, login_to_saucedemo):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

        sort_option = driver.find_element(By.XPATH, '//span[@class="select_container"]')
        sort_option.click()

        sort_option_a_z = driver.find_element(By.XPATH, '//option[text()="Name (A to Z)"]')
        sort_option_a_z.click()

        product_names_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        product_names = [elem.text for elem in product_names_elements]

        if sort_option_a_z == "Name (A to Z)":
            assert product_names == sorted(product_names), "Products are not sorted alphabetically (A to Z)"

    def test_sort_product_z_a_functionality(self, login_to_saucedemo):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

        sort_option = driver.find_element(By.XPATH, '//span[@class="select_container"]')
        sort_option.click()

        sort_option_z_a = driver.find_element(By.XPATH, '//option[text()="Name (Z to A)"]')
        sort_option_z_a.click()

        product_names_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        product_names = [elem.text for elem in product_names_elements]

        if sort_option_z_a == "Name (Z to A)":
            assert product_names == sorted(product_names), "Products are not sorted alphabetically (Z to A)"

    def test_sort_product_price_low_high_functionality(self, login_to_saucedemo):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

        sort_option = driver.find_element(By.XPATH, '//span[@class="select_container"]')
        sort_option.click()

        sort_option_price_low_high = driver.find_element(By.XPATH, '//option[text()="Price (low to high)"]')
        sort_option_price_low_high.click()

        product_prices_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        product_prices = [float(elem.text.strip("$")) for elem in product_prices_elements]

        assert product_prices == sorted(product_prices), "Products are not sorted correctly by price"


    def test_sort_product_price_high_low_functionality(self, login_to_saucedemo):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

        sort_option = driver.find_element(By.XPATH, '//span[@class="select_container"]')
        sort_option.click()

        sort_option_price_high_low = driver.find_element(By.XPATH, '//option[text()="Price (high to low)"]')
        sort_option_price_high_low.click()

        product_prices_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        product_prices = [float(elem.text.strip("$")) for elem in product_prices_elements]

        assert product_prices == sorted(product_prices,
                                        reverse=True), "Products are not sorted correctly by price (high to low)"

        print("Test passed: The products is sorted with different ways.")

        driver.close()
