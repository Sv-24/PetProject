from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'
expected_product_page_url = "https://www.saucedemo.com/inventory.html"


class TestLoginPage:
    @staticmethod
    def verify_current_url(driver, expected_url):
        current_url = driver.current_url
        if current_url == expected_url:
            return "User is redirected to the product page."
        else:
            return "User is not redirected to the product page."

    def test_login_functionality(self):

        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://www.saucedemo.com/")

        username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
        assert username_field.is_displayed(), "The username is not visible."
        username_field.send_keys(USERNAME)
        current_username_value = username_field.get_attribute("value")
        assert current_username_value == USERNAME, "The username is not displayed correctly.."

        password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
        assert password_field.is_displayed(), "The username is not visible."
        password_field.send_keys(PASSWORD)
        current_password_value = password_field.get_attribute("value")
        assert current_password_value == PASSWORD, "The password is not displayed correctly"

        login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
        login_button.click()

        result = self.verify_current_url(driver, expected_product_page_url)

        page_header = driver.find_element(By.XPATH, '//div[@class="app_logo"]')
        assert page_header.is_displayed(), "Page header is not displayed."

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="inventory_list"]')))

        first_item = driver.find_element(By.XPATH, '//a[@id="item_4_img_link"]')
        assert first_item.is_displayed(), "First item is not displayed correctly."

        print("Test passed:", result)

        driver.close()
