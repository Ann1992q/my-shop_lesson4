import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id("menu-item-40")
shop.click()
Basket = driver.find_element_by_css_selector(".post-182 > a[rel]")
Basket.click()
time.sleep(5)
Item = driver.find_element_by_class_name("cartcontents")
Item_get_text = Item.text
print(Item_get_text)
assert Item_get_text == "1 Item"
time.sleep(3)
price = driver.find_element_by_css_selector(".wpmenucart-contents>.amount")
price_get_text = price.text
assert price_get_text == "₹180.00"
print("Стоимость равна 180 р.")
Basket2 = driver.find_element_by_class_name("wpmenucart-contents")
Basket2.click()
Subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']>span"), "₹180.00"))
Total = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong>span"), "₹183.60"))

driver.quit()