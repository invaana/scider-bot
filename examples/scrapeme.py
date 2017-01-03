"""
'rsquarelabs_com.py' is created by 'invaana' for the project 'scout' on 14 December, 2016.

"""

import os, sys
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__)) #adding the parent directory to the python path
SCIDER_PATH = os.path.join(CURRENT_PATH, '..') #adding the project to the python path
sys.path.append(SCIDER_PATH)

from scout.scider.tasks import scrape_website_task, scrape_website_topics_task
from scout.scider import helpers


__CONFIG_FOLDER__ = 'configs'
config_file = "%s/newscientist.json"%__CONFIG_FOLDER__
config = helpers.read_json_file(config_file)



topics_configs =  scrape_website_topics_task(config=config,config_folder=__CONFIG_FOLDER__)['topics_configs']
topics_configs_count = len(topics_configs)
print topics_configs
print "Found %s topics "%topics_configs_count

for i, each_config_loc in enumerate(topics_configs):
    if i ==0:
        continue
    print "Now detailed scrapping %s/%s topics" %(i+1, topics_configs_count)
    config_file = each_config_loc
    config = helpers.read_json_file(config_file)
    scrape_website_task(config, 10000, True)







"""
from scout.scraper import ScrapeDataWithBS4, ScrapeHTML
d = ScrapeHTML('http://rsquarelabs.com')
with open("%s.log"%__name__,'w') as f:
    f.write(d.result['data'].encode('utf-8'))
print d.result
print "Im done"
"""