from selenium import webdriver
from bs4 import BeautifulSoup

import time
import os
import json


# Path of the Chrome driver
LOCAL_DIR = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
DRIVER_FILE = 'chromedriver_mac'
DRIVER_LOCATION = os.path.join(LOCAL_DIR, DRIVER_FILE)

# Option setups for Chrome driver
options = webdriver.ChromeOptions() 
options.add_argument("headless")
options.add_argument('--ignore-certificate-errors')

# Setup the Crhome driver
driver = webdriver.Chrome(DRIVER_LOCATION, options=options)
driver.get('https://www.randomlists.com/things')

# Select the "Return" button
random_button = driver.find_elements_by_xpath("//button[@data-action='rerun' and @class='button']")[0]


# Function to parse random names from html
def parse_random_things():

    html = driver.execute_script("return document.body.innerHTML")
    bsObj = BeautifulSoup(html,features='lxml')

    result = []

    if bsObj.find('div', {'class': 'Rand-stage'}):
        random_thing_list = bsObj.find('div', {'class': 'Rand-stage'})
        random_thing_items = random_thing_list.findAll('span', {'class': 'rand_medium'})

        for item in random_thing_items:
            result.append(item.contents[0])      

        return result

    else:
        return None


from progress.bar import Bar

datas = []
bar = Bar('Processing', max=100)

# Repeat the generation for 100 times
for i in range(100):
    datas += parse_random_things()
    random_button.click()
    bar.next()

print("\nScraped %d items in total!" % len(datas))

# Format the data to a dictionary
final_datas = []
for index, name in enumerate(datas):
    item_dict = {'id': index, 'name': name}
    final_datas.append(item_dict)
     
# Writing datas to a json file
with open('data.json', 'w') as outfile:
    json.dump(final_datas, outfile, indent=4)