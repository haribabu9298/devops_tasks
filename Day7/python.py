# *Create a Python script that analyzes Linux_2k.log and produces a report showing:*
# *Export summary to linux_log_report.txt

# Logfile Link: https://github.com/logpai/loghub/blob/master/Linux/Linux_2k.log

import re
# *Total number of log entries
with open("Linux_2k.log",'r') as fr:
    n=len(fr.read())
    with open("linux_log_report.txt", 'w') as fw:
        fw.write(f"Total no of log entries {n}\n")


# *Number of failed login attempts
pattern="failure"
count=0
file=open("Linux_2k.log",'r')
for line in file:
    if re.search(pattern,line):
        count+=1
with open("linux_log_report.txt", 'a') as fa:
    fa.write(f"no of failed log attempts {count}\n")



# *IPs with most failed attempts
pattern="failure"
l1=[]
my_dict={}
#max=0
file=open("Linux_2k.log" , 'r')
for line in file:
    if re.search(pattern,line):
        if line.split(" ")[12].split("=")[1].strip():
            l1.append(line.split(" ")[12].split("=")[1])
# for ip in set(l1):
#     c=0
#     for l1_ip in l1:
#         if ip == l1_ip:
#             c+=1
#     if c>max:
#         max=c
#         ip_max=ip
# print(max,ip_max)

for ip in set(l1):
    c=0
    for l1_ip in l1:
        if ip == l1_ip:
            c+=1
    my_dict[ip]=c
with open("linux_log_report.txt", 'a') as fw:
    fw.write(f"IPs with most failed attempts is {max(my_dict, key=my_dict.get)}")
