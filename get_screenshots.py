## useful resources
##https://selenium-python.readthedocs.io/waits.html

# credits
#  https://stackoverflow.com/questions/73214339/reddit-isnt-scraping-the-top-comments-python-
#  https://stackoverflow.com/a/57630350

import time, string
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data={}

def reddit_scrapper(url):

    # chrome_options = Options()
    # chrome_options.add_argument("--no-sandbox")

    # webdriver_service = Service("chromedriver/chromedriver") # path to where you saved chromedriver binary
    browser = webdriver.Chrome(ChromeDriverManager().install())

    try:
        # Load cookies to prevent cookie overlay & other issues
        # browser.get('www.reddit.com')
        # for cookie in config['reddit_cookies'].split('; '):
        #     cookie_data = cookie.split('=')
        #     browser.add_cookie({'name':cookie_data[0],'value':cookie_data[1],'domain':'reddit.com'})
        browser.get(url)

        # Fetching the post itself, text & screenshot
        post = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.Post')))
        post_text = post.find_element(By.CSS_SELECTOR, 'h1').text
        post_desc = post.find_element(By.CSS_SELECTOR, 'p').text
        data['0'] = post_text + " " + post_desc
        post.screenshot('downloaded_screenshot/0.png')

        # Let comments load
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

        # Fetching comments & top level comment determinator
        comments = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[id^=t1_][tabindex]')))
        #the code above fetches elements with div id starting with "t1_"
        allowed_style = comments[0].get_attribute("style")
        
        # Filter for top only comments
        NUMBER_OF_COMMENTS = 10
        all_comments = [comment for comment in comments if comment.get_attribute("style") == allowed_style]
        comments = all_comments[:NUMBER_OF_COMMENTS]

        print('💬 Scraping comments...',end="",flush=True)
        # Save time & resources by only fetching X content
        for i in range(len(comments)):
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
                comments[i].screenshot(f'downloaded_screenshot/{i+1}.png') # the f is for string interpolation
                data[str(i+1)] = ''.join(filter(lambda c: c in string.printable, text))
                #filter only allows text that are printable

            except Exception as e:
                raise 

        if browser.session_id:
            browser.quit()
        return data
    except Exception as e:
        if browser.session_id:
            browser.quit()
        raise # this is better than raise(e) because it trace the actual root of the issue

print(data)

if __name__ == "__main__":
    reddit_scrapper("https://www.reddit.com/r/learnpython/comments/hly22a/automatically_screenshot_and_save_a_reddit_post/")