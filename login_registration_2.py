from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
My_Account = driver.find_element_by_link_text("My Account")
My_Account.click()

username = driver.find_element_by_id("username")
username.send_keys("Liya77792@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("liya77792liya77792")
login = driver.find_element_by_css_selector("[value='Login']")
login.click()
Logout = driver.find_element_by_link_text("Logout")
Logout_get_text = Logout.text # получили текст элемента с помощью .text
#assert Logout_get_text == "Logout" # добавили проверку что содержимое равно ожидаемому

if Logout_get_text == "Logout":
    print("Слово есть на странице")
else:
    print("Слова на странице нет")



driver.quit()