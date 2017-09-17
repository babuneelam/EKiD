from PIL import Image, ImageDraw, ImageFont
import os
import GetPic
import random
import re
import sys
sys.path.append(os.getcwd()+'/CCP')
from EnvCfg import EnvCfg
from ImgCfg import ImgCfg
from AlgoCfg import AlgoCfg
from FontCfg import FontCfg

def insert_word(img, word, search_str, img_download_index, image_num):
    draw = ImageDraw.Draw(img)

    GetPic.download_from_google(word, search_str, img_download_index)

    ext_list={'png', 'jpg', 'gif', 'jpeg'}
    for ext in ext_list:
        image_file=EnvCfg.ImageStoreDir + ImgCfg.License+'/'+ \
                   ImgCfg.ImageType+'/'+ word+'/'+str(img_download_index)+'.'+ext
        if os.path.isfile(image_file):
            break
    url_file=EnvCfg.ImageStoreDir + ImgCfg.License+'/'+ \
               ImgCfg.ImageType+'/'+ word+'/'+str(img_download_index)+'_url.txt'
    if os.path.isfile(url_file):
        url_f = open(url_file, "r")
        url = url_f.read()
        url_f.close()
        img_sources_file=EnvCfg.OutputDir+ '/image_sources.txt'
        with open(img_sources_file, 'a') as file_object:
            file_object.write(url)
            file_object.write("\n")


    if not ext:
        print "Couldn't get image"
        return

    # Deciding where to place the lines
    xstart = 1000
    xend = 2300
    if image_num == 1:
        offset = (200, 350)
        ystart=500
        yend = 500
    elif image_num == 2:
        offset = (200, 1000)
        ystart=1150
        yend = 1150
    elif image_num == 3:
        offset = (200, 1650)
        ystart=1800
        yend = 1800
    elif image_num == 4:
        offset = (200, 2300)
        ystart=2450
        yend = 2450
    elif image_num == 5:
        offset = (200, 2950)
        ystart=3100
        yend = 3100
    else:
        print "Invalid image_num"
        return

    img1 = Image.open(image_file, 'r')
    word_img = img1.resize((500, 500))
    word_img_w, word_img_h = word_img.size
    img.paste(word_img, offset)

    # Draw the lines
    fontFactor = FontCfg.FontFactor
    yoffset = 125
    draw.line((xstart, ystart, xend, yend), fill='black', width=3)
    for x in xrange(xstart, xend, 35):
        draw.line((x, ystart+(yoffset/fontFactor), x+18, \
                   yend+(yoffset/fontFactor)), \
                  fill='grey', width=3)
    draw.line((xstart,ystart+(yoffset*2/fontFactor), xend, \
               yend+(yoffset*2)/fontFactor), \
              fill='black', width=3)

    capitalLetterSize = 355
    smallLetterSize = 240
    fontsFolder1 = EnvCfg.FontsFolder
    upperArialFont = ImageFont.truetype(os.path.join(fontsFolder1, \
                         'Arial.ttf'), capitalLetterSize/fontFactor)
    lowerArialFont = ImageFont.truetype(os.path.join(fontsFolder1, \
                         'Arial.ttf'), smallLetterSize/fontFactor)
    fontsFolder2 = EnvCfg.CustomFontsDir
    upperDashFont = ImageFont.truetype(os.path.join(fontsFolder2, \
                         'bythebutterfly_dashness/dashness.ttf'), \
                         capitalLetterSize/fontFactor)
    lowerDashFont = ImageFont.truetype(os.path.join(fontsFolder2, \
                         'bythebutterfly_dashness/dashness.ttf'), \
                         smallLetterSize/fontFactor)

    # Draw the aplphabet
    word_len = len(word)
    if AlgoCfg.AlgoType == 'Full':
        draw.text((xstart,ystart-(15/fontFactor)), word[0].upper(), \
                  fill = 'grey', font=upperDashFont) 
        i=300/fontFactor 
        for c in word[1:]:
            draw.text((xstart+i,ystart+75/fontFactor), c, fill = 'grey', \
                      font=lowerDashFont)  
            i += 175/fontFactor 
    elif AlgoCfg.AlgoType == 'Specified':
        if word[0] == '-':
            draw.text((xstart,ystart-(105/fontFactor)), '_' , fill = 'grey', \
                      font=upperArialFont)
        else:
            draw.text((xstart,ystart-(15/fontFactor)), word[0].upper(), \
                      fill = 'grey', font=upperDashFont)
        i=300/fontFactor
        for c in word[1:]:
            if c == '-':
                draw.text((xstart+i,ystart+(25/fontFactor)), '_' , \
                          fill = 'grey', font=lowerArialFont)
            else:
                draw.text((xstart+i,ystart+(75/fontFactor)), c, \
                          fill = 'grey', font=lowerDashFont)
            i += 175/fontFactor
    elif AlgoCfg.AlgoType == 'Random':
        cur_blank_chars = 0
        max_blank_chars = min(word_len, AlgoCfg.max_blank_chars)
        if max_blank_chars == word_len:
            blank_pos_list = range(1, word_len+1)
        else:
            blank_pos_list = random.sample(range(1, word_len), max_blank_chars)
            blank_pos_list.sort()
        blank_pos = blank_pos_list[cur_blank_chars]
        if (blank_pos == 1):
            draw.text((xstart,ystart-(105/fontFactor)), '_' , fill = 'grey', \
                      font=upperArialFont)
            cur_blank_chars += 1
            blank_pos = blank_pos_list[cur_blank_chars]
        else:
            draw.text((xstart,ystart-(15/fontFactor/2)), word[0].upper(), \
                      fill = 'grey', font=upperDashFont)
        cur_pos=2
        i=350/fontFactor
        for c in word[1:]:
            if (cur_blank_chars != max_blank_chars and blank_pos == cur_pos):
                draw.text((xstart+i,ystart+(25/fontFactor)), '_' , \
                          fill = 'grey', font=lowerArialFont)
                cur_blank_chars += 1
                if cur_blank_chars < max_blank_chars:
                    blank_pos = blank_pos_list[cur_blank_chars]
            else:
                draw.text((xstart+i,ystart+(85/fontFactor)), c, \
                          fill = 'grey', font=lowerDashFont)
            i += 175/fontFactor
            cur_pos += 1
    elif AlgoCfg.AlgoType == 'Empty':
        pass
    

if __name__ == "__main__":
    img= sys.argv[1]
    searchtext = sys.argv[2]
    insert_word(img, searchtext)


