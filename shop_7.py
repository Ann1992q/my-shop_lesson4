import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id("menu-item-40")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")

Basket1 = driver.find_element_by_css_selector(".post-182 > a[rel]")

Basket1.click()
time.sleep(3)

Basket2 = driver.find_element_by_id("wpmenucartli")
time.sleep(3)

Basket2.click()
time.sleep(3)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Proceed_to_Checkout = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")) )
time.sleep(3)
Proceed_to_Checkout.click()
time.sleep(3)
First_name = driver.find_element_by_id("billing_first_name")
First_name.send_keys("Liya")
Last_name = driver.find_element_by_id("billing_last_name")
Last_name.send_keys("Lana")
Phone = driver.find_element_by_id("billing_phone")
Phone.send_keys("9116163219")
Email = driver.find_element_by_id("billing_email")
Email.send_keys("liya77792@mail.ru")
Country = driver.find_element_by_css_selector("#s2id_billing_country b")
Country.click()
time.sleep(5)

driver.execute_script("window.scrollBy(0, 300);")
Sel = driver.find_element_by_id("s2id_autogen1_search").send_keys("Alg")
time.sleep(3)
Algeria = driver.find_element_by_class_name("select2-match")
Algeria.click()
time.sleep(3)
Address = driver.find_element_by_css_selector("[placeholder='Street address']")
time.sleep(3)
Address.send_keys("Tokio City")
Town = driver.find_element_by_css_selector("input#billing_city")
Town.send_keys("Algeria")
Postcode = driver.find_element_by_css_selector("input#billing_postcode")
Postcode.send_keys("100-0000")
State = driver.find_element_by_css_selector(".input-text#billing_state")
State.send_keys("Alderia")

time.sleep(4)
Check_payments = driver.find_element_by_id("payment_method_cheque")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
Check_payments.click()

Place_order = driver.find_element_by_id("place_order")
Place_order.click()

time.sleep(5)


Thanks = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
Check_Payments = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method>strong"), "Check Payments"))

driver.quit()