#useful website
#https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html#videofileclip
#https://stackoverflow.com/questions/72914568/overlay-image-on-video-using-moviepy
#https://docs.python.org/3/library/multiprocessing.html

from moviepy.video.VideoClip import ImageClip
from moviepy.editor import VideoFileClip  
from moviepy.editor import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.editor import concatenate_videoclips

video_path = './assets/downloaded_videos/base_video_trim.mp4'

def create_video(audios):
    comments_speech = audios
    video= VideoFileClip(video_path).without_audio()
    start_time=0
    clips=[]
    for comment_number in range(len(comments_speech)):
        length = comments_speech.get(comment_number)[0]
        audio_clip = AudioFileClip(comments_speech.get(comment_number)[1])
        
        
        title = ImageClip(f"./assets/downloaded_screenshot/{comment_number}.png").set_start(0).set_duration(length).set_pos(("center","center"))
                #.resize(height=50) # if you need to resize...
        print(start_time,length)    
        video_clip=video.subclip(start_time,start_time+length)
        video_clip2=video_clip.set_audio(audio_clip)
        clips.append(CompositeVideoClip([video_clip2, title]))
        
        start_time+=length
        print(f"{comment_number+1}st done")

    final = concatenate_videoclips(clips).set_position("center")

    # final = Video(final).add_watermark(
    #     text="ThePaceMaker_yvanroan", opacity=0.4
    #  ) create a video class that will handle watermarks look at utils/video for reference
    final.write_videofile(
        "./result/test.mp4",
        fps=30,
        audio_codec="aac",
        audio_bitrate="192k",
        verbose=False,
        # threads=multiprocessing.cpu_count()#Return the number of CPUs in the system.
    )
