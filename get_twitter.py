
import time, string
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# Set driver and initial array 



def twitter_scrapper(url,count):
    chrome_options = Options()
        
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument('window-size=2560,1440')
    chrome_options.add_argument("--disable-software-rasterizer")
    # chrome_options.headless = True

    browser = webdriver.Chrome(options = chrome_options, executable_path=r"./chrome_driver/chromedriver.exe")# will be deprecated soon 

    browser.get(url) #input the url you wanna scrappe here

    time.sleep(5) #change according to your pc and internet connection
        
    tweets = {}
    go=True
    i=0
    height= browser.execute_script("return document.body.scrollHeight") #1500
        #update all_tweets to keep loop
    all_tweets = browser.find_elements(By.XPATH, '//div[@data-testid]//article[@data-testid="tweet"]')

    for item in all_tweets: # skip tweet already scrapped
        print('--- text ---')
        try:
            text = item.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
            text = text.split('\n')
        except:
            text = '[empty]'
            
        print(text)
        #Append new tweets replies to tweet dic
        tweets[i]=text
        time.sleep(2)
        i+=1

    while go:
        
        # Scroll down to bottom
        browser.execute_script(f"window.scrollTo(0, {height});")
        # Wait to load page
        time.sleep(3)
        # Calculate new scroll height and compare with last scroll height
        
        #update all_tweets to keep loop
        all_tweets = browser.find_elements(By.XPATH, '//div[@data-testid]//article[@data-testid="tweet"]')

        for item in all_tweets: # skip tweet already scrapped
            print('--- text ---')
            try:
                text = item.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
                print(text)
                text = text.split('\n')
            except:
                text = '[empty]'
            print(text)
            tweets[i]=text
            time.sleep(2)
            if len(tweets)==count:
                go=False
                break

            i+=1
        
    browser.quit()
    print(tweets)
    data={}
    r=0
    for j in tweets.values():
        for k in j:
            if k=='':
                continue
            data[r]=sanitize_text(k)
            r+=1
    print(data)
    return data

def sanitize_text(text: str) -> str:
    r"""Sanitizes the text for tts.
        What gets removed:
     - following characters`^_~@!&;#:-%“”‘"%*/{}[]()\|<>?=+`
     - any http or https links

    Args:
        text (str): Text to be sanitized

    Returns:
        str: Sanitized text
    """
    # r in front of the strings means that it is a raw string, so all format are ignored(e.x: \n is not a newline)

    # remove any urls from the text
    regex_urls = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    
    
    result = re.sub(regex_urls, " ", text)
    result = re.sub('"','',result)
    result = re.sub('>','is greater than',result)
    result = re.sub('<','is less than',result)
    # note: not removing apostrophes
    regex_expr = r"\s['|’]|['|’]\s|[\^_~@!&;#\-–—“”‘\"\*/{}\[\]\(\)\\|<>=+]"  #removed :
    result = re.sub(regex_expr, " ", result)
    result = result.replace("+", "plus").replace("&", "and")
    # remove extra whitespace
    return " ".join(result.split())

