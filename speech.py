#credits https://github.com/elebumm/RedditVideoMakerBot/issues?page=1&q=is%3Aissue+is%3Aopen

import re
from gtts import gTTS
from get_screenshots import reddit_scrapper
from mutagen.mp3 import MP3


lang='en'

def text_to_mp3(data):
    speech_per_comment={}
    i=0
    length=0
    for text in data.values():
        if length>60:
            break
        myobj = gTTS( text = sanitize_text(text), lang=lang, slow=False)
        myobj.save(f"./assets/speeches/welcome{i}.mp3")
        audio = MP3(f"./assets/speeches/welcome{i}.mp3")
        length = int(audio.info.length)        
        speech_per_comment[i]=(length,f"./assets/speeches/welcome{i}.mp3")
        # print(speech_per_comment.get(i)[0])
        i+=1

    return speech_per_comment


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