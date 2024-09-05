from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id("menu-item-40")
shop.click()
HTML5_Forms = driver.find_element_by_class_name("post-181")
HTML5_Forms.click()

element = driver.find_element_by_css_selector(".summary > h1")

element_get_text = element.text
assert "HTML5 Forms" in element_get_text

print("Заголовок книги называется: 'HTML5 Forms'")

driver.quit()