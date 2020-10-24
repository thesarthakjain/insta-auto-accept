from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import creds

sleep_duration = 5
username = creds.username
password = creds.password
driver = webdriver.Chrome(creds.driver)
wait = WebDriverWait(driver, 5)

def login():
    #driver.maximize_window()
    print("https://www.instagram.com/accounts/activity/")
    driver.get("https://www.instagram.com/accounts/activity/")
    print("Site opened")

    username_box = wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
    username_box.send_keys(username)
    pass_box = driver.find_element_by_name('password')
    pass_box.send_keys(password)
    submit_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
    submit_button.click()
    print("Logging you in")

    notnow_button  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
    notnow_button.click()
    print("Not now pressed")

def follow_list():
    follow_list_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/div[1]')))
    follow_list_button.click()
    print("Follow list button pressed")

def accept():
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div[1]/div/div[1]/div[3]/div/div[1]/button')))
    confirm_button.click()
    print("Request accepted.")

def refresh():
    driver.get("https://www.instagram.com/accounts/activity/")


login()
while True:
    try:
        follow_list()
        accept()
    except:
        print(f"No follow requests, trying again in {sleep_duration} seconds.")
    time.sleep(sleep_duration)
    refresh()
