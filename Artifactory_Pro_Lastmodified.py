import urllib.request, json 
import sys, collections
import requests
from datetime import datetime
file = open(sys.argv[1], "r")
for l in file:
    line = l
    line = line.replace("artifactory/", "artifactory/api/storage/")
file.close()
dict = {}
dictsort = {}
user = 'user'
passwd = 'password'
with requests.get(line, auth=(user, passwd)) as url:
    data = json.loads(url.text)
    print(data)
    for name in data["children"] :
        art_name = name["uri"].strip('/')
        fullpath = line.strip('\n') + art_name.strip('\n')
        url2 = requests.get(fullpath, auth=(user, passwd))
        data2 = json.loads(url2.text)
        print(data2["lastModified"])
        newdt = datetime.strptime(data2["lastModified"], "%Y-%m-%dT%H:%M:%S.%f%z")
        dict.update({newdt : art_name})
dictsort = sorted(dict.keys())
print(dictsort[-1])
urlfile = open(sys.argv[1], "w")
urlfile.write(line.strip('\n').replace("/api/storage", "") + dict[dictsort[-1]].strip('\n'))
urlfile.close()
