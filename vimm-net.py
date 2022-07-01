import time
from bs4 import BeautifulSoup
import requests
import string
import glob
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
browser = Firefox()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
URL = "https://vimm.net"
browser.get(URL)
input("are you ready")
def seekanddestroy(url2):
    for i in string.ascii_lowercase:
        realurl = url2+i
        print("-" * 50)
        print(realurl)
        page = requests.get(realurl, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        evens = soup.findAll(class_="even")
        odds = soup.findAll(class_="odd")
        list = [*odds, *evens]
        for x in list:
            clean = str(x.findChild().findChild())
            try:
                finalurl = URL+clean[9:clean.index('" onmouseover=')]
            except ValueError:
                finalurl = URL+clean[9:clean.index('">')]
            browser.get(finalurl)
            tits = browser.find_element(By.CSS_SELECTOR, "h2.mainContent > span:nth-child(3)").text
            print(f"{finalurl} - {tits}")

            # download
            try:
                browser.find_element(By.CSS_SELECTOR, "#download_form").click()
                #donation dialog
                browser.find_element(By.CSS_SELECTOR, "#tooltip4 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(2) > input:nth-child(1)").click()
                time.sleep(3)
            except Exception as e:
                print(f"something went wrong: {e}")
                pass

            # checking files
            while len(glob.glob("/home/riddle/Downloads/*.txt")) > 0:
                print(f"partial files found")
                time.sleep(15)

seekanddestroy("https://vimm.net/vault/GBC/")
