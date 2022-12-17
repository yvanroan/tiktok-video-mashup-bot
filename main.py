from background import download_yt_videos, is_yt
from get_data import reddit_scrapper
from speech import *
from video_maker import create_video
from image_maker import img_maker
from trimmer import trim_vid
from cleanup import cleanup
from check_duplicate import video_exist
from get_twitter import twitter_scrapper


def run():
    
    cleanup()
    yt = ""
    session_id=""
    start_time= 0
    end_time = 0

    while(not is_yt(yt)):
        yt=input("Enter the link of the background you want to use below(youtube only):\n")
    download_yt_videos(yt)

    while(end_time<=start_time):
        print("Make sure that the end time is greater than the start time")
        a=input("At what time do you want the video to start (in seconds):\n")
        b = input("At what time do you want the video to end (in seconds):\n")
        start_time = int(a)
        end_time = int(b)
    
    
    url= input("Enter the link of the post you want to use:\n")
    c = int(input("Enter 1 for Reddit and anything else for twitter:"))

    length_comment= int(input("Enter the number of comments/lenght of thread:\n"))
    speech= int(input("Enter your 1 for a text to speech using tiktoktts or 2 for pyttsx3:\n"))
    if speech==1:
        session_id= int("Enter your tiktok session id to use tiktoktts")

    voice=int(input("Enter 1 for male voice and 2 for female voice:"))

    if c==1:
        obj,subfolder= reddit_scrapper(url,length_comment)
        title=obj[0]
    else:
        obj=twitter_scrapper(url,length_comment)
        subfolder = 'twitter'
        title= obj[0]
    
    if not video_exist(subfolder,title):
        new_obj = img_maker(obj)
    
        duration = end_time - start_time
        
        if speech == 1:
            number_of_clip,audio_time = tiktok_text_to_mp3(new_obj,duration,voice,session_id)
        else:
            number_of_clip,audio_time = py_text_to_mp3(new_obj,duration,voice)

        min = int(audio_time/60)
        sec=int(audio_time - (min*60))

        print(f'the video will be {min}:{sec}\n')
        trim_vid(start_time,start_time+audio_time)
        create_video(number_of_clip,title,subfolder)
        cleanup()        

    


if __name__== "__main__":
    run()
