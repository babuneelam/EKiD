"""
Source: https://github.com/atif93/google_image_downloader
Not extact replica of the above source, Modified as necesary
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import os
import json
import urllib2
import sys
import time
sys.path.append(os.getcwd()+'/CCP')
from EnvCfg import EnvCfg
from ImgCfg import ImgCfg

#os.environ["PATH"] += os.pathsep + os.getcwd()

def download_from_google(word):
        ext_list={'png', 'jpg', 'gif', 'jpeg'}
        for ext in ext_list:
            image_file = EnvCfg.ImageStoreDir + ImgCfg.License+'/'+ \
                         ImgCfg.ImageType + '/' +word+'/0.'+ext
            if os.path.isfile(image_file):
                #print "image file exists already"
	        return
        download_path = EnvCfg.ImageStoreDir + ImgCfg.License+'/'+ \
                        ImgCfg.ImageType+'/'
	num_requested = 1
	number_of_scrolls = num_requested / 400 + 1 
	# number_of_scrolls * 400 images will be opened in the browser

	if not os.path.exists(download_path + word.replace(" ", "_")):
		os.makedirs(download_path + word.replace(" ", "_"))

        #display = Display(visible=0, size=(800, 600))
        #display.start()

        if (ImgCfg.License == 'AnyLicense' and ImgCfg.ImageType == 'AllImages'):
            # All Images, Any License, safe search on
            url = "https://www.google.com/search?tbm=isch&source=hp&biw=1164&bih=635&q="+word+"&oq="+word+"&gs_l=img.3..0l10.46946.47724.0.48035.7.7.0.0.0.0.132.472.2j3.5.0....0...1.1.64.img..2.5.472.0..35i39k1.lGhvJnRhXEM"

        elif (ImgCfg.License == 'FreeLicense' and ImgCfg.ImageType == 'AllImages'):
            # Any Images, Free License, safe search on
            url = "https://www.google.com/search?q="+word+"&safe=active&tbm=isch&source=lnt&tbs=sur:fc&sa=X&ved=0ahUKEwi_0em0t_bVAhXEhFQKHf_rD_oQpwUIHw&biw=1164&bih=635&dpr=2"
        elif (ImgCfg.License == 'AnyLicense' and ImgCfg.ImageType == 'LineartImages'):
            # Line Art Images, Any License, safe search on
            url = "https://www.google.com/search?q="+word+"&safe=active&tbm=isch&source=lnt&tbs=itp:lineart&sa=X&ved=0ahUKEwi_0em0t_bVAhXEhFQKHf_rD_oQpwUIHw&biw=1164&bih=635&dpr=2"
        elif (ImgCfg.License == 'FreeLicense' and ImgCfg.ImageType == 'LineartImages'):
            # Line Art Images, Free License, safe search on
            url = "https://www.google.com/search?q="+word+"&safe=active&tbs=itp:lineart,sur:fc&tbm=isch&source=lnt&sa=X&ved=0ahUKEwjr3s7OuPbVAhVByVQKHUhbAmUQpwUIHw&biw=1164&bih=635&dpr=2"

	#url = "https://www.google.com/search?q="+word+"&source=lnms&tbm=isch"

        # Advance search, linear art filter
        #url = "https://www.google.com/search?as_st=y&tbm=isch&as_q=&as_epq="+word+"&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=itp:lineart,sur:f"

        # All Images, Any License
        #url = "https://www.google.com/search?tbm=isch&source=hp&biw=1164&bih=635&q="+word+"&oq="+word+"&gs_l=img.3..0l10.46946.47724.0.48035.7.7.0.0.0.0.132.472.2j3.5.0....0...1.1.64.img..2.5.472.0..35i39k1.lGhvJnRhXEM"


	driver = webdriver.Firefox(executable_path=EnvCfg.GeckoDrvPath, log_path=EnvCfg.GeckoDrvLogFile)
	#driver = webdriver.PhantomJS()
	driver.get(url)

	headers = {}
	headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
	extensions = {"jpg", "jpeg", "png", "gif"}
	img_count = 0
	downloaded_img_count = 0
	
	for _ in xrange(number_of_scrolls):
		for __ in xrange(10):
			# multiple scrolls needed to show all 400 images
			driver.execute_script("window.scrollBy(0, 1000000)")
			time.sleep(0.2)
		# to load next 400 images
		time.sleep(0.5)
		try:
			driver.find_element_by_xpath("//input[@value='Show more results']").click()
		except Exception as e:
			print "Less images found:", e
			break

	# imges = driver.find_elements_by_xpath('//div[@class="rg_meta"]') # not working anymore
	imges = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
	#print "Total images:", len(imges), "\n"
	for img in imges:
		img_count += 1
		img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
		img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
		#print "Downloading image", img_count, ": ", img_url
		try:
			if img_type not in extensions:
				img_type = "jpg"
			req = urllib2.Request(img_url, headers=headers)
			raw_img = urllib2.urlopen(req).read()
			f = open(download_path+word.replace(" ", "_")+"/"+str(downloaded_img_count)+"."+img_type, "wb")
			f.write(raw_img)
			f.close
			downloaded_img_count += 1
		except Exception as e:
			print "Download failed:", e
		finally:
			print
		if downloaded_img_count >= num_requested:
			break

	#print "Total downloaded: ", downloaded_img_count, "/", img_count
	driver.quit()
 
        #display.stop()

if __name__ == "__main__":
	word = sys.argv[1]
	get_pic_from_google(word)

