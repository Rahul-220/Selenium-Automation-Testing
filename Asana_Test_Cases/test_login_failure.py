import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_failure(driver):
    driver.get("https://app.asana.com/-/login")
    email = driver.find_element(By.NAME, "e")
    email.send_keys("rxr5870@mavs.uta.edu")
    email.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    password = wait.until(EC.visibility_of_element_located((By.ID, "lui_6")))
    password.send_keys("12345678")
    password.send_keys(Keys.ENTER)

    message_element = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located(((By.XPATH, "//div[@class='MessageBanner-contents MessageBanner-contents--center']"))))
          
    assert "The username or password is not correct." in message_element.text, "Login failed!"
      
    driver.quit()

if __name__ == "__main__":
    pytest.main()

