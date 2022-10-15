from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


input_video_path = './assets/downloaded_videos/main_video.mp4'
output_video_path = './assets/downloaded_videos/base_video_trim.mp4'

def trim_vid(start_time,end_time):
    ffmpeg_extract_subclip(input_video_path, start_time,end_time, targetname=output_video_path)


# from moviepy.video.io.VideoFileClip import VideoFileClip

# input_video_path = './assets/downloaded_videos/main_video.mp4'
# output_video_path = './assets/downloaded_videos/base_video_trim.mp4'

# def trim_vid(start_time,end_time):
#     with VideoFileClip(input_video_path) as video:
#         new = video.subclip(start_time, end_time)
#         new.write_videofile(output_video_path, audio_codec='aac')
