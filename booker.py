from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import timeit
import time
import schedule

def book_badminton(zone, court_1, court_2, target_time):
    # get the ascii of the zone and convert it to multipler
    # i.e. Zone B has an offset of 4 because zone A is always an element
    multiplier = ord(zone) - 65
    # Find the correct buttons for the target courts
    button_no_1 = multiplier * 4 + int(court_1)
    button_no_2 = multiplier * 4 + int(court_1)
    print(button_no_1)
    print(button_no_2)
    # get the elements for both time slots
    link_1 = driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/input".format(target_time , button_no_1))
    link_2 = driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/input".format(target_time , button_no_2))
    # Open both links for booking court in a new tab
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .click(link_1) \
        .key_up(Keys.CONTROL) \
        .perform()

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div/div[2]/input[1]").click()
    time.sleep(1)
    driver.close()
    print("BOOKED {} {}".format(zone, court_1))

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])

    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .click(link_2) \
        .key_up(Keys.CONTROL) \
        .perform()

    time.sleep(0.5)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div/div[3]/input[1]").click()
    time.sleep(1)
    driver.close()
    print("BOOKED {} {}".format(zone, court_2))

    driver.switch_to.window(driver.window_handles[0])

def book_squash(court_1, court_2, target_time):
    link_1 = driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/input".format(target_time , court_1))
    link_2 = driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/input".format(target_time , court_2))

    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .click(link_1) \
        .key_up(Keys.CONTROL) \
        .perform()

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div/div[3]/input[1]").click()
    time.sleep(1)
    driver.close()
    print("BOOKED{}".format(court_1))

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])

    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .click(link_2) \
        .key_up(Keys.CONTROL) \
        .perform()

    time.sleep(0.5)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/input".format(target_time , court_2)).click()
    driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div/div[4]/input[1]").click()
    time.sleep(1)
    driver.close()
    print("BOOKED {}".format(court_2))

    driver.switch_to.window(driver.window_handles[0])

def job():
    print("Log in")
    driver.get('https://sportwarwick.leisurecloud.net/Connect/mrmlogin.aspx')

    txt = open('password.txt', 'r').read().strip().split('\n')
    time.sleep(0.1)

    username = driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[1]/div/input[1]')
    username.send_keys(txt[0])

    password = driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[1]/div/input[2]')
    password.send_keys(txt[1])

    submit = driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div[2]/section/div/div/div/div[2]/div[2]/div/div[1]/div/input[3]')
    submit.click()


    # navigate to the badminton booking page
    print("Looking for Badminton")
    driver.get('https://sportwarwick.leisurecloud.net/Connect/mrmselectActivityGroup.aspx')
    driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div/div[2]/div/div[11]/div[1]/input').click()
    driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div/div[2]/div/div[1]/div[1]/input').click()

    # click the time slot
    try:
        driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div/section/div/div/div[1]/div[2]/div[1]/table/tbody/tr[17]/td[8]/span/input').click()
    except:
        print('Badminton Not Available')
    else:
        time.sleep(5)

        # dict that holds avaliable courts in each zone.
        courts = {'A': [], 'B': [], 'C': [], 'D': []}

        # time 17 == 21:00
        target_time = "17"

        for i in range(1, 17):
            try:
                x = (driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/input".format(target_time ,i)).get_attribute('data-qa-id'))
            except:
                x = (driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]".format(target_time, i)).get_attribute('data-qa-id'))
            finally:
                if "Not Available" not in x:
                    court = re.search("Court=(Zone ([a-zA-Z]) Court (\d))", x)
                    courts[court.group(2)].append(court.group(3))
                

        badminton_zone_priority = ['D', 'A', 'C', 'B']

        for zone in badminton_zone_priority:
            if len(courts[zone]) != 0:
                if set(['1','2']).issubset(courts[zone]): 
                    print('Booking Zone: ' + zone + ' Courts: 1 & 2')
                    book_badminton(zone, '1', '2', target_time)
                    break

                elif set(['3','4']).issubset(courts[zone]):
                    print('Booking Zone: ' + zone + ' Courts: 3 & 4')
                    book_badminton(zone, '3', '4', target_time)
                    break

                elif set(['2','3']).issubset(courts[zone]):
                    print('Booking Zone: ' + zone + ' Courts: 2 & 3')
                    book_badminton(zone, '2', '3', target_time)
                    break

        else:
            print('Badminton Not Available')

    time.sleep(3)

    # navigate to the Squash booking page
    print('Looking for Squash')
    courts = []
    driver.get('https://sportwarwick.leisurecloud.net/Connect/mrmselectActivityGroup.aspx')
    driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div/div[2]/div/div[11]/div[1]/input').click()
    driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div/div[2]/div/div[3]/div[1]/input').click()
    target_time = "58"
    try:
        driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div/div/div/section/div/div/div[1]/div[2]/div[1]/table/tbody/tr[{}]/td[8]/span/input'.format(target_time)).click()
    except:
        print('Squash Not Avaliable')
    else:
        time.sleep(5)

        for i in range(1, 7):
            try:
                x = (driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]/input".format(target_time, i)).get_attribute('data-qa-id'))
            except:
                x = (driver.find_element(by=By.XPATH, value="/html/body/form/div[3]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/table/tbody/tr[{}]/td[{}]".format(target_time, i)).get_attribute('data-qa-id'))
            finally:
                if "Not Available" not in x:
                    court = re.search('Court (\d)', x)
                    courts.append(court.group(1))
        
        
        if len(courts) != 0:
            if set(['5','6']).issubset(courts): 
                print('Booking Courts: 5 & 6')
                book_squash('5', '6', target_time)

            elif set(['1','2']).issubset(courts):
                print('Booking Courts: 1 & 2')
                book_squash('1', '2', target_time)

            elif set(['3','4']).issubset(courts):
                print('Booking Courts: 3 & 4')
                book_squash('3', '4', target_time)

            elif set(['2','3']).issubset(courts):
                print('Booking Courts: 2 & 3')
                book_squash('2', '3', target_time)

            elif set(['4','5']).issubset(courts):
                print('Booking Courts: 4 & 5')
                book_squash('4', '5', target_time)
            
            else:
                print('Squash Not Available')


    # Logout after 5 seconds
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/header/div[1]/div/div/div[2]/div/a[3]').click()


if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print("RUNNING BOOKING TOOL")
    print('Starting - Waiting for wednesday @ 00:00')
    schedule.every().wednesday.at("00:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(10)