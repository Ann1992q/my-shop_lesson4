import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id("menu-item-40")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
Basket1 = driver.find_element_by_css_selector(".post-182 > a[rel]")
Basket1.click()
time.sleep(5)
Basket2 = driver.find_element_by_css_selector(".post-180 > a[rel]")
Basket2.click()
Basket3 = driver.find_element_by_id("wpmenucartli")
Basket3.click()
time.sleep(5)
Delete = driver.find_element_by_css_selector(".remove[data-product_id='182']")
time.sleep(5)
Delete.click()
Undo = driver.find_element_by_link_text("Undo?")
Undo.click()
Quantity = driver.find_element_by_class_name("qty")
Quantity.clear()
Quantity.send_keys("3")

Update_basket = driver.find_element_by_css_selector("[name='update_cart']")
Update_basket.click()

Quantity_value = Quantity.get_attribute("value")
assert Quantity_value == "3"

time.sleep(5)
Apply_coupon = driver.find_element_by_css_selector("[value='Apply Coupon']")
Apply_coupon.click()

M = driver.find_element_by_class_name("woocommerce-error")
M_get_text = M.text
print(M_get_text)

driver.quit()



