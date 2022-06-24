#!/usr/bin/python
import pexpect
import sys
child = pexpect.spawn('sudo minicom -D /dev/ttyUSB0', env = {"TERM": "vt102"})
child.sendline('')
child.expect('root@app:~#')

#Checking whether app is working
print("**********Checking whether app is working**********")
child.sendline('ls /dev/rpmsg*')
child.expect('\r\n')
child.expect('root@app:~#')
print child.before[:-2]
print('\n')

#Checking Artifact Version
print("**********Checking Artifact Version**********")
child.sendline('cat /etc/mender/artifact_info')
child.expect('\r\n')
child.expect('root@app:~#')
print child.before[:-2]
print('\n')

#Printing Log Messages
print("**********Printing Log Messages**********")
child.sendline('cat /logs/messages')
child.expect('\r\n')
child.expect('root@app:~#')
print child.before[:-2]
print('\n')

#Checking Process Status
print("**********Checking Process Status**********")
child.sendline('ps | grep start.sh')
child.expect('\r\n')
child.expect('root@app:~#')
print child.before[:-2]
print('\n')

#Checking LTE connectivity
print("**********Checking LTE connectivity**********")
child.sendline('ping 172.217.17.68')
child.expect('\r\n')
child.sendcontrol('c')
child.expect('root@app:~#')
print child.before[:-4]
print('\n')

#Checking Disk Space
print("**********Checking Disk Space**********")
child.sendline('df -h')
child.expect('\r\n')
child.expect('root@app:~#')
print child.before[:-2]
print('\n')

#Checking Memory Usage Status
print("**********Checking Memory Usage Status**********")
child.sendline('top')
child.sendline('')
child.sendcontrol('c')
child.expect('\r\n')
child.expect('root@app:~#')
print child.before[:-4]
print('\n')

#Checking Ethernet
print("**********Checking Ethernet**********")
child.sendline('ifconfig eth0')
child.expect('\r\n')
child.expect('root@app:~#')
print child.before[:-2]
print('\n')

#Terminating Minicom
print("**********Terminating Minicom**********")
child.terminate(force=True)
sys.exit()
