# python -m pytest -v --driver Chrome --driver-path B:/PyCharm/chromedriver.exe
from selenium import webdriver
import time
import pytest

@pytest.fixture(autouse=True, scope="module")
def testing():
   pytest_driver = webdriver.Chrome('B:\\PyCharm\\chromedriver.exe')
   # Переходим на страницу авторизации
   pytest_driver.get('http://petfriends.skillfactory.ru/login)

   yield

   pytest_driver.quit()


def test_class():
//div[@class=".col-sm-4 left"]/text()[2]
//div[@class=".col-sm-4 left"]/h2/following-sibling::text()[1]

statistic_user = driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]')
assert str(len(list_my_pets)) in statistic_user.text

def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('rustam.s2012@gmail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('RUSTAM1997')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


   # Убедиться, что внутри каждого из элементов есть имя питомца, возраст и вид.
   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-body .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-body .card-text')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0