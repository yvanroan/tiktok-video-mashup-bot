
import praw
import pandas as pd
import PIL
from PIL import Image, ImageDraw, ImageFont
import textwrap
import itertools


reddit_read_only = praw.Reddit(client_id="1Lv93E7_10pKuvuZKNj9Dg", client_secret="ces0dPBH0dhTC-xydMjbAmcXtAczXA", user_agent="monroi")


subreddit = reddit_read_only.subreddit("AskReddit")
    
posts = subreddit.top(time_filter='week')
# Scraping the top posts of the current week

posts_dict = {"Title": [],
              "Post Text": [],
              "ID": [],
              "Score": [],
              "Total Comments": [],
              "Post URL": []
			}

top20 = itertools.islice(posts, 3)
print("start")
for post in top20:
    print("init")
    url = "https://www.reddit.com" + post.permalink
    
    # Title of each post
    posts_dict["Title"].append(post.title)
	
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
	
    # Unique ID of each post
    posts_dict["ID"].append(post.id)
	
    # The score of a post
    posts_dict["Score"].append(post.score)
	
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
    
    # URL of each post
    posts_dict["Post URL"].append(url)
    print("mid")
    
    submission = reddit_read_only.submission(url=url) 
    submission.comments.replace_more(limit=0)     
    print("again")
# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
print("end")
print(top_posts)

#top_posts.to_csv("Top Posts.csv", index=True)


#--------------------------------------------------------------
#                  drawing starts here
#--------------------------------------------------------------

# create empty image
# img = Image.new(size=(350, 200), mode='RGB')
# draw = ImageDraw.Draw(img)

# top = 0
# bottom = 200
# left = 0
# right = 350

# draw white rectangle 350x200 with center in 200,150
# draw.rectangle((left, top, right, bottom), fill='white')

# current_top = top
# current_bottom = bottom
# current_left = left
# current_right = right

#reddit icon
# reddit_icon = Image.open('reddit_icon.png')
# reddit_icon.thumbnail((30,30))

# img.paste(reddit_icon,(current_left+5,current_top+10))

# arial = ImageFont.FreeTypeFont('C:/Users/roany/python codes/tiktok_reddit bot/arial.ttf', size=13)

# subreddit="r/AskReddit \n"

# user="u/its_him \n\n"

#writing subreddit and user
# left1, top1, right1, bottom1 = arial.getbbox(subreddit)  # new version
# width = right1 - left1
# height = bottom1 - top1

# current_top +=10

# draw.text((current_left+10+30, current_top), subreddit, font=arial, fill='black')
# draw.text((current_left+10+30, current_top+15), user, font=arial, fill=(153,153,255))

# current_top += height

#bold arial font
# content_font = ImageFont.FreeTypeFont('C:/Users/roany/python codes/tiktok_reddit bot/arial_bold.ttf', size=16) 


# lines = textwrap.wrap(top_posts.get("Title")[0], width=40)



#you might realize that the size of the rectangle and the text do not match its not our fault its just how weird it is ;)

#intialize the top position of the text
# current_top += 30

#if the text goes below the width it goes onto a new line
# for line in lines:
#     left2, top2, right2, bottom2 = content_font.getbbox(line)  # new version
#     width = right2 - left2
#     height = bottom2 - top2
#     draw.text((current_left+10, current_top), line, font=content_font, fill='black')
#     print(line)
#     current_top += height+5

# img.save('center-newer.png')

# img.show()