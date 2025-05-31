import maskpass
import base64
import requests
import json
# Input a password from user. Prevent the entered password from being displayed on the screen. Encrypt it using base64 and store it locally in a text file.
pwd = maskpass.askpass()
encoded_base64=base64.b64encode(pwd.encode("UTF-8")) #converting to byte and then to base64
print(encoded_base64)
with open("encode.txt",'w') as fw:
    fw.write(encoded_base64.decode("UTF-8")) #decoding back to string from byte for writing inside file only allows str 


# Input password from user in the same manner, check the password by decrypting password saved in text file. Display success message if  password is correct.
pwd=maskpass.askpass()
with open("encode.txt",'r') as fr:
    byte_encoded=fr.read().encode("UTF-8") #encoding str to bytes
    base64_decoded=base64.b64decode(byte_encoded) #decoding bytes to base64
    pass_str=base64_decoded.decode("UTF-8") #decoding bytes to str
if pass_str==pwd:
    print("password is correct")
else:
    print("password is incorrect")



# Use json.dumps() to log deployment data (e.g., timestamps, status, host) in a structured format.
deployment_list=[]
deployment_data1={
    "timestamp": "31-05-2025-12-12-12",
    "status": "success",
    "host": "ibm.com"
}
deployment_list.append(deployment_data1)
deployment_data2={
    "timestamp": "30-05-2025-13-13-13",
    "status": "failure",
    "host": "ibm.com"
}
deployment_list.append(deployment_data2)
print(json.dumps(deployment_list,indent=3))


# Use requests.get() to hit API: https://jsonplaceholder.typicode.com/users and extract values from the JSON response using the json module.
response=requests.get("https://jsonplaceholder.typicode.com/users",verify=False)
json_data=response.json()
for user in json_data:
    print(f"user id is {user['id']} and username is {user['name']}")


# Write a function to check required keys ("host", "port", "auth") in a JSON config file.
with open("config.json",'r') as fr:
    json_data=json.loads(fr.read())
for key,value in json_data.items():
    print(f"host for {key} is {value['host']} , port is  {value['port']} and auth is {value['auth']} ")