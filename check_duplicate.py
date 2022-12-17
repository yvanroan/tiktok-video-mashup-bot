import os
from os.path import exists

# this checks if the video you want to create already exist by checking the title and subreddit
def video_exist(subreddit,title):
    path_result = f"./result/{subreddit}/{title}"

    if exists(path_result):
        print(f"the file {title} already exist in result/{subreddit}.")
        return True
    
    return False