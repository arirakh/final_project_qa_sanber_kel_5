import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
      options = webdriver.ChromeOptions()
      options.add_experimental_option('excludeSwitches', ['enable-logging'])

      self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def test_login_orangeHRM(self):
      driver = self.driver
      
      driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
      driver.maximize_window()
      time.sleep(3)

      username = driver.find_element_by_name('username')
      username.clear()
      username.send_keys('Admin')
      time.sleep(1)

      password = driver.find_element_by_name('password')
      password.clear()
      password.send_keys('admin123')
      time.sleep(1)

      buttonSubmit = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
      buttonSubmit.submit()
      time.sleep(3)

      self.assertIn('OrangeHRM', driver.title)
      time.sleep(3)

unittest.main()
