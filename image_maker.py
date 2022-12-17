from PIL import Image, ImageDraw, ImageFont
import textwrap
from get_data import reddit_scrapper
from get_twitter import twitter_scrapper

def img_maker(data):
    k=0
    data2={}
    idx=0

    while k<len(data):
        lines = textwrap.wrap(data[k],70)#width=70
        print(f'{lines}')
        length = len(lines)
        
        width=700
        # if the lines are more than 4, we will cut them in rectangles of two lines and save them 
        
        if length<=3:
            text= ' '
            height= (length+2)*20
            # create empty image
            img = Image.new(size=(width, height), mode='RGB')
            draw = ImageDraw.Draw(img)

            top = 0
            bottom = 200
            left = 0
            right = 650

            # draw white rectangle 350x200 with center in 200,150
            draw.rectangle((left, top, right, bottom), fill='black')

            current_top = top
            current_left = left



            #bold arial font
            content_font = ImageFont.FreeTypeFont('./assets/arial.ttf', size=19)


            
            #intialize the top position of the text
            current_top = 20

            #if the text goes below the width it goes onto a new line
            for line in lines:
                left2, top2, right2, bottom2 = content_font.getbbox(line)  # new version
                width = right2 - left2
                height = bottom2 - top2
                draw.text((current_left+10, current_top), line, font=content_font, fill='white')
                text+= line+' '
                current_top += height+5

            img.save(f'./assets/downloaded_screenshot/{k+idx}.png')
            data2[k+idx]= text
            
        else:

            i=0
            j=3
        
            while j<=length:
                text= ' '
                sublines=lines[i:j]

                sublength=len(sublines)+2 #the 2 is for the space above and below

                height= sublength*20
                # create empty image
                img = Image.new(size=(width, height), mode='RGB')
                draw = ImageDraw.Draw(img)

                top = 0
                bottom = 200
                left = 0
                right = 650

                # draw white rectangle 350x200 with center in 200,150
                draw.rectangle((left, top, right, bottom), fill='black')

                current_top = top
                current_left = left



                #bold arial font
                content_font = ImageFont.FreeTypeFont('./assets/arial.ttf', size=19)


                
                #intialize the top position of the text
                current_top = 20

                #if the text goes below the width it goes onto a new line
                for line in sublines:
                    left2, top2, right2, bottom2 = content_font.getbbox(line)  # new version
                    # width1 = right2 - left2
                    height1 = bottom2 - top2
                    draw.text((current_left+10, current_top), line, font=content_font, fill='white')
                    text+= line+' '
                    current_top += height1+5

                img.save(f'./assets/downloaded_screenshot/{k+idx}.png')
                data2[k+idx]= text
                print(f'{i},{j},{idx}')
                # print(f'{text}')
                i=j
                if j==length:
                    break
                if j+3>length:
                    j=length
                else:
                    j+=3
                idx+=1
        
        k+=1
    return data2