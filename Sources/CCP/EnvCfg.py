import os
import re

class EnvCfg:
    RunDir='../RuntimeInfo/'
    OutputDir='../RuntimeInfo/output/'
    ImageStoreDir='../RuntimeInfo/google_images/'
    GeckoDrvPath=''
    GeckoDrvLogFile='../RuntimeInfo/geckodriver.log'
    FontsFolder=''
    CustomFontsDir='MyCustomFonts'

    @classmethod
    def process_config_file(cls, environ_config_file):
        env_f = open(environ_config_file)
        env_cfgs = env_f.readlines()

        for env_cfg in env_cfgs:
            env_cfg = env_cfg.rstrip()
            #print env_cfg
            if bool(re.match('^GECKO_DRV_PATH=[A-Ba-b0-9\/]+', env_cfg)):
                cls.GeckoDrvPath = env_cfg.partition('=')[2]
                #print env_cfg.partition('=')[2]
            elif bool(re.match('^FONTS_FOLDER=[A-Ba-b0-9\/]+', env_cfg)):
                cls.FontsFolder = env_cfg.partition('=')[2]
                #print env_cfg.partition('=')[2]
            else:
               continue
        #print cls.GeckoDrvPath

