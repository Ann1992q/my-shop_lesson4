import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id("menu-item-40")
shop.click()

Book1 = driver.find_element_by_class_name("post-169")
Book1.click()
price_old = driver.find_element_by_css_selector(".price>del>span")
price_old_get_text = price_old.text # получили текст элемента с помощью .text
assert price_old_get_text == "₹600.00" # добавили проверку что содержимое равно ожидаемому
price_new = driver.find_element_by_css_selector(".price>ins>span")
price_new_get_text = price_new.text
assert price_new_get_text == "₹450.00"
b2 = driver.find_element_by_class_name("images")
time.sleep(3)
driver.execute_script("return arguments[0].scrollIntoView(true);", b2) # автоматически проскроллили до зоны видимости кнопки
time.sleep(3)
b2.click()
time.sleep(5)


btn1 = WebDriverWait(driver, 20).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))


btn1.click()

driver.quit()
