from selenium import webdriver
from selenium.webdriver.common.by import By

def Author (SearchVar):

    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Admin\darconf\chromedriver.exe')
    driver.get ("https://google.com/")
    assert 'Bing' in driver.title
    SearchBox = driver.find_element_by_name("q")
    SearchBox.send_keys(SearchVar)
    SearchBox.submit()
    At = driver.find_elements_by_css_selector ('#gs_res_ccl_mid > div:nth-child(1) > div.gs_ri > div.gs_a')
    for item in At:
    	print(item.text)
    wait = WebDriverWait(driver, 10)
        	
Author("darwoft")