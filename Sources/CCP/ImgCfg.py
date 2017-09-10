import os

class ImgCfg:
    ImageType = 'AllImages'
    License = 'FreeLicense'

    @classmethod
    def process_config_file(cls, img_config_file):
        img_f = open(img_config_file)
        img_cfgs = img_f.readlines()

        for img_cfg in img_cfgs:
            img_cfg = img_cfg.rstrip()
            if img_cfg == 'AnyLicense':
                cls.License = 'AnyLicense'
            elif img_cfg == 'FreeLicense':
                cls.Liense = 'FreeLicense'
            elif img_cfg == 'AllImages':
                cls.ImageType = 'AllImages'
            elif img_cfg == 'LineartImages':
                cls.ImageType = 'LineartImages'
            else:
               continue
 

