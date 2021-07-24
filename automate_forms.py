#! python3
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import random

fabric_xpath = {
    'cotton': '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[1]/label/div/div[1]',
    'wool':   '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[3]/label/div/div[1]',
    'linen':  '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[2]/label/div/div[1]'
}
chrome_drive_path = r"C:\Users\Nat\Downloads\Compressed\fonts\chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_argument('-incognito')
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScik3kYf8fmiDsm0F5p1GVtJ4aLl7Plv5zcYaDCcD1expmuAw/viewform?usp=sf_link'

names = 'nat theo aarron kwame kwaku akwasi peter osei mercy yaa akua serwaa john'.split()
i = 0
while i < 100:
    i += 1
    button_range = random.randint(0, 4)
    second_button = random.randint(5,9)
    name = random.choice(names)
    others_ans = random.choice(['None', 'no idea', 'none','..','??', '','_'])
    chosen_fabric = fabric_xpath[random.choice(['wool', 'cotton', 'linen'])]





    browser = webdriver.Chrome(executable_path=chrome_drive_path, options=option)
    browser.get(form_url)

    next_buttom = browser.find_element_by_class_name('appsMaterialWizButtonPaperbuttonLabel')
    next_buttom.click()

    time.sleep(3)
    textbox_class_name="quantumWizTextinputPaperinputInput"



    try:
        main = WebDriverWait(browser, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, textbox_class_name))
        )
        main.send_keys(name)
        radio_buttoms = browser.find_elements_by_class_name("docssharedWizToggleLabeledContainer")
        radio_buttoms[button_range].click()
        radio_buttoms[second_button].click()
        others = browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
        others.send_keys(others_ans)

        m_C =browser.find_element_by_xpath(chosen_fabric)
        m_C.click()

        print('*********')

        time.sleep(1)
        submit_buttom = browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
        submit_buttom.click()

        print('********* ' + i + ' items done ' )

    except:
        # browser.quit()
        pass

    browser.quit()

