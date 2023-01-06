import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestFailedCreate(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_Create_Negatif(self): 
        driver = self.driver
        driver.get("https://en-gb.facebook.com/reg/") # open sites
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.NAME,"firstname").send_keys("My") # input firstname
        time.sleep(1)
        driver.find_element(By.NAME,"lastname").send_keys("Acccount") # input lastname
        time.sleep(1)
        driver.find_element(By.NAME,"reg_email__").send_keys("08123456789") # input mobile number/ email address
        time.sleep(1)
        driver.find_element(By.NAME,"reg_passwd__").send_keys("Testing1!") # input password
        time.sleep(1)
        driver.find_element(By.ID,"day").click() #click day dropdown
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='day']/option[20]").click() # click 20
        time.sleep(1)
        driver.find_element(By.ID,"month").click() #click month dropdown
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='month']/option[2]").click() #click February
        time.sleep(1)
        driver.find_element(By.ID,"year").click() #click year dropdown
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='year']/option[25]").click() #click 1999
        time.sleep(1)
        driver.find_element(By.NAME,"sex").click() #choose and click Female
        time.sleep(1)
        driver.find_element(By.NAME,"websubmit").click() #Click Sign In
        time.sleep(33)

        #validation
        assert driver.find_element(By.ID, "reg_error_inner") # appear alert "An error occurred. Please try again"
        time.sleep(2)
       

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
