import os
import re

class FontCfg:
    FontSize = 'K1'
    FontFactor = 2 # Relative to PK3. The more this, the less the font size

    @classmethod
    def process_config_file(cls, font_config_file):
        font_f = open(font_config_file)
        font_cfgs = font_f.readlines()

        for font_cfg in font_cfgs:
            font_cfg = font_cfg.rstrip()
            if bool(re.match('^GradeLevel=[A-Za-z0-9]+', font_cfg)):
                FontSize= font_cfg.partition('=')[2]
                if FontSize == "K1":
                    cls.FontSize = FontSize
                    cls.FontFactor = 2 
                elif (FontSize == "PS1" or FontSize == "PS2" or \
                      FontSize == "PS3" or FontSize == "PK1" or \
                      FontSize == "PK2" or FontSize == "PK3"):
                    cls.FontSize = FontSize
                    cls.FontFactor = 1 
                else: # invalid inputs
                    pass
            else:
               continue
        #print cls.FontSize
        #print cls.FontFactor
 

