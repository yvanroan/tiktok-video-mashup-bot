from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    print("Downloading...")

def on_complete(stream, file_path):
    print("Download Complete")

def download_yt_videos(url: str, outpath: str = "./"):
    try:
        yt= YouTube(url,
                    on_progress_callback=on_progress,
                    on_complete_callback=on_complete,
                    )
    except: 
        print("the url is not working")
    mp4_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    try:
        mp4_video.download(outpath)
    except:
        print("it could not download this")

#"https://www.youtube.com/watch?v=n_Dv4JMiwK8"
#"./downloaded_videos"

if __name__ == "__main__":
    
    download_yt_videos("https://www.youtube.com/watch?v=n_Dv4JMiwK8","./downloaded_videos")