# python -m pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome("/Users/HPmaster/Desktop/skill_facktory/skillfactory/python_selenium_sf/chromedriver")
driver.get("https://habr.com/ru/company/inDrive/blog/693768/")
(driver.find_element(By.XPATH, "//*id=[\"image\"]/img"))[0].click

sleep(3)
driver.save_screenshot('habr.png')
driver.get("https://habr.com/ru/company/inDrive/blog/693768/ ")

driver.quit