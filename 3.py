from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
import time
import pytest

def test_all_pets_presented():
    # Вводим e-mail:
    pytest.driver.find.elements_by_id('email').send_keys('rustam.s2012@gmail.com')
    # Вводим пароль:
    pytest.driver.find.elements_by_id('pass').send_keys('RUSTAM1997')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку, чтобы открыть страницу "Мои питомцы"
    pytest.driver.find_element_by_link_text('Мои питомцы').click
    # Сохраняем переменную
    statistics = pytest.driver.find_element_by_css_selector(".\\.col-sm-4.left")
    # Получаем информацию о питомцах
    number = statistics[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    # Находим питомцев на странице
    #pets = pytest.driver.find_element_by_css_selector('tbody > tr')
    pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody > tr')))
    #Сравниваем количество питомцев на странице с данными статистики
    for i in range(len(pets)):
        assert len(pets) == number