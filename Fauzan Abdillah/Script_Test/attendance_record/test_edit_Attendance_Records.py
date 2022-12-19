import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestEditAttendanceRecords(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
    
    def test_edit(self):
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
        driver.find_element(By.XPATH,"(//span[@class='oxd-topbar-body-nav-tab-item'])[2]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//a[text()='Employee Records']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("paul")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@role='listbox']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(10)
        driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-pencil-fill']").click()
        time.sleep(10)
        driver.find_element(By.XPATH,"(//textarea[@placeholder='Type here'])[1]").send_keys(" edit")
        time.sleep(10)
        driver.find_element(By.XPATH,"(//textarea[@placeholder='Type here'])[2]").send_keys(" edit")
        time.sleep(10)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(10)
        

    def tearDown(self):
        self.driver.close()
       
if __name__ == "__main__":
    unittest.main()