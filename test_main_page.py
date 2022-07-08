from selenium.webdriver.common.by import By
import time


url = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(driver):
    login_link = driver.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(driver):
   driver.get(url)
   go_to_login_page(driver)



