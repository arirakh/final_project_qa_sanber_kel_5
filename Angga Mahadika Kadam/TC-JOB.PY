import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
    
    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(2)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//a[@class='oxd-main-menu-item active'])[6]").click()
        time.sleep(5)
       
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
       
if __name__ == "__main__":
    unittest.main()
