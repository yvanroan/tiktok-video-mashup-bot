#credits https://github.com/elebumm/RedditVideoMakerBot/issues?page=1&q=is%3Aissue+is%3Aopen
#install pyttsx3 gtts mutagen 
# from get_screenshots import reddit_scrapper
from gtts import gTTS
import pyttsx3 
from mutagen.mp3 import MP3
from moviepy.editor import * 
from tiktok import tts
from image_maker import img_maker
from speedup import speed_up
from get_twitter import twitter_scrapper
# from cleanup import cleanup #take this out later



lang='en'
     
def gtts_text_to_mp3(data,duration: int):
    time=0
    i=0
    length=0

    for text in data.values():
        
        myobj = gTTS( text = text, lang=lang, slow=False)
        myobj.save(f"./assets/speeches/{i}.mp3")
        audio = MP3(f"./assets/speeches/{i}.mp3")
        length = audio.info.length
        time+=length
        print(f'{time}')
        i+=1

        if time>160 or time>duration:
            time-=length
            i-=1
            return i,time

def py_text_to_mp3(data ,duration: int ,voice: int):
    print("in")
    time=0
    i=0
    engine = pyttsx3.init() # object creation
    engine.setProperty('rate', 200) 
    engine.setProperty('volume',0.7)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    if voice!=1 or voice !=2:
        voice = 1
    
    engine.setProperty('voice', voices[voice].id)   #changing index, changes voices. 1 for female 0 for male
    
    for text in data.values():

        """Saving Voice to a file"""
        # On linux make sure that 'espeak' and 'ffmpeg' are installed
        engine.save_to_file(text, f'./assets/speeches/{i}.mp3')
        engine.runAndWait()
        length=AudioFileClip(f"assets/speeches/{i}.mp3").duration
        time+=length
        i+=1
        
        print(f'{time}')

        if time>160 or time>duration:
            time-=length
            i-=1
            print(f'{i},{time}')
    return i,time

        
def tiktok_text_to_mp3(data ,duration: int ,voice: int,session_id: str):

    i=0
    time=0
    length=0

    if voice==2:
            text_speaker= 'en_us_002'
    else:
        text_speaker= 'en_us_006'
    
    for text in data.values():
        tts(session_id, text_speaker, text, f'./assets/speeches/{i}.mp3')
        print(text)
        length=speed_up(f"assets/speeches/{i}.mp3")
        # length=AudioFileClip(f"assets/speeches/{i}.mp3").duration
        time+=length
        i+=1

        if time>200 or time>duration:
            time-=length
            i-=1

    return i,time

