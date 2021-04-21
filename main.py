# This python file implements CLI(Command Line Interface)

import os, subprocess
from hadoop import hadoop

def index():
    # all the available services
    data = {
        "hadoop": [
            "Install Hadoop Name Node(Master)",
            "Install Hadoop Data Node(Slave)",
            "Install Client",
            "Start Name Node",
            "Start Data Node",
            "See connected devices"
        ],

        "docker" : [
            "Install Docker",
            "Start a Container with Custom Image",
            "Running Containers",
            "List Images",
            "Stop a container"
        ],

        "linux" : [
            "Install Software",
            "Start Service",
            "Stop Service",
            "Basic linux commands"
        ],
        "aws" : [
            "Start EC2 instance",
            "Upload files to S3",
            "Stop EC2 instance"
            ]
    }
    return data



def main_menu():
    c = 1
    data = index()
    
    #technology
    tech_list = list(data)
    print("Technologies that you can implement in few clicks \n")
    for i in data.keys():
        print(f" Press {c} for {i} \n")
        c += 1
    tech_choice = int(input("Enter your choice : ")) # select technology of your choice
    tech = tech_list[tech_choice-1]

    #service
    svc = data[tech]
    c = 1
    print("\n All the availble services for {tech} \n")
    for i in svc:
        print(f" Press {c} to {i} \n")
        c += 1
    service_no = int(input("Choose from one of the above service : ")) # select service of a technology

    print("\n Enter the below details to processed further \n")

    remote = input("Your using AWS instance 0/1(0-> false, 1 -> True) : ")
    ip_detail = input("Enter your system user and IP eg:- ec2-user@132.168.15.55 : ")
    ip_detail = ip_detail.split('@')
    user = ip_detail[0]
    ip = ip_detail[1]
    passw = input("Enter the your VM password or key file : ")

    user_data = { "user" : user, "ip" : ip, "remote" : remote, "passw": passw}

    try:
        # dict key is equal to function name
        output_data = eval(tech+f"(service_no = {service_no}, data = {user_data})") #executing the function
        return output_data
    
    except:
        output_data = {"Status": "Failed", "Remarks" : "Tech Stack Doens't exist"}
        return output_data

    return "Add more"


