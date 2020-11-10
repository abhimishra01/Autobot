import os
os.system('tput setaf 3')
print('Please  wait while we are resolving dependencies....!')
os.system("rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm")
os.system("dnf install figlet -y")
os.system("pip3 install yattag")
os.system('clear')
os.system('tput setaf 7')
