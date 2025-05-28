import os
import platform
import argparse
import subprocess
# Collect all platform info like OS name, release, version, machine type,  hostname and architecture.Save it in system_info.txt.
with open('system_info.txt', 'w') as f:
    # OS Information
    f.write(f"Name: {platform.system()}\n")
    f.write(f"Version: {platform.version()}\n")
    f.write(f"Release: {platform.release()}\n")
    f.write(f"machine type: {platform.uname().system}\n")
    f.write(f"hostname: {platform.uname().node}\n")
    f.write(f"architecture: {platform.uname().machine}\n")

# Ping google.com and save the output to ping_log.txt.
os.system('ping -t 5 google.com > ping_log.txt')

# Check the running process and parse output to find if nginx, python, or mysqld is running,
os.system('ps -elf | grep -e nginx -e python -e mysqld')

# Write a script that accepts two numbers as arguments and prints their sum.
a=int(input())
b=int(input())
print(f"sum is {a+b}")

# Pass log file path and number of lines to read from end: python tail.py myapp.log 10
#python3.10 python.py --file_path=myapp.log --lines=10
parser=argparse.ArgumentParser()
parser.add_argument("--file_path",required=True)
parser.add_argument("--lines",required=True)
args=parser.parse_args()
lines=args.lines
file_path=args.file_path
line="-"+str(lines)+"f"
subprocess.run(['tail', f'{line}',f'{file_path}'])

# You can use platform, subprocess and sys modules for completing todays tasks.