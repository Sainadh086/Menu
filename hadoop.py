import subprocess, os

def hadoop(service_no, data):

    # creating inventory file
    if data['passw'][-4:]  == '.pem' :
        inv = f"{data['ip']} ansible_user={data['user']} ansible_ssh_private_key_file={data['passw']}" #for inventory
    else:
        inv = f"{data['ip']} ansible_user={data['user']} ansible_ssh_pass={data['passw']}"

    inv_file = open("ip.txt","w")
    inv_file.write("[hadoop]\n")
    inv_file.write(inv)
    inv_file.close()
    try: 
        if service_no == 1:
            #configure namenode/master
            out = subprocess.getoutput("ansible-playbook playbooks/master-hadoop.yml")
        elif service_no == 2:
            #configure datanode/slave
            out = subprocess.getoutput(f"ansible-playbook playbooks/slave-hadoop.yml -e master_ip={data['master_ip']}")
        elif service_no == 3:
            #configure client
            out = subprocess.getoutput("ansible-playbook playbooks/client-hadoop.yml")
        elif service_no == 4:
            #start namenode 
            out = subprocess.getoutput("ansible hadoop -m shell -a 'sudo hadoop-daemon.sh start namenode'")
        elif service_no == 5:
            #start datanode
            out = subprocess.getoutput("ansible hadoop -m shell -a 'sudo hadoop-daemon.sh start datanode'")
        elif service_no == 6:
            #connected devices
            out = subprocess.getoutput("ansible hadoop -m shell -a 'sudo hadoop dfsadmin -report'")
            return {"status" : "Successfull", "Output" : out}
        return out
    except:
        return "failed"


        
