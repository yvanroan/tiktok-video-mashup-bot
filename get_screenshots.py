from selenium import webdriver

driver = webdriver.Chrome()
#https://www.reddit.com/r/learnpython/comments/hly22a/automatically_screenshot_and_save_a_reddit_post/
driver.get('https://www.google.com')
driver.save_screenshot('screenshot.png')