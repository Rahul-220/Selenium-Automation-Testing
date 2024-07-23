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

def test_settings(driver):
    driver.get("https://app.asana.com/-/login")
    email = driver.find_element(By.NAME, "e")
    email.send_keys("rxr5870@mavs.uta.edu")
    email.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    password = wait.until(EC.visibility_of_element_located((By.ID, "lui_6")))
    password.send_keys("rxr@1234")
    password.send_keys(Keys.ENTER)

    time.sleep(5)
    
    drop_down = driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/div[1]/div[3]/div/div[3]/span")
    drop_down.click()
    time.sleep(5)
    
    settings = driver.find_element(By.XPATH," /html/body/div[2]/div/div/div/div/div[5]/div/div/span[2]")
    settings.click()

    time.sleep(5)
    
    driver.quit()