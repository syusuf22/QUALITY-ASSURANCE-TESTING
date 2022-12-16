import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager




def chrometest():
    start = time.process_time()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title
    driver.close()
    end= time.process_time()


    return end-start

def Edgetest():
    start = time.process_time()
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title
    driver.close()
    end= time.process_time()

    return end-start

def Operatest():
    start = time.process_time()
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title
    driver.close()
    end= time.process_time()

    return end-start

def Firefoxtest():
    start = time.process_time()
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title
    driver.close()
    end= time.process_time()

    return end-start

def bravetest():
    start = time.process_time()
    driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title
    driver.close()
    end= time.process_time()

    return end-start




holder= {'Chrome':0, 'Edge':0,'Firefox':0, 'Brave':0}
holder['Chrome']+=chrometest()
holder['Edge'] +=Edgetest()
#holder['Opera'] +=Operatest()
holder['Firefox'] +=Firefoxtest()
holder['Brave']+= bravetest()
sorted_holder = sorted(holder.items(), key=lambda a:a[1])
print(sorted_holder)
