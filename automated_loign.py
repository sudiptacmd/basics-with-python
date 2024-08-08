from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service('/home/sudipta/Documents/config/chromedriver-linux64/chromedriver')

def get_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("diable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    print(driver.current_url)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)
    time.sleep(2)

main()