from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://jqueryui.com/resources/demos/progressbar/download.html')
driver.implicitly_wait(3)
my_element=driver.find_element(By.ID,"downloadButton")
my_element.click()
# progress_ele=driver.find_element(By.CLASS_NAME,"progress-label")
# print(f"{progress_ele.text=='Completed!'}")
WebDriverWait(driver,30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME,"progress-label"),
        'Complete!'
    )
)

