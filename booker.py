from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re
import timeit
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://sportwarwick.leisurecloud.net/Connect/mrmlogin.aspx')

password_txt = open('password.txt', 'r').read().strip()
time.sleep(0.1)

username = driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[1]/div/input[1]')
username.send_keys('harvey.jarvis@warwick.ac.uk')

password = driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[1]/div/input[2]')
password.send_keys(password_txt)

submit = driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[1]/div/input[3]')
submit.click()

# navigate to the badminton booking page
driver.get('https://sportwarwick.leisurecloud.net/Connect/mrmselectActivityGroup.aspx')
driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div/div[2]/div/div[11]/div[1]/input').click()
driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div/div[2]/div/div[1]/div[1]/input').click()

# click the time slot
driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div/section/div/div/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[8]/span/input').click()
time.sleep(5)

# dict that holds avaliable courts in each zone.
courts = {'A': [], 'B': [], 'C': [], 'D': []}

for i in range(1, 17):
    try:
        x = (driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[5]/td[{}]/input".format(i)).get_attribute('data-qa-id'))
    except:
        x = (driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[5]/td[{}]".format(i)).get_attribute('data-qa-id'))
    finally:
        if "Not Available" not in x:
            court = re.search("Court=(Zone ([a-zA-Z]) Court (\d))", x)
            courts[court.group(2)].append(court.group(3))
        

print(courts)
# Logout after 5 seconds
time.sleep(5)
driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/header/div[1]/div/div/div[2]/div/a[3]').click()


'''
/html/body/form/div[3]/div/div/div/section/div/div/div[1]/div[2]/div[1]/table/tbody/tr[18]/td[2]

/html/body/form/div[3]/div/div/div/section/div/div/div[1]/div[2]/div[1]/table/tbody/tr[17]/td[7]

/html/body/form/div[3]/div/div/div/section/div/div/div[1]/div[2]/div[1]/table/tbody/tr[17]/td[8]
/html/body/form/div[3]/div/div/div/section/div/div/div[1]/div[2]/div[1]/table/tbody/tr[17]/td[8]
'''