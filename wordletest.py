import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def greater_length():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title
    e = driver.find_element(By.CLASS_NAME, "text-xl")
    e.clear()
    time.sleep(15)
    e.send_keys("xkhfgkv,kgkftekyjhrsdtfxcg,jhvfvjygfhjtredrgrfrsersdtfgjv,hhdxfngv")
    e.send_keys(Keys.RETURN)
    assert "Word not found"  in driver.page_source
    

    el = driver.find_element(By.CLASS_NAME, "text-xl")
    el.clear()   
    time.sleep(15)
    el.send_keys("CLOCK$")
    el.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    

    driver.close()



def lower_length():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title

    el = driver.find_element(By.CLASS_NAME, "text-xl")
    el.clear()
    el.send_keys("P")
    el.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    el.clear()

    ele = driver.find_element(By.CLASS_NAME, "text-xl")
    ele.clear()
    ele.send_keys("PY")
    ele.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    ele.clear()

    elem = driver.find_element(By.CLASS_NAME, "text-xl")
    elem.clear()
    elem.send_keys("PYC")
    elem.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    driver.close()

    eleme = driver.find_element(By.CLASS_NAME, "text-xl")
    eleme.clear()
    eleme.send_keys("CONE")
    eleme.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    eleme.clear()


    elemen = driver.find_element(By.CLASS_NAME, "text-xl")
    elemen.clear()
    elemen.send_keys("T")
    elemen.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    elemen.clear()

    element = driver.find_element(By.CLASS_NAME, "text-xl")
    element.clear()
    element.send_keys("TAY")
    element.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    element.clear()

    l = driver.find_element(By.CLASS_NAME, "text-xl")
    l.clear()
    l.send_keys("TAYE")
    l.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    l.clear()

    le = driver.find_element(By.CLASS_NAME, "text-xl")
    le.clear()
    le.send_keys("CON")
    le.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    le.clear()

    lem = driver.find_element(By.CLASS_NAME, "text-xl")
    lem.clear()
    lem.send_keys("LPT2")
    lem.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    lem.clear()

    leme = driver.find_element(By.CLASS_NAME, "text-xl")
    leme.clear()
    leme.send_keys("NIL")
    leme.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    leme.clear()

    lemen = driver.find_element(By.CLASS_NAME, "text-xl")
    lemen.clear()
    lemen.send_keys("NaN")
    lemen.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    lemen.clear()


def special_characters():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title

    el = driver.find_element(By.CLASS_NAME, "text-xl")
    el.clear()
    el.send_keys("    ")
    el.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    el.clear()

    ele = driver.find_element(By.CLASS_NAME, "text-xl")
    ele.clear()
    ele.send_keys("Dima&")
    ele.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    ele.clear()

    elem = driver.find_element(By.CLASS_NAME, "text-xl")
    elem.clear()
    elem.send_keys("*****")
    elem.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    driver.close()

    eleme = driver.find_element(By.CLASS_NAME, "text-xl")
    eleme.clear()
    eleme.send_keys("MOU&&")
    eleme.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    eleme.clear()


    elemen = driver.find_element(By.CLASS_NAME, "text-xl")
    elemen.clear()
    elemen.send_keys("1E02")
    elemen.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    elemen.clear()

    element = driver.find_element(By.CLASS_NAME, "text-xl")
    element.clear()
    element.send_keys("1E+02")
    element.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    element.clear()



def special_cases():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title

    el = driver.find_element(By.CLASS_NAME, "text-xl")
    el.clear()
    el.send_keys("NULL")
    el.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    el.clear()

    ele = driver.find_element(By.CLASS_NAME, "text-xl")
    ele.clear()
    ele.send_keys("UNDEF")
    ele.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    ele.clear()

    elem = driver.find_element(By.CLASS_NAME, "text-xl")
    elem.clear()
    elem.send_keys("LPT1")
    elem.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    elem.clear()

    eleme = driver.find_element(By.CLASS_NAME, "text-xl")
    eleme.clear()
    eleme.send_keys("COM1")
    eleme.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    eleme.clear()

    elemen = driver.find_element(By.CLASS_NAME, "text-xl")
    elemen.clear()
    elemen.send_keys("FILE:")
    elemen.send_keys(Keys.RETURN)
    assert "Word not found"  in driver.page_source
    elemen.clear

    element = driver.find_element(By.CLASS_NAME, "text-xl")
    element.clear()
    element.send_keys("FALSE")
    element.send_keys(Keys.RETURN)
    assert "Not enough letters" not in driver.page_source
    element.clear()

    l = driver.find_element(By.CLASS_NAME, "text-xl")
    l.clear()
    l.send_keys("TRUE")
    l.send_keys(Keys.RETURN)
    assert "Not enough letters" in driver.page_source
    l.clear()

    le = driver.find_element(By.CLASS_NAME, "text-xl")
    le.clear()
    le.send_keys("$USER")
    le.send_keys(Keys.RETURN)
    assert "Word not found" in driver.page_source
    le.clear()

    lem = driver.find_element(By.CLASS_NAME, "text-xl")
    lem.clear()
    lem.send_keys("NONE")
    lem.send_keys(Keys.RETURN)
    assert "Not enough letters"  in driver.page_source
    lem.clear()

    leme= driver.find_element(By.CLASS_NAME, "text-xl")
    leme.clear()
    leme.send_keys("INF")
    leme.send_keys(Keys.RETURN)
    assert "Not enough letters"  in driver.page_source
    leme.clear()

    lement = driver.find_element(By.CLASS_NAME, "text-xl")
    lement.clear()
    lement.send_keys("ERROR")
    lement.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    lement.clear()

    driver.close()
