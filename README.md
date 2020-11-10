                                             AutoBot Installation Documention:-

•	Introduction:-

o	Autobot is a Terminal User Interface Automation program made with Python Programming Language and build on concepts of Integration of Technologies for the sake of making Automation as much as possible.

o	Currently Autobot  Version 1.0  is having capability of providing automation to five different technologies:-

	Centos/Redhat Enterprise Linux Operating System

	Docker Container Engine.

	Amazon Web Services :- Command Line Interface.

	Hadoop Cluster.

	Python Programming Language.

•	Use-Case:-

o	In today’s world of rapidly expanding and evolving technologies we can see automation is getting dominant in each and every sector.

o	So we can find the Use Cases of Autobot in lots of areas. For Example:

	The Configuration of Namenode and Datanodes in a Hadoop Cluster is a very hectic task. Sys-Admins have to give lots of time just to configure and write the XML files of hadoop configuration directory.

	The current version of Autobot is capable enough to set your hadoop’s ‘hdfs-site.xml’ & ‘core-site.xml’ automatically just by providing inputs of master’s ip address, the directory to be shared in hadoop cluster and that’s all. All the formatting and configuration of namenode or datanode will be done accordingly by own.

	Our team is planning to make sure the upcoming versions of Autobot would be capable of provide automation in configuring each and every configuration files of hadoop cluster , Kubernetes cluster, Jenkins, ELK stack and other Devops tools.

•	How to use:-

o	Firstly you need to clone this repository in your Redhat Enterprise Linux Version 8.0 Operating system.

o	You can use github cli for this. If you don’t have Github CLI available in your operating system, you can install it by running the following commands on your terminal:-

	dnf config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo

	dnf install gh –y

o	Secondly you will need Python Version3 i.e python3 Interpreter to run this software.

o	In case python3 unavailable in your RHEL 8.0 Operating System you can download using the following command:-

	dnf install python36 -y

o	After cloning the repository you can goto the folder and run the ‘Autobot.py’ with python3 interpreter (python3 Autobot.py).

o	After that you will be displayed the Home-UI of the software and you will be asked to provide the name of technology in which you need implement automation.


	Here is a brief manual of using the particular options:-

	Hadoop Cluster:-

	You can firstly Input the word ‘Setup’ so the software will understang we need the hadoop configuration to be done.

	The you will be asked to input which node to setup i.e Namenode or Datanode and you can select them accordingly.

	Then you can input the name of directory to be shared in the cluster and the ip address of the Namenode accordingly. In the background everything will be get ready 
with starting of hadoop namenode/datanode.

	Docker Container Engine:-

	You can input whatever desire you need to fulfil through this program for example if you need to see the available images , you can input “show available images” for the same.

	If you  need to launch a container or webserver, you can input the same requirement accordingly ‘I want to launch a container’ or ‘I want to launch a webserver in a container’ accordingly.

	Everything from PATing to copying your website file will be done automatically and you will be given a webserver running on top of a centos docker container with your desired port.

	You can also input requirements such as ‘remove/terminate all containers’ or ‘remove a container’ accordingly.


	AWS CLI :-

	When you will select this category for automation you will find a list of available options with multiple different Services provided by AWS.

	The services include EC2, EBS, S3 Bucket, Cloudfront, etc,.

	You can accordingly select the options as per your requirements and you will be redirected to all set of instructions and inputs on the way accordingly.

	Soon our team members are working to implement some more Cloud Computing services in this software.

                                                                           Developers:-

                                                                                                           	Abhishek Mishra 
                                                                      
                                                                                                           	Deepali Ghadia

                                                                                                           	Snehal Shinde

                                                                                                           	Aishwarya Birla
    
                                                                                                           	Rahul Kashyap

                                                                                                                                                         

