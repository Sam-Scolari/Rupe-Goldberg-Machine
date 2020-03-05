from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import time

#options = Options()
#options.add_argument("--headless")
#driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()

while (True):
    driver.get("https://lprubegoldberg.weebly.com/")

    site_time = (driver.find_element_by_css_selector(".blog-title-link").text)[16:-2]

    site_hour = int(site_time[:2])
    site_min = int(site_time[3:])


    real_hour = int(time.strftime('%I'))
    real_min = int(time.strftime('%M'))

    real_time = str(real_hour) + ":" + str(real_min)

    if (site_min == real_min or site_min-1 == real_min or site_min+1 == real_min):
        print("Running!")
        time.sleep(60)

    time.sleep(1)



    

    