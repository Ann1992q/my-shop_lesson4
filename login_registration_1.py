from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
My_Account = driver.find_element_by_link_text("My Account")
My_Account.click()

reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("liya77792@mail.ru")

password = driver.find_element_by_id("reg_password")
password.send_keys("liya77792liya77792")

register = driver.find_element_by_css_selector(".woocomerce-FormRow > input:nth-child(3)")
register.click()
driver.quit()
