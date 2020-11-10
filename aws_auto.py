import os
import getpass
os.system('tput setaf 5')
os.system('clear')
os.system('figlet AWS CLI ')
os.system('tput setaf  3')
print(""" Press 1 : To Login in AWS
 press 2 : Describe All Instances
 press 3 : To Create New Key-Pair
 press 4 : To Create New Security Group
 Press 5 : To Create a Volume
 Press 6 : extract subnet id
 Press 7 : launch a Instance (aws linux)
 Press 8 : start instance
 Press 9 : stop instance
 Press 10 : Attach volume with instance
 Press 11 : For Partitioning the attached volume
 Press 12 : configure Web Server
 Press 13 : Format Partition
 Press 14 : Mount the Web Server to Volume
 Press 15 : create a S3 Bucket
 Press 16 : Upload a local file(or image) to the s3 bucket
 Press 17 : create CloudFront Distribution using origin as S3 Object-url
 Press 18 : Enter S3 bucket name
 Press 19 : Exit
""")	
os.system('tput setaf 2')
while True:
    ch = input("Enter your Choice :-  ")
    print(ch)
    if int(ch)== 1:
        os.system("aws configure")
        os.system('sleep 2')
        os.system('python3 aws_auto.py')
    if int(ch)==2:
        os.system("aws ec2 describe-instances")
        os.system('sleep 4')
        os.system('python3 aws_auto.py')
    if int(ch) == 3:
        key_name = input("Enter Key-Pair Name :")
        os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
        os.system('sleep 4')
        os.system('python3 aws_auto.py')
    if int(ch) == 4:
        sg_grp = input("Enter Security Group Name : ")
        des = input("Enter Security Group Description : ")
        os.system("aws ec2 create-security-group --group-name {} --description {}".format(sg_grp,des))
        os.system('sleep 4')
        os.system('python3 aws_auto.py')
    if int(ch) == 5:
        vol = input("Enter Volume Size : ")
        az = input("Enter Availability Zone : ")
        os.system("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone {}".format(vol,az))
        os.system('sleep 4')
        os.system('python3 aws_auto.py')
    if int(ch) == 6:
        os.system("aws ec2 describe-subnets --query Subnets[0].[SubnetId]")
        os.system('sleep 4')
        os.system('python3 aws_auto.py')
    if int(ch) == 7:
        print("""
                 Press 1:AWS Linux
                 Press 2:Redhat Linux
                    """)
        os.system('sleep 5')
        os.system('python3 aws_auto.py')
        print("Enter your Choice :  ",end="")
        img=input()
        if int(img) ==1:
            key = input("Enter your key:-")
            subnet = input("Enter subnet id:-")
            sg_grp = input("Enter your security grp:-")
            os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --subnet-id {} --instance-type t2.micro --key-name {} --security-group-ids {} --count 1".format(subnet,key,sg_grp))
            os.system('sleep 4')
            os.system('python3 aws_auto.py')
        if int(img) == 2:
            key = input("Enter your key:-")
            subnet = input("Enter subnet id:-")
            os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --subnet-id {} --instance-type t2.micro --key-name {} --security-group-ids {} --count 1".format(subnet,key,sg_grp))
            print("Successfully launched instance!")
            os.system('sleep 4')
            os.system('python3 aws_auto.py')
    if int(ch) == 8:
        sti = input("Enter Instance Id:- ")
        os.system(" aws ec2 start-instances --instance-id {}".format(sti))
        os.system('sleep 3')
        os.system('python3 aws_auto.py')
    if int(ch) == 9:
        spi = input("Enter Instance Id :- ")
        os.system(" aws ec2 stop-instances --instance-id {}".format(spi))
        os.system('sleep 2')
        os.system('python3 aws_auto.py')
    if int(ch) == 10:
        size = input("Enter Size :- ")	
        zone = input("Enter availability zone :- ")
        vtype = input("Enter volume type :- ")
        os.system(" aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(zone,size,vtype))
        os.system('sleep 4')
        os.system('python3 aws_auto.py')
    if int(ch) == 11:
        os.system("tput setaf 3")
        print("\t\t\tVolume Zone & Instance Zone Must be same !!!")
        print("\t\t\t--------------------------------------------")
        os.system("tput setaf 7")
        print("Enter volume-id : ",end = "")
        vid = input()
        print("Enter instance-id : ",end = "")
        iid = input()
        print("Enter device : /dev/",end= "")
        device = input()
        os.system(" aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(vid,iid,device))
        os.system('sleep 4')
        os.system('python3 aws_auto.py')
    if int(ch) == 12:
        print("Enter IP : ",end = "")
        ip = input()
        print("Enter key : ",end = "")
        key = input()
        print("Enter device : /dev/",end= "")
        device = input()
        os.system(" ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/{} ".format(ip,key,device))
        os.system('sleep 3')
        os.system('python3 aws_auto.py')
    if int(ch) == 13:
        os.system("tput setaf 3")
        print("\t\t\tHTTPD must be installed...")
        print("\t\t\t--------------------------")
        os.system("tput setaf 7")
        print("Enter IP : ",end = "")
        ip = input()
        print("Enter key : ",end = "")
        key = input()
        os.system(" ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(ip,key))
        os.system('sleep 3')
        os.system('python3 aws_auto.py')
    if int(ch) == 14:
        print("Enter IP : ",end = "")
        ip = input()
        print("Enter key : ",end = "")
        key = input()
        print("Enter Device : /dev/",end="")
        device = input()
        os.system(" ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{} ".format(ip,key,device))
        os.system('sleep 3')
        os.system('python3 aws_auto.py')
    if int(ch) == 15:
        print("Enter IP : ",end = "")
        ip = input()
        print("Enter key : ",end = "")
        key = input()
        print("Enter Device : /dev/",end="")
        device = input()
        os.system(" ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html/ ".format(ip,key,device))
        os.system('sleep 3')
        os.system('python3 aws_auto.py')
    if int(ch) == 16:  
        print("Enter region : ",end = "")
        region_name = input()
        print("Enter your bucket name: ",end ="")
        bname= input()
        os.system(" aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration 					LocationConstraint={}".format(bname,region_name,region_name))
        os.system('sleep 4')
        os.system('python3 aws_auto.py')
    if int(ch) == 17:
        print("Enter local file path: ",end ="")
        path = input()
        print("Enter your s3 bucket name: ",end= "")
        bname = input()
        os.system(" aws s3 sync {} s3://{} ".format(path,bname))
        os.system('sleep 4')
        os.system('python3 aws_auto.py')
    if int(ch) == 18:
        print("Enter your s3 bucket name: ",end= "")
        bname = input()
        print("Enter region where s3 create a bucket (such as ap-south-1): ",end = "")
        region_name = input()
        os.system(" aws cloudfront create-distribution --origin-domain-name {}.s3.{}.amazonaws.com ".format(bname,region_name))
        os.system('sleep 4')
        os.system('python3 aws_auto.py')
    if int(ch) == 19:
        os.system('clear')
        exit()
    else:
        print("\t\t\t -----------------------------")
        os.system("tput setaf 3")
        print("\t\t Invalid Input..!! You are exited from the Menu")
        os.system("tput setaf 7")
        print("\t\t\t -----------------------------")
        exit()
                
