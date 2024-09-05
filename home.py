from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")

Selenium_Ruby = driver.find_element_by_class_name("post-160")
#Selenium_Ruby = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "post-160")) )
Selenium_Ruby.click()

reviews_tab = driver.find_element_by_class_name("reviews_tab")
reviews_tab.click()

star_5 = driver.find_element_by_class_name("star-5")
star_5.click()

comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")

author = driver.find_element_by_id("author")
author.send_keys("Liya")

email = driver.find_element_by_id("email")
email.send_keys("liya777@mail.ru")

submit = driver.find_element_by_class_name("submit")
submit.click()

driver.quit()
