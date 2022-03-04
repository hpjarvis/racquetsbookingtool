import requests
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

password_txt = open('password.txt', 'r').read().strip()
login = {"ctl00$MainContent$InputLogin": "harvey.jarvis@warwick.ac.uk", "ctl00$MainContent$InputPassword": password_txt}

data = {
    
}

with requests.Session() as s:
    r = s.get("https://sportwarwick.leisurecloud.net/Connect/mrmlogin.aspx")
    p = s.post("https://sportwarwick.leisurecloud.net/Connect/mrmlogin.aspx", data=data)
    r = s.get("https://sportwarwick.leisurecloud.net/Connect/memberHomePage.aspx")
    print(p.text)



# from selenium import webdriver
# import time

# driver = webdriver.Chrome("chromedriver.exe")
# driver.get('https://sportwarwick.leisurecloud.net/Connect/mrmlogin.aspx')

# password_txt = open('password.txt', 'r').read().strip()
# time.sleep(0.1)

# username = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[1]/div/input[1]')
# username.send_keys("harvey.jarvis@warwick.ac.uk")

# password = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[1]/div/input[2]')
# password.send_keys(password_txt)

# submit = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[1]/div/input[3]')
# submit.click()

# time.sleep(0.2)

# # navigate to the badminton booking page
# driver.get('https://sportwarwick.leisurecloud.net/Connect/mrmselectActivityGroup.aspx')
# driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div/div[2]/div/div[11]/div[1]/input').click()
# driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div/div[2]/div/div[1]/div[1]/input').click()
# driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div/section/div/div/div[1]/div[2]/div[1]/table/tbody/tr[17]/td[5]/span/input').click()

# time.sleep(5)
# driver.find_element_by_xpath('/html/body/form/div[3]/header/div[1]/div/div/div[2]/div/a[3]').click()
# exit()