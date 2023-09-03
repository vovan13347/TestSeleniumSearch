

import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestSearchInput(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome(options)
    
    def test_search(self):
        driver = self.driver
        driver.get("http://www.google.com/")
        driver.find_element(By.NAME, "q").send_keys("Hello" + Keys.ENTER)
        time.sleep(5)
        driver.find_element(By.NAME, "q").send_keys("World" + Keys.ENTER)
        time.sleep(5)
        value = driver.find_element(By.NAME, "q")
        search_result = value.get_attribute("value")
        self.assertEqual(search_result, "HelloWorld")
        time.sleep(5)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
