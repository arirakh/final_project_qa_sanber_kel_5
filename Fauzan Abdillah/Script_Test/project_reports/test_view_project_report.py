import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestViewProjectReport(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
    
    def test_view(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(2)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//a[@class='oxd-main-menu-item'])[4]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//span[@class='oxd-topbar-body-nav-tab-item'])[3]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//a[text()='Project Reports']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("acme")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@role='listbox']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(10)
        
       

    def tearDown(self):
        self.driver.close()
       
if __name__ == "__main__":
    unittest.main()