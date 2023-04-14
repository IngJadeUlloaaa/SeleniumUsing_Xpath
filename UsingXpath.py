import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')

    def test_searchXpath(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(5)
        searchXpath = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        searchXpath.send_keys('Hola Mundo!', Keys.ARROW_DOWN)
        time.sleep(3)
        searchXpath.send_keys(Keys.ENTER)

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()
