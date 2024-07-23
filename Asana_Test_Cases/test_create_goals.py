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

def test_create_goals(driver):
    driver.get("https://app.asana.com/-/login")

    email = driver.find_element(By.NAME, "e")
    email.send_keys("rxr5870@mavs.uta.edu")
    email.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    password = wait.until(EC.visibility_of_element_located((By.ID, "lui_6")))
    password.send_keys("rxr@1234")
    password.send_keys(Keys.ENTER)

    time.sleep(5)

    my_goals = driver.find_element(By.LINK_TEXT,"Goals")
    my_goals.click()

    time.sleep(5)

    add_goal = driver.find_element(By.CSS_SELECTOR,".ThemeableRectangularButtonPresentation--isEnabled.ThemeableRectangularButtonPresentation.ThemeableRectangularButtonPresentation--medium.PrimaryButton--standardTheme.PrimaryButton.GoalIndexListPageToolbar-addGoalButton")
    add_goal.click()

    time.sleep(2)

    blank_goal = driver.find_element(By.XPATH,"//span[normalize-space()='Blank goal']")
    blank_goal.click()

    time.sleep(5)

    goal_title = driver.find_element(By.CSS_SELECTOR,"#create_goal_dialog_name_input")
    goal_title.send_keys("Complete Assignment")

    time.sleep(5)

    save_goal_button = driver.find_element(By.XPATH,"//div[normalize-space()='Save goal']")
    save_goal_button.click()

    driver.quit()
