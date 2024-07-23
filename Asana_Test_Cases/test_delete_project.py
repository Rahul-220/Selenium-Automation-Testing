import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_delete_project(driver):
    driver.get("https://app.asana.com/-/login")

    email = driver.find_element(By.NAME, "e")
    email.send_keys("rxr5870@mavs.uta.edu")
    email.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    password = wait.until(EC.visibility_of_element_located((By.ID, "lui_6")))
    password.send_keys("rxr@1234")
    password.send_keys(Keys.ENTER)

    time.sleep(5)

    project_select = driver.find_element(By.LINK_TEXT, "Test project created")
    project_select.click()

    time.sleep(5)

    down = driver.find_element(By.XPATH, "(//*[name()='svg'][@class='Icon DownIcon'])[1]")
    down.click()

    time.sleep(2)

    delete_project = driver.find_element(By.XPATH, "//span[normalize-space()='Delete project']")
    delete_project.click()

    time.sleep(5)

    delete_button = driver.find_element(By.XPATH, "//div[normalize-space()='Delete']")
    delete_button.click()

    driver.quit()
