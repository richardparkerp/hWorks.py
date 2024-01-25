from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


service = Service(ChromeDriverManager().install())
option = Options()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option,
                          service=service)

driver.get("https://weathershopper.pythonanywhere.com")

temp=driver.find_element(By.ID,"temperature")
arr=temp.text.split(' ')
print(arr[0])

if int(arr[0])<19:
    print(int(arr[0]))
    # btn_moisturizers=driver.find_element(By.CLASS_NAME,"btn btn-primary")
    btn_moisturizers = driver.find_element(By.LINK_TEXT, "Buy moisturizers")
    btn_moisturizers.click()



elif int(arr[0])>34:
    btn_sunscreens = driver.find_element(By.LINK_TEXT, "Buy sunscreens")
    btn_sunscreens.click()

