from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def pythontest():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(by=By.NAME, value="q")
    elem.clear()
   
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source

    eleme = driver.find_element(by=By.NAME, value="q")
    eleme.clear()
    eleme.send_keys("pycon")
    eleme.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source

    elemen = driver.find_element(by=By.NAME, value="q")
    elemen.clear()
    elemen.send_keys("pycon")
    elemen.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
   
    

pythontest()
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/samir/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(by=By.NAME, value="q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
'''