#useful website
#https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html#videofileclip
#https://stackoverflow.com/questions/72914568/overlay-image-on-video-using-moviepy
#https://docs.python.org/3/library/multiprocessing.html

import multiprocessing
from moviepy.video.VideoClip import ImageClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.editor import concatenate_videoclips
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

number_of_content=4
m=7

def create_video(video):
    ffmpeg_extract_subclip(video, t1=5, t2=65, targetname="./downloaded_videos/video_1.mp4")# creates a subclip

    video_1 = VideoFileClip("./downloaded_videos/video_1.mp4").without_audio().resize(height=H).crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)
    n=3
    image_clips=[]
    for i in range(number_of_content):

        title = ImageClip(f"./downloaded_screenshot/{i}.png").set_start(n).set_duration(m).set_pos(("center","center"))
                #.resize(height=50) # if you need to resize...
        image_clips.append(title)
        
        n+=m

    image_concat = concatenate_videoclips(image_clips).set_position("center")
    final = CompositeVideoClip([video_1, image_concat])
    # final = Video(final).add_watermark(
    #     text="ThePaceMaker_yvanroan", opacity=0.4
    #  ) create a video class that will handle watermarks look at utils/video for reference
    final.write_videofile(
        "./downloaded_videos/test.mp4",
        fps=30,
        audio_codec="aac",
        audio_bitrate="192k",
        verbose=False,
        threads=multiprocessing.cpu_count()#Return the number of CPUs in the system.
    )
if __name__ == "__main__":
    create_video("./downloaded_videos/base_video.mp4",)