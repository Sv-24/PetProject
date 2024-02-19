from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'


class TestLoginPage:

    def test_login_functionality(self):

        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://www.saucedemo.com/")

        username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
        username_field.send_keys(USERNAME)
        # TODO: add step for checking username field value
        assert username_field.is_displayed(), "The username is not visible."

        password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
        password_field.send_keys(PASSWORD)

        login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
        login_button.click()

        expected_product_page_url = "https://www.saucedemo.com/inventory.html"
        current_url = driver.current_url
        if current_url == expected_product_page_url:
            print("User is redirected to the product page.")
        else:
            print("User is not redirected to the product page.")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="inventory_list"]' )))

        #inventory_list = driver.find_element(By.XPATH, '//div[@class="inventory_list"]')
        #assert inventory_list.is_displayed(), "Inventory list is not displayed."

        first_item = driver.find_element(By.XPATH, '//a[@id="item_4_img_link"]')
        assert first_item.is_displayed(), "First item is not displayed correctly."

        print("Test passed: User successfully logged in and viewed the available products.")

        driver.close()

