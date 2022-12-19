import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TerminationReason(unittest.TestCase):

    def setUp(self):
      options = webdriver.ChromeOptions()
      options.add_experimental_option('excludeSwitches', ['enable-logging'])

      self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def test_akses_halaman_termination_reasons(self):
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
      
      menuPIM = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
      menuPIM.click()
      time.sleep(3)

      buttonConfiguration = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
      buttonConfiguration.click()
      time.sleep(1)

      menuTerminationReason = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[5]/a')
      menuTerminationReason.click()
      time.sleep(3)

      self.assertIn("Termination Reasons", driver.page_source)
    
    def test_akses_add_halaman_termination_reasons(self):
      driver = self.driver
      self.test_akses_halaman_termination_reasons()

      buttonAdd = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button')
      buttonAdd.click()
      time.sleep(5)

      self.assertIn('Add Termination Reason', driver.page_source)

    def test_tambah_data_termination_reason(self):
      driver = self.driver
      self.test_akses_add_halaman_termination_reasons()

      nameInput = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input')
      nameInput.clear()
      nameInput.send_keys('Test Termination Reason #1')
      time.sleep(1)

      buttonSubmit = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
      buttonSubmit.click()
      time.sleep(10)

      inputText = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[11]/div/div[2]/div')
      self.assertIn("Test Termination Reason #1", inputText)

    def test_tombol_cancel_add_termination_reason(self):
      driver = self.driver
      self.test_akses_add_halaman_termination_reasons()

      buttonCancel = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[1]')
      buttonCancel.click()
      time.sleep(10)

      self.assertIn("Termination Reasons", driver.page_source)

    def test_akses_halaman_edit_termination_reason(self):
      driver = self.driver
      self.test_akses_halaman_termination_reasons()

      buttonEdit = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[11]/div/div[3]/div/button[2]')
      buttonEdit.click()
      time.sleep(3)

      self.assertIn('Edit Termination Reason', driver.page_source)

    def test_memunculkan_modal_delete_termination_reason(self):
      driver = self.driver
      self.test_akses_halaman_termination_reasons()

      buttonDelete = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[10]/div/div[3]/div/button[1]')
      buttonDelete.click()
      time.sleep(3)

      titleConfirmation = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/div[1]/p')
      self.assertIn('Are you Sure?', titleConfirmation)

    def test_tombol_cancel_modal_delete_termination_reason(self):
      driver = self.driver
      self.test_akses_halaman_termination_reasons()

      buttonCancel = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/div[3]/button[1]')
      buttonCancel.click()
      time.sleep(3)

      self.assertIn('Termination Reasons', driver.page_source)

    def test_tombol_close_modal_delete_termination_reason(self):
      driver = self.driver
      self.test_akses_halaman_termination_reasons()

      buttonClose = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/button')
      buttonClose.click()
      time.sleep(3)

      self.assertIn('Termination Reasons', driver.page_source)

    def test_tombol_delete_muncul_saat_check_all(self):
      driver = self.driver
      self.test_akses_halaman_termination_reasons()

      checkboxAll = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div[1]/div/label/input')
      checkboxAll.click()

      self.assertIn('Delete Selected', driver.page_source)

    def tearDown(self):
      self.driver.close()

unittest.main()
