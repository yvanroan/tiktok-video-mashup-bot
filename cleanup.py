import os,time
from os.path import exists

def cleanup():
    #Deletes all temporary files in assets( doesnot clean the background videos at the moment)

    # Returns:
    #     int: How many files were deleted
    path_screenshots = "./assets/downloaded_screenshot"
    path_videos = "./assets/downloaded_videos"
    path_speeches = "./assets/speeches"
    if exists("./assets"):
        file_screenshot = [f for f in os.listdir(path_screenshots)]
        file_videos = [f for f in os.listdir(path_videos)]
        file_speeches = [f for f in os.listdir(path_speeches)]

        for f in file_screenshot:
            os.remove(path_screenshots+'/'+f)

        for f in file_speeches:
            os.remove(path_speeches+'/'+f)


        
        

