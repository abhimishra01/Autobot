#!/usr/bin/python3
import os
import subprocess as sb
from yattag import Doc,indent
os.system('clear')
os.system('tput setaf  6')
os.system("figlet 'Hadoop \nautomation' -f small")
n=0
while True:
    os.system('tput setaf  6')
    inp=input("What can I do for you? : ")
    if ("setup" in inp):
        if("namenode" in inp) or ("name node" in inp) or ("master" in inp):
            n=0
        elif("datanode" in inp) or ("data node" in inp) or ("slave" in inp):
            n=1
        else:
            node=input("Which node do you want to setup?")
            while True:
                if("namenode" in node) or ("name node" in node) or ("master" in node):
                    n=0
                    break
                elif("datanode" in node) or ("data node" in node) or ("slave" in node):
                    n=1
                    break
                else:
                    print("Invalid choice.")
                    node=input("please enter again(datanode/namenode)?:")
        print(n)
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
                    text1('hdfs://{}:9001'.format(ip))
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
            else:
                os.system("figlet  Namenode Start error")
                    
        else:
            os.system("hadoop-daemon.sh start datanode")
            os.system("figlet  Datanode started")
         
    

    elif("bye" or "exit" or "quit" in inp):
        os.system('tput setaf 7')
        break

