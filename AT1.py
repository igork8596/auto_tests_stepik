"""
import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
"""

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/simple_form_find_task.html')
    text1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(1) > input')
    text1.send_keys('Игорь')
    text2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(2) > input')
    text2.send_keys('Кузьминов')
    text3 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(3) > input')
    text3.send_keys('Москва')
    text4 = browser.find_element(By.CSS_SELECTOR, '#country')
    text4.send_keys('РФ')
    button = browser.find_element(By.CSS_SELECTOR, '#submit_button')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
"""

"""
from time import sleep
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

x = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = 'http://suninjuly.github.io/find_link_text'
try:
    browser = webdriver.Chrome()
    sleep(1)
    browser.get(link)
    sleep(1)
    find_link = browser.find_element(By.LINK_TEXT, x)
    find_link.click()
    text1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(1) > input')
    text1.send_keys('Игорь')
    text2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(2) > input')
    text2.send_keys('Кузьминов')
    text3 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(3) > input')
    text3.send_keys('Москва')
    text4 = browser.find_element(By.CSS_SELECTOR, '#country')
    text4.send_keys('РФ')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    sleep(30)
    browser.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
"""

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_xpath_form')
    text1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(1) > input')
    text1.send_keys('Игорь')
    text2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(2) > input')
    text2.send_keys('Кузьминов')
    text3 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div:nth-child(3) > input')
    text3.send_keys('Москва')
    text4 = browser.find_element(By.CSS_SELECTOR, '#country')
    text4.send_keys('РФ')
    button = browser.find_element(By.XPATH, '/html/body/div/form/div[6]/button[3]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.first_block > div.form-group.first_class > input').send_keys('Игорь')
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.first_block > div.form-group.second_class > input').send_keys('Кузьминов')
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.first_block > div.form-group.third_class > input').send_keys('123@mail.ru')

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    time.sleep(1)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(20)
    browser.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    time.sleep(1)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(20)
    browser.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    sum_x_y = int(x) + int(y)
    Select(browser.find_element(By.ID, 'dropdown')).select_by_visible_text(str(sum_x_y))
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(20)
    browser.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    time.sleep(1)
    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(20)
    browser.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(2)').send_keys('Name')
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(4)').send_keys('Last name')
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(6)').send_keys('email@mail.ru')
    #time.sleep(1)
    browser.find_element(By.ID, 'file').send_keys('D:\123.txt')
    time.sleep(10)
finally:
    browser.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(int(x)))
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(20)
    browser.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(int(x)))
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    sleep(20)
    browser.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    browser.implicitly_wait(20)
    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(int(x)))
    browser.find_element(By.ID, 'solve').click()
finally:
    sleep(20)
    browser.quit()
"""
