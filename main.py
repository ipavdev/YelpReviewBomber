from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from os import system
import random
import requests
import string
import json
import os
import openai
import imaplib
import email
from email.header import decode_header
import time
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_exists_by_xpath(xpath):
    try:
       driver.find_element(By.XPATH, xpath)
    except:
        return False
    return True


def is_english(s):
    english_letters = string.ascii_letters
    for c in s:
        if c not in english_letters:
            return False
    return True

while True:
    PROXY = ""

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)


    with webdriver.Chrome(chrome_options=chrome_options) as driver: 
        los_angeles_zip_codes = [90001, 90002, 90003, 90004, 90005, 90006, 90007, 90008, 90010, 90011, 90012, 90013, 90014, 90015, 90016, 90017, 90018, 90019, 90020, 90021, 90022, 90023, 90024, 90025, 90026, 90027, 90028, 90029, 90031, 90032, 90033, 90034, 90035, 90036, 90037, 90038, 90039, 90040, 90041, 90042, 90043, 90044, 90045, 90046, 90047, 90048, 90049, 90056, 90057, 90058, 90059, 90061, 90062, 90063, 90064, 90065, 90066, 90067, 90068, 90069, 90071, 90077, 90079, 90089, 90090, 90094, 90095, 90272, 90290, 90291, 90292, 90293, 90401, 90402, 90403, 90404, 90405, 90501, 90502, 90710, 90717, 90731, 90732, 90744, 90745, 90810, 90813, 91030, 91040, 91042, 91105, 91201, 91202, 91203, 91204, 91205, 91206, 91207, 91208, 91210, 91214, 91303, 91304, 91306, 91311, 91316, 91324, 91325, 91326, 91330, 91331, 91335, 91340, 91342, 91343, 91344, 91345, 91352, 91356, 91364, 91367, 91371, 91401, 91402, 91403, 91405, 91406, 91411, 91423, 91436, 91501, 91502, 91504, 91505, 91506, 91601, 91602, 91604, 91605, 91606, 91607]
        driver.get('https://www.yelp.com/signup?return_url=https://google.com')
        resp = requests.get("https://randomuser.me/api/").text
        js = json.loads(resp)

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
        )


        firstname_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="first_name"]'))
        )

        lastname_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="last_name"]'))
        )

        zipcode_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="zip"]'))
        )

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )

        birthday = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/form/div[2]/div/fieldset/ul/li[1]/select/option[{random.randint(2,11)}]'))
        )

        birthmonth = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/form/div[2]/div/fieldset/ul/li[2]/select/option[{random.randint(1,28)}]'))
        )

        birthyear = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/form/div[2]/div/fieldset/ul/li[3]/select/option[{random.randint(20,68)}]'))
        )


        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="signup-button"]'))
        )

        email_input.send_keys(str(random.randint(100, 10000)) + "@gmail.com") #I recomend getting a domain and setting up emails to redirect to 1 email for this
        
        if(is_english(js["results"][0]["name"]["first"]) == False):
            continue
        firstname_input.send_keys(js["results"][0]["name"]["first"])
        
        if(is_english(js["results"][0]["name"]["last"]) == False):
            continue
        lastname_input.send_keys(js["results"][0]["name"]["last"])
        
        zipcode_input.send_keys(los_angeles_zip_codes[random.randint(1, len(los_angeles_zip_codes))])
        
        birthday.click()
        
        birthmonth.click()
        
        birthyear.click()
        
        password_input.send_keys(generate_password(15))
        
        login_button.click()
        time.sleep(2)
        driver.get("https://www.yelp.com/biz/") #enter the yelp page
        
        writeareview = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[2]/div[1]/a'))
        )
        writeareview.click()

        time.sleep(10)
        stars = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/yelp-react-root/div/div/div/div/div/main/div/div[2]/form/div[1]/div/div[1]/div[1]/fieldset/ul/li[1]/div[1]/input'))
        )
        stars.click()

        reviewmessage = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/yelp-react-root/div/div/div/div/div/main/div/div[2]/form/div[1]/div/div[2]/div[1]/p'))
        )

        openai.api_key = "" #open ai key

        # set up the GPT-3 engine
        engine = "text-davinci-002"

        #prompt for the review
        prompt = (
            "Q: Generate a fake bad Yelp review\nA:"
        )


        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1004,
            temperature=0.7,
            n=1
        )
       
        reviewmessage.send_keys(response.choices[0].text)

        
        # Wait for 2 seconds before checking again
        time.sleep(2)




        submitreview = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/yelp-react-root/div/div/div/div/div/main/div/div[2]/form/div[2]/button'))
        )
        submitreview.click()


        
        for j in range(10):
            
            time.sleep(1)
        IMAP_SERVER = 'imap.gmail.com'
        IMAP_PORT = 993

        # Login credentials
        USERNAME = ''
        PASSWORD = ''

        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

        mail.login(USERNAME, PASSWORD)

        mail.select('inbox')


        status, email_ids = mail.search(None, 'ALL')
        latest_email_id = email_ids[0].split()[-1]

        _, data = mail.fetch(latest_email_id, '(RFC822)')

        message = email.message_from_bytes(data[0][1])

        sender = decode_header(message['From'])[0][0]
        subject = decode_header(message['Subject'])[0][0]
        date = decode_header(message['Date'])[0][0]

        if 'Please confirm your email' in subject:
            if sender == 'Yelp <no-reply@yelp.com>':
                html_content = None
                for part in message.walk():
                    content_type = part.get_content_type()
                    if 'text/html' in content_type:
                        html_content = part.get_payload(decode=True).decode('utf-8')
                        break
            if html_content:
                for line in html_content.splitlines():
                    if 'email_confirm_v2' and 'track.gif' in line:
                        driver.get(str(line.strip().replace("<img src=\"", "").split('"')[0]))

                    if 'email_confirm_v2' and '<link itemprop="target" href="https://www.yelp.com/ce' in line:
                        driver.get(line.strip().replace("<link itemprop=\"target\" href=\"", "").replace("\">", ""))
    time.sleep(10800)
