from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://chromedriver_win32//chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(15)
driver.maximize_window

driver.find_element_by_name("username").send_keys("Admin")
driver.find_element_by_name("password").send_keys("admin123")
driver.find_element_by_class("oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()