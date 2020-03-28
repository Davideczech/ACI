import json
import os
import csv
from pprint import pprint
#list for BD descriptions
bddes=[]
 # Get the absolute path for the directory where this file is located "here"

here = os.path.abspath(os.path.dirname(__file__))

 # Read in the JSON text
with open(os.path.join(here, "tn-PRD_auto.json")) as file:
     json_text = file.read()

# Use the json module to parse the JSON string into native Python data
json_data = json.loads(json_text)


#absolute path to BD descriptions:
#print(json_data["imdata"][0]["fvTenant"]["children"][2]["fvBD"]["attributes"])

for tenant in json_data["imdata"]:
    #iteration through children
    for childrno in tenant["fvTenant"]["children"]:
        #if the BD is in the children list
        if "fvBD" in childrno:
            bddes.append(childrno["fvBD"]["attributes"]["descr"])

            #print(childrno["fvBD"]["attributes"]["descr"])
print(bddes)
with open("descripts.csv", 'w') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(bddes)
