# Automatic Script for getting the json file for all of the data in the /People folder
# !/usr/bin/python

import os

picture = "/home/wlhoyt/Pictures/People"
label = "/home/wlhoyt/Pictures/Label"
files = os.listdir(picture)

for name in files:
    num = name.split(".")[0]
    url = "http://localhost:3000/api/json/%" + "2F"+ str(num) + ".jpg"
    label_num = label + "/" + str(num) + ".json"
    command  = "wget -P " + label + " -O " + label_num + " " + url
    os.system(command)
