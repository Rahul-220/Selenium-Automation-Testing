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

def test_create_project(driver):
    driver.get("https://app.asana.com/-/login")

    email = driver.find_element(By.NAME, "e")
    email.send_keys("rxr5870@mavs.uta.edu")
    email.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    password = wait.until(EC.visibility_of_element_located((By.ID, "lui_6")))
    password.send_keys("rxr@1234")
    password.send_keys(Keys.ENTER)

    time.sleep(5)

    add_create_button = driver.find_element(By.CSS_SELECTOR,"div[aria-label='Create']")
    add_create_button.click()
    time.sleep(5)

    add_project = driver.find_element(By.XPATH,"//span[normalize-space()='Project']")
    add_project.click()

    time.sleep(5)

    my_tasks = driver.find_element(By.CSS_SELECTOR,"img[src='https://d3ki9tyy5l5ruj.cloudfront.net/obj/2201b53b56249b2529f04482c2f2049dc1bf1c61/rocket.svg']")
    my_tasks.click()

    time.sleep(2)

    start_scratch = driver.find_element(By.CSS_SELECTOR,".ThemeableCardPresentation--isValid.ThemeableCardPresentation.ThemeableInteractiveCardPresentation--isNotSelected.ThemeableInteractiveCardPresentation--isEnabled.ThemeableInteractiveCardPresentation.PlaceholderButtonCard.TemplateGalleryV2Browser-blankProjectRow")
    start_scratch.click()

    time.sleep(2)

    input = driver.find_element(By.CSS_SELECTOR,"#new_project_dialog_content_name_input")
    input.send_keys("Test project created")

    time.sleep(5)

    click_create_project = driver.find_element(By.XPATH,"//div[contains(text(),'Create project')]")
    click_create_project.send_keys(Keys.ENTER)

    time.sleep(10)

    driver.quit()