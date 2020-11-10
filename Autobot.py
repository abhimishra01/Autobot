import os 
os.system('clear')
while True:
    os.system('tput setaf  1')
    os.system('figlet  Autobot: The Automation Tool')
    os.system('tput setaf  2')
    print('Autobot is capable of making your workcycle easier ,faster &  efficient ')
    os.system('tput setaf  5')
    print(''' 
        Hadoop Cluster
        AWS CLI 
        Docker 
        ''')
    os.system('tput setaf 3')
    inp=input('Please input the name of technology among above : ')
    if ((('Hadoop' in inp) or ('hadoop' in inp) or ('bigdata in hadoop')) and (('cluster' in inp) or ('Cluster' in inp))):
        os.system('python3 hadoop.py')
    elif ((('aws' in inp) or ('AWS' in inp) or ('Amazon' in inp) or ('Aws' in inp) or ('AWs' in inp)) and (('cli' in inp) or ('CLI' in inp))):
        os.system('python3 aws_auto.py')
    elif ((('Docker' in inp) or ('docker' in inp) or ('container' in inp) or ('engine' in inp) or ('DOCKER' in inp))):
        os.system(' python3 docker_auto.py')
    elif ((('install' in inp) or ('resolve' in inp)) and ( ('dependencies' in inp) or ('requirements' in inp))):
        os.system('python3 dependencies.py')
    elif (('exit' in inp) or ('bye' in inp) or ('break' in inp) or ('goodbye' in inp) or ('shutdown' in inp) or ('tata' in inp)):
        break


os.system('tput setaf 7')
                


