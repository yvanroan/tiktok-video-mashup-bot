#useful website
#https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html#videofileclip
#https://stackoverflow.com/questions/72914568/overlay-image-on-video-using-moviepy
#https://docs.python.org/3/library/multiprocessing.html

from moviepy.video.VideoClip import ImageClip
from moviepy.editor import * 
from os.path import exists
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.AudioClip import CompositeAudioClip
from speedup import speed_up


video_path = './assets/downloaded_videos/base_video.mp4'
W, H = 1080, 1920


def create_video(number_of_clips,title,subreddit):
    VideoFileClip.reW = lambda clip: clip.resize(width=W)
    VideoFileClip.reH = lambda clip: clip.resize(width=H)
    video= VideoFileClip(video_path).without_audio().resize(height=H).crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)#resize(height=1920,width=1080).

    image_clips=[]

    audio_clips = [AudioFileClip(f"./assets/speeches/{i}.mp3") for i in range(number_of_clips)]
    audio_concat = concatenate_audioclips(audio_clips)
    audio_composite = CompositeAudioClip([audio_concat])

    for i in range(number_of_clips):
        image_clips.append(
            ImageClip(f"./assets/downloaded_screenshot/{i}.png")
            .resize(width=W - 200)
            .set_duration(audio_clips[i].duration)
        )

    image_concat= concatenate_videoclips(image_clips).set_position("center")
    image_concat.audio = audio_composite
    final= CompositeVideoClip([video,image_concat])
    watermark= ImageClip(f"./assets/watermark/watermark11.png").set_duration(audio_composite.duration).margin(right=8, bottom=8, opacity=0).set_pos(("right","bottom"))

    final = CompositeVideoClip([final,watermark])


    if not exists(f"./result/{subreddit}"):
        print("The results folder didn't exist so I made it")
        os.makedirs(f"./result/{subreddit}")

    final.write_videofile(
        f"./result/{subreddit}/{title}.mp4",
        fps=30,
        audio_codec="aac",
        audio_bitrate="192k",
        verbose=False,
        # threads=multiprocessing.cpu_count()#Return the number of CPUs in the system.
    )

