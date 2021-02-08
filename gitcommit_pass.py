import sys, git, re, fileinput, shutil
from pathlib import Path

from git.repo.base import Repo

print("Cloning Remote Repo from Git...")
repo = git.Repo.clone_from(sys.argv[1]+"/"+sys.argv[2]+"/"+sys.argv[3], sys.argv[3], branch=sys.argv[4])

#setting Git Username and email
with repo.config_writer() as git_config:
    git_config.set_value('user', 'name', 'GR')
    git_config.set_value('user', 'email', 'gr123@example.com')

def file_modify(my_file):
    with open(my_file, "r+") as file:
       #read the file contents
       file_contents = file.read()
       text_pattern = re.compile("@Library\(\'SharedLibrary@[0-9][0-9][0-9][0-9].[0-9][0-9].[0-9][0-9]\'\)")
       file_contents = text_pattern.sub("@Library(\'SharedLibrary@"+sys.argv[5]+"\')", file_contents)
       file.seek(0)
       file.truncate()
       file.write(file_contents)
       print(file_contents)
       file.close()

#Checking if file exists
my_file = Path(sys.argv[3]+"/"+"Jenkinsfile")
if my_file.is_file:
    print("File Exists")
    file_modify(my_file)

else:
    print("File Doesn't Exist")

#Git Add, Commit and Push
try:
    repon = Repo(sys.argv[3])
    repon.git.add(update=True)
    repon.index.commit("Jenkinsfile modified")
    origin = repon.remote(name='origin')
    origin.push()
    print("New code change commited to Git Repo")
except:
    print('Some error occured while pushing the code')

#Deleting Git Repo
try:
    shutil.rmtree(sys.argv[3])
except OSError as e:
    print("Error: %s : %s" % (sys.argv[3], e.strerror))
