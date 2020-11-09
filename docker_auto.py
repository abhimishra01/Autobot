#!/usr/bin/python3
import os 
os.system('clear')
os.system("tput setaf 2")
os.system('figlet Docker Automation')
inp = input('What Can I Do for you : ')
if ((('run' in inp) or ('launch' in inp)) and (('container' in inp) or ('Operating system' in inp) or ('os' in inp))):
    os.system("tput setaf 3")
    container_name= input('Please tell what will be the name of container? : ')
    os.system('espeak-ng Please tell what will be the name of container?')
    os.system("tput setaf 2")
    image_name = input('Which Image name you would like to use? : ')
    image_version = input('Which version of the {} image you want to use? : '.format(image_name))
    os.system('docker ps | grep {}:{} > /dev/null'.format(image_name,image_version) )
    if os.system('echo #?')==0:
        os.system("tput setaf 5")
        print('Just a sec Launching your Docker container........')
        os.system('docker run -it  --name {0} {1}:{2}'.format(container_name, image_name, image_version))  
        os.system("tput setaf 1")
        print('Stopped the Docker container........')
        os.system("python3 auto.py")
    else:
         print("Image Unavailable Pulling the image from Docker Hub")
         os.system("espeak-ng Image Unavailable Pulling the image from Docker Hub")
         os.system("docker pull {}:{}".format(image_name,image_version))
elif((('webserver' in inp) or ('httpd' in inp ) or ('apache' in inp)) and (('run' in inp) or ('container' in inp ) or ('docker' in inp))):
        os.system("tput setaf 3")
        container_name= input('Please tell what will be the name of container? : ')
        os.system('espeak-ng Please tell what will be the name of container?')
        os.system("tput setaf 2")
        os.system('netstat -tnlp')
        port= input('Please input the port Number on which your Webserver will run : ')
        path= input('Please Input the path of your webserver file : ')
        os.system('docker ps | grep centos:latest > /dev/null' )
        if os.system('echo #?')==0:
            os.system("tput setaf 5")
            print('Just a sec Launching your Docker container........')
            os.system('docker run -dit   -p {1}:80    --name {0} centos'.format(container_name,port))
            os.system("docker exec {} yum install httpd -y > /dev/null".format(container_name))
            print('Please Wait while we are configuring the webserver for you...!')
            os.system("docker cp {0} {1}:/var/www/httpd/".format(path,container_name))
            os.system('docker exec  {} /usr/sbin/httpd'.format(container_name))
            os.system("tput setaf 3")
            os.system('figlet Launched Webserver on Port {}'.format(port))
            


else:
    exit()
