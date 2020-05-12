import os
import time
import paramiko
#paramiko.util.log_to_file('/tmp/paramiko.log')
#paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

host = 'owncloud.estuate.com'
port = 22
username = 'root'
pwd='sys3stu@t3'

#files = ['file1', 'file2', 'file3', 'file4']
remote_images_path = '/root/anaconda-ks.cfg'
local_path = 'C:/Users/nishant.singh/Desktop/Python'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, port=port, username=username, password=pwd)
stdin, stdout, stderr = ssh.exec_command(command)
(stdoutstring, stderrstring) = execute_ssh_command(host, port, username, pwd, "ls -al")
for stdoutrow in stdoutstring:
    print (stdoutrow)
sftp = ssh.open_sftp()
sftp.get(remote_images_path, local_path)
sftp.close()
ssh.close()
