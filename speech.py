#credits https://github.com/elebumm/RedditVideoMakerBot/issues?page=1&q=is%3Aissue+is%3Aopen

import re
from gtts import gTTS
from get_screenshots import reddit_scrapper


lang='en'


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

    # note: not removing apostrophes
    regex_expr = r"\s['|’]|['|’]\s|[\^_~@!&;#:\-–—%“”‘\"%\*/{}\[\]\(\)\\|<>=+]"
    result = re.sub(regex_expr, " ", result)
    result = result.replace("+", "plus").replace("&", "and")
    # remove extra whitespace
    return " ".join(result.split())

def text_to_mp3(url):
    texts = reddit_scrapper(url)
    content=''
    print(texts)
    for text in texts.values():
        content += ' '+ sanitize_text(text)
    
    print(content)    
    myobj = gTTS(text=content, lang=lang, slow=False)
  
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("./speeches/welcome.mp3")
    print("done")


# if __name__ == "__main__":
#     text_to_mp3("https://www.reddit.com/r/learnpython/comments/hly22a/automatically_screenshot_and_save_a_reddit_post/")