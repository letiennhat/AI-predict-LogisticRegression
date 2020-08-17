from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import time
#import return_dcom
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager
#from pyvirtualdisplay import Display

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
driver.get('http://autogame.xyz/thong-ke-tai-xiu-go.win.html')
#time.sleep(5)
wait(driver, 5).until(EC.alert_is_present())
alert = driver.switch_to_alert()
alert.accept()
time.sleep(5)
list_total = []
list_session = []
html_text = driver.page_source
html = BeautifulSoup(html_text, "lxml")

#for i in range(3175434,3175818):
for i in range(3175894,3176021):
    spans_newtotal = html.find_all('div', {'data-ses': f'{i}'})
    list_session.append(spans_newtotal[0].text.strip())
with open(f'data_test{time.localtime(time.time()).tm_mday}_{time.localtime(time.time()).tm_mon}.txt','w+') as f:
    f.write(str(list_session))

