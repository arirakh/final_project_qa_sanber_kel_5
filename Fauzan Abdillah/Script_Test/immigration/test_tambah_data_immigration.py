import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestTambahDataImmigration(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
    
    def test_tambah(self):
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
        driver.find_element(By.XPATH,"//a[text()='Immigration']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='orangehrm-background-container']//div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/div[@class='orangehrm-action-header']/button[@type='button']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("01234")
        time.sleep(5)
        driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[1]").send_keys("2022-12-01")
        time.sleep(5)
        driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[2]").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[2]").send_keys("2022-12-10")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[2]/div/div[4]/div/div[2]/input").send_keys("abc")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").send_keys("iiiii")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@role='listbox']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']//textarea[@placeholder='Type Comments here']").send_keys("immigration baru")
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(10)
       

    def tearDown(self):
        self.driver.close()
       
if __name__ == "__main__":
    unittest.main()