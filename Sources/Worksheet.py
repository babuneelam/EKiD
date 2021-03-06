from PIL import Image, ImageDraw, ImageFont
import os
import re
import sys
import DrawWord
import shutil
sys.path.append(os.getcwd()+'/CCP')
from EnvCfg import EnvCfg
from ImgCfg import ImgCfg
from AlgoCfg import AlgoCfg
from FontCfg import FontCfg

cfgDir = '../ConfigControls/'
#Process Config Files 
EnvCfg.process_config_file(cfgDir+'EnvCfg')
#traceConfig = TraceCfg(cfgDir+'TraceCfg')
ImgCfg.process_config_file(cfgDir+'ImgCfg')
FontCfg.process_config_file(cfgDir+'FontCfg')
AlgoCfg.process_config_file(cfgDir+'AlgoCfg')

runDir = EnvCfg.RunDir
outDir = EnvCfg.OutputDir

#Remove existing contents of output directoty
if os.path.exists(runDir):
    if os.path.exists(outDir):
        shutil.rmtree(outDir)
    os.makedirs(outDir)
else:
    os.makedirs(runDir)
    os.makedirs(outDir)

# Read words from input file & create instances for each 
word_file = open(cfgDir+'WordList')
word_lines = word_file.readlines()

if AlgoCfg.AlgoType == 'Set':
    algo_list={'Full', 'Empty', 'Random'}
    fno = 1
    for algo in algo_list:
        AlgoCfg.AlgoType = algo
        #Create Image file
        img = Image.new('RGBA', (2480, 3508), 'white')
        sub = 1

        #print words in the worksheet
        word_num=1
        for word_line in word_lines:
            word_line = word_line.rstrip()
            words = re.split(",\s*", word_line)
            if (len(words) >1):
                img_download_index = int(words[1]) -1
            else:
                img_download_index = 0
            if (len(words) >2):
                search_str = words[2]
            else:
                search_str = words[0]
            if words[0] != '':
                DrawWord.insert_word(img, words[0].lower(), search_str, img_download_index, word_num)
                word_num += 1
                if word_num == 6:
                    #Save image into a disk file
                    img.save(outDir+'/ws'+str(fno)+'_'+str(sub)+'.png')
                    #Create Image file
                    img = Image.new('RGBA', (2480, 3508), 'white')
                    word_num=1
                    sub += 1
    
        if word_num >= 2 and word_num < 6 :
            #Save image into a disk file
            img.save(outDir+'ws'+str(fno)+'_'+str(sub)+'.png')
        fno += 1
else:
    fno = 1
    #Create Image file
    img = Image.new('RGBA', (2480, 3508), 'white')

    #print words in the worksheet
    word_num=1
    for word_line in word_lines:
        word_line = word_line.rstrip()
        words = re.split(",\s*", word_line)
        if (len(words) >1):
            img_download_index = int(words[1]) -1
        else:
            img_download_index = 0
        if (len(words) >2):
            search_str = words[2]
        else:
            search_str = words[0]
        if words[0] != '':
            DrawWord.insert_word(img, words[0].lower(), search_str, img_download_index, word_num)
            word_num += 1
            if word_num == 6:
                #Save image into a disk file
                img.save(outDir+'ws'+str(fno)+'.png')
                #Create Image file
                img = Image.new('RGBA', (2480, 3508), 'white')
                word_num=1
                fno += 1
    if word_num >= 2 and word_num < 6 :
        #Save image into a disk file
        img.save(outDir+'ws'+str(fno)+'.png')

