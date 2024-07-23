import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Import TimeoutException

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get("https://app.asana.com/-/login")
    email = driver.find_element(By.NAME, "e")
    email.send_keys("rxr5870@mavs.uta.edu")
    email.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    password = wait.until(EC.visibility_of_element_located((By.ID, "lui_6")))
    password.send_keys("rxr@1234")
    password.send_keys(Keys.ENTER)

    message_element = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.ID, "asana_full_page")))
          
           
    assert message_element.is_displayed(), "Login failed!"
      
    driver.quit()

if __name__ == "__main__":
    pytest.main()
