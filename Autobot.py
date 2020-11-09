#!/usr/sbin/python3
import os 
os.system('clear')
os.system('tput setaf  4')
os.system('yum list | grep yattag  >  /dev/null ')
os.system('clear')
print('Please wait while we are resolving dependencies....!')
if os.system('echo $? > /dev/null')!=0:
    os.system("rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm")
    os.system("yum install figlet -y")
os.system("pip3 list| grep yattag > /dev/null")
if os.system('echo $?')!=0:
    os.system("pip3 install yattag")
os.system('clear')
os.system('tput setaf  6')
os.system('figlet  Welcome to Autobot:- The Automation tool')
os.system('tput setaf  2')
print('''This automation tool is an integration of 5 Different Technologies:-
Linux Operating System--Docker Container Engine--Hadoop Cluster--Amazon Web Services Command Line Interface ''')
os.system('tput setaf 3')
print('This program is capable of making things way easier and handy to make your workcycle faster and efficient ')
os.system('tput setaf  5')
print(''' 
    Hadoop Cluster
    AWS CLI 
    Docker
''')
while True:
    inp=input('Please input the name of technology in which you need to implement this tool : ')
    if ((('Hadoop' in inp) or ('hadoop' in inp) or ('bigdata in hadoop')) and (('cluster' in inp) or ('Cluster' in inp))):
        os.system('python3 hadoop.py')
    elif ((('aws' in inp) or ('AWS' in inp) or ('Amazon' in inp) or ('Aws' in inp) or ('AWs' in inp)) and (('cli' in inp) or ('CLI' in inp))):
        os.system('python3 aws_auto.py')
    elif ((('Docker' in inp) or ('docker' in inp) or ('container' in inp) or ('engine' in inp) or ('DOCKER' in inp)) and (('Container' in inp ) or ('container' in inp))):
        os.system(' python3 docker_auto.py')
    elif (('exit' in inp) or ('bye' in inp) or ('break' in inp) or ('goodbye' in inp) or ('shutdown' in inp) or ('tata' in inp)):
        break


                


