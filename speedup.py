
from moviepy.editor import *
from pydub import AudioSegment

   
# loading video dsa gfg intro video
def speed_up(path):
    
    AudioSegment.converter = './ffmpeg.exe'                        
    AudioSegment.ffprobe   = './ffprobe.exe'
    sound = AudioSegment.from_file(path, format="mp3")
    speed_X = 1.1
    final = sound.speedup(speed_X, 150, 25)


    #export / save pitch changed sound
    final.export(path, format="mp3")
    audio = AudioFileClip(path)
    return audio.duration


# if __name__== "__main__":
#     speed_up('./assets/speeches/5.mp3','./assets/speeches/20.mp3')
    