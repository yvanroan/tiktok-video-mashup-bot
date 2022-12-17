from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


input_video_path = './assets/downloaded_videos/main_video.mp4'
output_video_path = './assets/downloaded_videos/base_video.mp4'

def trim_vid(start_time,end_time):
    ffmpeg_extract_subclip(input_video_path, start_time,int(end_time)+1, targetname=output_video_path)#that 2 helps leave it like that



# from moviepy.video.io.VideoFileClip import VideoFileClip

# input_video_path = './assets/downloaded_videos/main_video.mp4'
# output_video_path = './assets/downloaded_videos/base_video_trim.mp4'

# def trim_vid(start_time,end_time):
#     with VideoFileClip(input_video_path) as video:
#         new = video.subclip(start_time, end_time)
#         new.write_videofile(output_video_path, audio_codec='aac')

# if __name__ == "__main__":
#     trim_vid(2022,2177);