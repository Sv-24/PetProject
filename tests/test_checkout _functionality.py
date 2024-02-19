from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver

FIRSTNAME = "Kate"
LASTNAME = "Parker"
POSTCODE = "12345"


class TestCheckoutProcess:
    def test_checkout_functionality(self, login_to_saucedemo, add_profuct_to_saucedome):
        checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
        checkout_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "checkout_info_container")))
        first_name_field = driver.find_element(By.XPATH, '//input[@id="first-name"]')
        first_name_field.send_keys(FIRSTNAME)
        last_name_field = driver.find_element(By.XPATH, '//input[@id="last-name"]')
        last_name_field.send_keys(LASTNAME)
        post_code_field = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
        post_code_field.send_keys(POSTCODE)
        continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
        continue_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "checkout_summary_container")))
        finish_button = driver.find_element(By.XPATH, '//button[@id="finish"]')
        finish_button.click()

        header = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')
        assert header.is_displayed(), "Order confirmation message not found"

        print("Test4 passed: THANK YOU FOR YOUR ORDER a confirmation message is displayed.")

        driver.close()
