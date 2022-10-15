from background import download_yt_videos, is_yt
from get_screenshots import is_reddit, reddit_scrapper
from speech import text_to_mp3
from video_maker import create_video
from trimmer import trim_vid
from cleanup import cleanup


def run():
    
    yt = ""
    start_time= 0
    end_time = 0
    reddit= ""

    while(not is_yt(yt)):
        yt=input("Enter the link of the background you want to use below(youtube only):")
    download_yt_videos(yt)

    while(end_time<=start_time):
        print("Make sure that the end time is greater than the start time")
        a=input("At what time do you want the video to start (in seconds):\n")
        b = input("At what time do you want the video to end (in seconds):\n")
        start_time = int(a)
        end_time = int(b)
    trim_vid(int(start_time),int(end_time))
    
    while(not is_reddit(reddit)):
        reddit= input("Enter the link of the reddit post you want to use:\n")
    reddit_obj= reddit_scrapper(reddit)

    audios=text_to_mp3(reddit_obj)
    create_video(audios)
    cleanup()


if __name__== "__main__":
    run()