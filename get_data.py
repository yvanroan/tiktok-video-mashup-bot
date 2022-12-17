## useful resources
##https://selenium-python.readthedocs.io/waits.html
#  https://stackoverflow.com/questions/73214339/reddit-isnt-scraping-the-top-comments-python-
#  https://stackoverflow.com/a/57630350
#  https://ethanchiu.xyz/blog/2017/12/16/extracting-subreddit-names-from-URLs/
#https://saucelabs.com/resources/articles/selenium-tips-css-selectors

import time, string
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

data={}


#create a function to test that the url is from reddit
def is_reddit(url):
    if ('reddit' in url):
        return True
    return False

def reddit_scrapper(url,number_of_comments):

    subreddit= url.split('/')[4]

    #new way
    chrome_options = Options()
    # chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.headless = True

    browser = webdriver.Chrome(options = chrome_options, executable_path=r"./chrome_driver/chromedriver.exe")# will be deprecated soon 

    try:
        # Load cookies to prevent cookie overlay & other issues
        # browser.get('www.reddit.com')
        # for cookie in config['reddit_cookies'].split('; '):
        #     cookie_data = cookie.split('=')
        #     browser.add_cookie({'name':cookie_data[0],'value':cookie_data[1],'domain':'reddit.com'})

        browser.get(url)
        

        #fetching the div for the title
        post_header= WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.Post h1'))) #> div:nth-child(1) > div:nth-child(4) > div 
        post = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.Post:nth-child(1) p'))) #> div:nth-child(1) > div:nth-child(4) > div 
        post_title = post_header[0].text
        
        post_title= sanitize_text(post_title)
        print(post_title)
        data[0] = post_title
        j=1

        print(len(post)-1)
        error=0

        while j+error<len(post):
            text=post[j+error].text
            text= sanitize_text(text)
            text=re.sub(r'\s+', ' ', text)
            if len(text) <= 1 or text == ' ':
                print("newline")
                error+=1
                continue
            
            else:
                print(f'{data[j-1]}\n')
                # time.sleep(1)
                # post_content[j+error-1].screenshot(f'./assets/downloaded_screenshot/{j}.png')                
                data[j]=text
                j+=1

        # Let comments load
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        if(number_of_comments>0):
            # Fetching comments & top level comment determinator
            comments = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[id^=t1_][tabindex]')))
            #the code above fetches elements with div id starting with "t1_"
            allowed_style = comments[0].get_attribute("style")
            
            # Filter for top only comments
            NUMBER_OF_COMMENTS = number_of_comments #turn it back to 10 after
            all_comments = [comment for comment in comments if comment.get_attribute("style") == allowed_style]
            comments = all_comments[:NUMBER_OF_COMMENTS]

            print('💬 Scraping comments...',end="",flush=True)
            # Save time & resources by only fetching X content
            for i in range(len(comments)):
                # print(comments[i])
                try:
                    print('.',end="",flush=True)

                    # Scrolling to the comment ensures that the profile picture loads
                    desired_y = (comments[i].size['height'] / 2) + comments[i].location['y']
                    window_h = browser.execute_script('return window.innerHeight')
                    window_y = browser.execute_script('return window.pageYOffset')
                    current_y = (window_h / 2) + window_y
                    scroll_y_by = desired_y - current_y

                    browser.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
                    time.sleep(1)
                    
                    # Getting comment into string
                    text = comments[i].find_element(By.CSS_SELECTOR,'.RichTextJSON-root').text

                    # Screenshot & save text
                    comments[i].screenshot(f'./assets/downloaded_screenshot/{i+j}.png') # the f is for string interpolation
                    data[i+j] = ''.join(filter(lambda c: c in string.printable, text))
                    # print(data[str(i+j)])
                    #filter only allows text that are printable

                except Exception as e:
                    raise 

        if browser.session_id:
            browser.quit()
        return data,subreddit
    except Exception as e:
        if browser.session_id:
            browser.quit()
        raise # this is better than raise(e) because it trace the actual root of the issue


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
    # note: not removing apostrophes
    regex_expr = r"\s['|’]|['|’]\s|[\^_~@!&;#:\-–—“”‘\"\*/{}\[\]\(\)\\|<>=+]"
    result = re.sub(regex_expr, " ", result)
    result = result.replace("+", "plus").replace("&", "and")
    # remove extra whitespace
    return " ".join(result.split())
