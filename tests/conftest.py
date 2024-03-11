import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'


@pytest.fixture
def login_to_saucedemo():
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys(USERNAME)

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    expected_product_page_url = "https://www.saucedemo.com/inventory.html"
    current_url = driver.current_url
    assert current_url == expected_product_page_url, "User is not redirected to the product page"


@pytest.fixture
def add_product_to_bucket():
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    add_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    add_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@id="shopping_cart_container"]')))
    container_button = driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
    container_button.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="cart_list"]')))
    item = driver.find_element(By.XPATH, '//div[@class="inventory_item_name" and text() = "Sauce Labs Backpack"] ')
    assert item.is_displayed(), " item is not displayed in the cart_list."
