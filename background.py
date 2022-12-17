from pytube import YouTube

def is_yt(url):
    if ('youtube' in url) or ('you.tube' in url):
        return True
    return False

def on_progress(stream, chunk, bytes_remaining):
    print("Downloading...")

def on_complete(stream, file_path):
    print("Download Complete")

def download_yt_videos(url: str):
    try:
        
        yt= YouTube(url,
                    on_progress_callback=on_progress,
                    on_complete_callback=on_complete,
                    )
    except: 
        print("the url is not working")
    mp4_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    try:
        # print(mp4_video.get_file_path())
        mp4_video.download("./assets/downloaded_videos","main_video.mp4")# it downloads it here
        

       
    except:
        print("it could not download this")


# if __name__ == "__main__":
    
#     download_yt_videos("https://www.youtube.com/watch?v=n_Dv4JMiwK8")https://www.reddit.com/r/csMajors/comments/y3nie5/that_was_fast/
#https://www.youtube.com/watch?v=qGa9kWREOnE
