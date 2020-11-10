#!/usr/bin/python3
import os
import subprocess as sb
from yattag import Doc,indent
os.system('clear')
n=0
while True:
    os.system('tput setaf  1')
    os.system("figlet 'Hadoop Automation' ")
    os.system('tput setaf  6')
    inp=input("What can I do for you? : ")
    if ("setup" in inp):
        if("namenode" in inp) or ("name node" in inp) or ("master" in inp):
            n=0
        elif("datanode" in inp) or ("data node" in inp) or ("slave" in inp):
            n=1
        else:
            node=input("Which node do you want to setup? : ")
            while True:
                if("namenode" in node) or ("name node" in node) or ("master" in node):
                    n=0
                    break
                elif("datanode" in node) or ("data node" in node) or ("slave" in node):
                    n=1
                    break
                else:
                    print("Invalid choice.")
                    node=input("please enter again(datanode/namenode)? : ")
        os.system('tput setaf  5')
        mkd=input("give the name of the directory : ")
        os.system('mkdir /{}'.format(mkd))
        os.system('rm -f  /etc/hadoop/hdfs-site.xml')
        os.system('rm -f  /etc/hadoop/core-site.xml') 
        print('Created a new Directory')
        ip=input("Enter ip address of master : ")
        os.system("cd /etc/hadoop")
        doc,tag,text=Doc().tagtext()
        with tag('configuration'):
            with tag('property'):
                with tag('name'):
                    if n==0:
                        text('dfs.name.dir')
                    else:
                        text('dfs.data.dir')
                with tag('value'):
                    text('/{}'.format(mkd))
        result=indent(
        doc.getvalue(),
        indentation =' '*4,
        newline='\r\n')
        f=open('/etc/hadoop/hdfs-site.xml','a')
        f.write('{}\n'.format(result))
        f.close()
        doc1,tag1,text1=Doc().tagtext()
        with tag1('configuration'):
            with tag1('property'):
                with tag1('name'):
                        text1('fs.default.name')
                with tag1('value'):
                    text1('hdfs://{}'.format(ip)+':9001')
        res=indent(
        doc1.getvalue(),
        indentation =' '*4,
        newline='\r\n')
        f=open('/etc/hadoop/core-site.xml','a')
        f.write('{}\n'.format(res))
        f.close()
        os.system('tput setaf  2')
        print('Setup Complete')
        if int(n==0):
            os.system("hadoop namenode -format -Y")
            os.system("hadoop-daemon.sh start namenode")
            os.system('jps | grep Namenode > /dev/null')
            if os.system('echo  $?')==0:
                os.system("figlet  Namenode Started")
                os.system("jps")
                os.system('sleep 5')
                os.system('clear')
            else:
                os.system("figlet  Namenode Start error")
                os.system('clear')
                    
        else:
            os.system("hadoop-daemon.sh start datanode")
            os.system('tput setaf 3')
            os.system('jps')
            os.system("figlet  Datanode Started")
            os.system('sleep 5')
            os.system('clear')
         
    
    elif ((('install' or 'download' or 'package' or 'rpm' or 'software' in inp)  and ('hadoop' in inp))):
        print('Please wait while we are installing Hadoop version 1.2 and Oracle JDK ...!!')
        os.system('pip3 install gdown')
        os.system('gdown https://drive.google.com/file/d/17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz/view?usp=sharing')
        os.system('gdown  https://drive.google.com/file/d/1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5/view?usp=sharing')
        os.chdir('/root/hadoopv1.2')
        os.system('rpm -ivh   jdk-8u171-linux-x64.rpm')
        os.system('rpm -ivh   hadoop-1.2.1-1.x86_64.rpm --force')
        os.system('figlet Hadoop & JDK installed..!')
        os.system('sleep 3')   
        os.system('clear')
    elif("bye" or "exit" or "quit" in inp):
        os.system('tput setaf 7')
        os.system('clear')
        break

