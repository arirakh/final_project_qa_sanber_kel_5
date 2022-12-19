import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHapusDataVacancies(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
    
    def test_hapus(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(2)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//a[@class='oxd-main-menu-item'])[5]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//a[text()='Vacancies']").click()
        time.sleep(10)
        driver.find_element(By.XPATH,"(//i[@class='oxd-icon bi-trash'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[text()=' Yes, Delete ']").click()
        time.sleep(10)
        
       

    def tearDown(self):
        self.driver.close()
       
if __name__ == "__main__":
    unittest.main()