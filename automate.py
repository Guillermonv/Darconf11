from selenium import webdriver
from selenium.webdriver.common.by import By

def Author (SearchVar):

    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Admin\darconf\chromedriver.exe')
    driver.get ("https://google.com/")
   
    assert 'Google' in driver.title
   
    SearchBox = driver.find_element_by_name("q")
    SearchBox.send_keys(SearchVar)
    SearchBox.submit()
  
    results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3') 
    results[0].click()
  
Author("darwoft")