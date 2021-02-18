import argparse, git, re, fileinput, shutil
from pathlib import Path
from git.repo.base import Repo

parser = argparse.ArgumentParser()
parser.add_argument("-url", help="Git Repo url to be cloned", type=str)
parser.add_argument("-O", help="Organizational unit", type=str)
parser.add_argument("-P", help="Project name", type=str, nargs='+')
parser.add_argument("-B", help="Branch name", type=str)
parser.add_argument("-V", help="Version name")
arg = parser.parse_args()

def file_modify(my_file):
    with open(my_file, "r+") as file:
       #read the file contents
       file_contents = file.read()
       text_pattern = re.compile("@Library\(\'SharedLibrary@[0-9][0-9][0-9][0-9].[0-9][0-9].[0-9][0-9]\'\)")
       file_contents = text_pattern.sub("@Library(\'SharedLibrary@"+arg.V+"\')", file_contents)
       file.seek(0)
       file.truncate()
       file.write(file_contents)
       print(file_contents)
       file.close()

for i in arg.P :
    print("Cloning Remote Repo from Git...")
    repo = git.Repo.clone_from(arg.url + "/" + arg.O + "/"+ i, i, branch=arg.B)
    #setting Git Username and email
    with repo.config_writer() as git_config:
        git_config.set_value('user', 'name', 'GR')
        git_config.set_value('user', 'email', 'gr123@example.com')
    #Checking if file exists
    my_file = Path(i+"/"+"Jenkinsfile")
    if my_file.is_file:
        print("File Exists")
        file_modify(my_file)

    else:
        print("File Doesn't Exist")

    #Git Add, Commit and Push
    try:
        repon = Repo(i)
        repon.git.add(update=True)
        repon.index.commit("Jenkinsfile modified")
        origin = repon.remote(name='origin')
        origin.push()
        print("New code change commited to Git Repo")
    except:
        print('Some error occured while pushing the code')

    #Deleting Git Repo
    try:
        shutil.rmtree(i)
    except OSError as e:
        print("Error: %s : %s" % (i, e.strerror))
