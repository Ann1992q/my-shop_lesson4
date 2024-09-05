from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id("menu-item-40")
shop.click()
HTML = driver.find_element_by_link_text("HTML")
HTML.click()

items_count = driver.find_elements_by_class_name("status-publish") # находим список всех элементов в корзине
# проверка что в корзине действительно 3 товара (добавьте в конец теста)
if len(items_count) == 3: # после 1-го урока можем теперь создать небольшую конструкцию для проверки кол-ва товаров
    print("Отображаются 3 товара") # len здесь посчитает количество элементов, найденных при помощи find_elements
else:
    print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))


driver.quit()