def invalid_words():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title

    el = driver.find_element(By.CLASS_NAME, "text-xl")
    el.clear()

    el.send_keys("PYCON")
    el.send_keys(Keys.RETURN)
    assert "Word not found" in driver.page_source
    el.clear()

    ele = driver.find_element(By.CLASS_NAME, "text-xl")
    ele.clear()
    ele.send_keys("PYTON")
    ele.send_keys(Keys.RETURN)
    assert "Word not found" in driver.page_source
    ele.clear()

    elem= driver.find_element(By.CLASS_NAME, "text-xl")
    elem.clear()
    elem.send_keys("CONAR")
    elem.send_keys(Keys.RETURN)
    assert "Word not found" in driver.page_source
    elem.clear()

    eleme = driver.find_element(By.CLASS_NAME, "text-xl")
    eleme.clear()
    eleme.send_keys("INLAW")
    elem.send_keys(Keys.RETURN)
    assert "Word not found" in driver.page_source
    elem.clear()

def valid_words():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://reactle.vercel.app/")
    assert "Reactle" in driver.title

    el = driver.find_element(By.CLASS_NAME, "text-xl")
    el.clear()

    el.send_keys("REACT")
    el.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    el.clear()

    ele = driver.find_element(By.CLASS_NAME, "text-xl")
    ele.clear()
    ele.send_keys("DRIVE"),
    ele.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    ele.clear()

    elem = driver.find_element(By.CLASS_NAME, "text-xl")
    elem.clear()
    elem.send_keys("WROTE")
    elem.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    elem.clear()

    eleme = driver.find_element(By.CLASS_NAME, "text-xl")
    eleme.clear()
    eleme.send_keys("COUNT")
    eleme.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    eleme.clear()

    elemen = driver.find_element(By.CLASS_NAME, "text-xl")
    elemen.clear()
    elemen.send_keys("CO-OP")
    elemen.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
   
    element = driver.find_element(By.CLASS_NAME, "text-xl")
    element.clear()
    element.send_keys("HAUSA")
    element.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    element.clear()

    l = driver.find_element(By.CLASS_NAME, "text-xl")
    l.clear()
    l.send_keys("EKARO")
    l.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    l.clear()

    le = driver.find_element(By.CLASS_NAME, "text-xl")
    le.clear()
    time.sleep(5)
    le.send_keys("ACTOR")
    le.send_keys(Keys.RETURN)
    assert "Not enough letters" not in driver.page_source
    le.clear()

    lem = driver.find_element(By.CLASS_NAME, "text-xl")
    lem.clear()
    lem.send_keys("DIVER")
    lem.send_keys(Keys.RETURN)
    assert "Not enough letters" not in driver.page_source
    lem.clear()

    leme = driver.find_element(By.CLASS_NAME, "text-xl")
    leme.clear()
    leme.send_keys("WRITE")
    leme.send_keys(Keys.RETURN)
    assert "Not enough letters" not in driver.page_source
    leme.clear()

    lemen = driver.find_element(By.CLASS_NAME, "text-xl")
    lemen.clear()
    lemen.send_keys("MOUNT")
    lemen.send_keys(Keys.RETURN)
    assert "Not enough letters" not in driver.page_source
    lemen.clear()

    lement = driver.find_element(By.CLASS_NAME, "text-xl")
    lement.clear()
    lement.send_keys("RULER")
    lement.send_keys(Keys.RETURN)
    assert "Not enough letters" not in driver.page_source
    lement.clear()

    eme = driver.find_element(By.CLASS_NAME, "text-xl")
    eme.clear()
    eme.send_keys("TONER")
    eme.send_keys(Keys.RETURN)
    assert "Not enough letters" not in driver.page_source
    eme.clear()

    emen = driver.find_element(By.CLASS_NAME, "text-xl")
    emen.clear()
    emen.send_keys("MOCHA")
    emen.send_keys(Keys.RETURN)
    assert "Word not found" not in driver.page_source
    emen.clear()

    ement = driver.find_element(By.CLASS_NAME, "text-xl")
    ement.clear()
    ement.send_keys("STRING")
    ement.send_keys(Keys.RETURN)
    assert "Word not found" not  in driver.page_source
    driver.close()


    m = driver.find_element(By.CLASS_NAME, "text-xl")
    m.clear()
    m.send_keys("CLOCK")
    m.send_keys(Keys.RETURN)
    assert "Not enough letters" not in driver.page_source
    m.clear()


greater_length()








