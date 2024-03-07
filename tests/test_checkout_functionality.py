import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

FIRSTNAME = "Kate"
LASTNAME = "Parker"
POSTCODE = "12345"


class TestCheckoutProcess:
    def test_checkout_functionality(self, login_to_saucedemo, add_profuct_to_saucedome):
        checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
        assert checkout_button.is_displayed(), "The button is not visible"
        checkout_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "checkout_info_container")))
        first_name_field = driver.find_element(By.XPATH, '//input[@id="first-name"]')
        assert first_name_field.is_displayed(), "The first name is not visible"
        first_name_field.send_keys(FIRSTNAME)
        current_first_name_value = first_name_field.get_attribute("value")
        assert current_first_name_value == FIRSTNAME, "The first name is not displayed correctly.."

        last_name_field = driver.find_element(By.XPATH, '//input[@id="last-name"]')
        assert last_name_field.is_displayed(), "The last name is not visible"
        last_name_field.send_keys(LASTNAME)
        current_last_name_value = last_name_field.get_attribute("value")
        assert current_last_name_value == LASTNAME, "The last name is not displayed correctly"

        post_code_field = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
        assert post_code_field.is_displayed(), "The post code is not visible"
        post_code_field.send_keys(POSTCODE)
        current_post_code_value = post_code_field.get_attribute("value")
        assert current_post_code_value == POSTCODE, "The post code is not displayed"

        continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
        assert continue_button.is_displayed(), "The continue button is not visible"
        continue_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "checkout_summary_container")))
        finish_button = driver.find_element(By.XPATH, '//button[@id="finish"]')
        assert finish_button.is_displayed(), "The button is not visible"
        finish_button.click()

        header = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')
        assert header.is_displayed(), "Order confirmation message not found"

        logging.info("Test4 passed: THANK YOU FOR YOUR ORDER a confirmation message is displayed.")

        driver.close()
