import psutil
import requests
import json
import os
# Print current CPU usage percentage.
print('The CPU usage is: ', psutil.cpu_percent(interval=2))

# List all running processes.
# for pid in psutil.pids():
#     print(psutil.Process(pid))

# Show total, used, free, and percentage disk usage .
print(psutil.disk_usage('/'))

# Display network I/O stats.
print(psutil.net_io_counters(pernic=True))

# Fetch https://example.com and display headers including content-type, server, etc.
r=requests.get('https://example.com',verify=False)
for header,value in r.headers.items():
    print(f"{header} is {value}")

# Use your github user api like https://api.github.com/users/haribabu9298, Extract and print name, public repos, followers.
user=os.getenv('user')
password=os.getenv('password')

def convert_bytes_to_json_str(byte_data):
    json_str = byte_data.decode('utf-8')
    user_data = json.loads(json_str)
    return user_data

response=requests.get('https://api.github.com/users/haribabu9298',verify=False,auth=(user,password))
#convert bytes to json
user_data=convert_bytes_to_json_str(response.content)
print("Login name is ",user_data['login'])

response=requests.get('https://api.github.com/users/haribabu9298/followers',verify=False,auth=(user,password))
# convert bytes to json
user_data=convert_bytes_to_json_str(response.content)
for i in range(len(user_data)):
    print("follower user id is :",user_data[i]['login'])


response=requests.get('https://api.github.com/users/haribabu9298/repos',verify=False,auth=(user,password))
# convert bytes to json
user_data=convert_bytes_to_json_str(response.content)
for i in range(len(user_data)):
    if not user_data[i]['private'] == 'True':
        print("public repo name is ",user_data[i]['name'])



# You can use psutil and requests module for completing above tasks.