import sys, re
def Str_Chck(filen, string):
    file = open(filen, "r")
    match = False
    for line in file:
        matched = re.match(string, line)
        if bool(matched):
            print (line+ " version is present")
            match = True
    file.close()
    return match

filen = sys.argv[1]
version1 = Str_Chck(filen, "[Vv][eE][Rr] = [0-9].[0-9].[0-9]")
version2 = Str_Chck(filen, "[Vv][eE][Rr] = [0-9].[0-9].[0-9]")
version3 = Str_Chck(filen, "[Vv][eE][Rr] = [0-9].[0-9].[0-9]")
if version1 and version2 and version3:
    print("success")
else:
    print("Build failed due to version1 or version2 or version3 not specified")
    sys.exit(-1)
