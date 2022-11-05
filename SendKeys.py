from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get('https://web.archive.org/web/20180926132852/http://www.seleniumeasy.com:80/test/basic-first-form-demo.html')
sum1=driver.find_element(By.ID,"sum1")
sum2=driver.find_element(By.ID,"sum2")
sum1.send_keys(4555)
sum2.send_keys(657)
Gettotal=driver.find_element(By.CSS_SELECTOR,"button[onclick='return total()']")
Gettotal.click()
total=driver.find_element(By.ID,"displayvalue").text
print(total)
