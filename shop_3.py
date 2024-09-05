import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_id("menu-item-40")
shop.click()

#Default_sorting = driver.find_elements_by_css_selector("[value='menu_order']")
from selenium.webdriver.support.select import Select # импортируем класс Select или библиотеки webdriver
Default_sorting = driver.find_element_by_class_name("orderby")# "element" это просто название переменной, можно задать и другое

select = Select(Default_sorting) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
select.select_by_value("menu_order")# ищем элемент с текстом "Sales" ; в этом и предыдущем методе добавлять .click() не нужно
a = driver.find_element_by_css_selector("[value='menu_order']")
a_get_text = a.text # получили текст элемента с помощью .text
if a_get_text == "Default sorting": # добавили проверку что содержимое равно ожидаемому
    print("Выбрана сортировка по умолчанию")
else:
    print("Сортировка по умолчанию не выбрана")
select2 = Select(Default_sorting)
select2.select_by_value("price-desc")
Default_sorting = driver.find_element_by_class_name("orderby")
high_to_low = driver.find_element_by_css_selector("[value='price-desc']") # нашли элемент по составному селектору
high_to_low_selected = high_to_low.get_attribute("selected")
if high_to_low_selected is not None:
    print("в селекторе выбран вариант сортировки по цене от большей к меньшей")
else:
    print("в селекторе не выбран вариант сортировки по цене от большей к меньшей")




#select2 = Select(Ds) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
#select2.Select2_by_value("6") # ищем элемент с текстом "Sales" ; в этом и предыдущем методе добавлять .click() не нужно
#high_to_low = driver.find_element_by_css_selector("option:nth-child(6)")
#high_to_low.click()

driver.quit()



