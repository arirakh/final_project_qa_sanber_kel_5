import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAksesdanUbahDataContactDetails(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
    
    def test_aksesubah(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(2)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//a[@class='oxd-main-menu-item'])[6]").click()
        time.sleep(10)
        driver.find_element(By.XPATH,"//a[text()='Contact Details']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]").send_keys("Padang")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[4]/div/div[2]/input").send_keys("Sumatera Barat")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[5]/div/div[2]/input").send_keys("255086")
        time.sleep(5)
        driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[1]").send_keys("iiiiii")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@role='listbox']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[7]").send_keys("081377")
        time.sleep(5)
        driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[9]").send_keys("fch@example.com")
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(10)
       

    def tearDown(self):
        self.driver.close()
       
if __name__ == "__main__":
    unittest.main()