import urllib.request, json 
import sys, collections
from datetime import datetime
file = open(sys.argv[1], "r")
for l in file:
    line = l
    line = line.replace("artifactory/", "artifactory/api/storage/")
file.close()
dict = {}
dictsort = {}
with urllib.request.urlopen(line) as url:
    data = json.loads(url.read().decode())
    print(data)
    for name in data["children"] :
        art_name = name["uri"].strip('/')
        url2 = urllib.request.urlopen(line.strip('\n') + art_name.strip('\n'))
        data2 = json.loads(url2.read().decode())
        newdt = datetime.strptime(data2["lastModified"], "%Y-%m-%dT%H:%M:%S.%fZ")
        dict.update({newdt : art_name})
dictsort = sorted(dict.keys())
print(dictsort[-1])
urlfile = open(sys.argv[1], "w")
urlfile.write(line.strip('\n').replace("/api/storage", "") + dict[dictsort[-1]].strip('\n'))
urlfile.close()
