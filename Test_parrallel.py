import time

from selenium import webdriver


def test_google():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    time.sleep(3)
    driver.quit()


def test_yatra():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.yatra.com/")
    time.sleep(3)
    driver.quit()


def test_automation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.automationtesting.in/Register.html")
    time.sleep(3)
    driver.quit()


def test_nopcommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com/")
    time.sleep(3)
    driver.quit()