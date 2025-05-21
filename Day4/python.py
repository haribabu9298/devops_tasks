# Create a list of server names (e.g., "web1", "db1", "cache1"). Loop through the list and print a message like: "Pinging web1... OK"
l1=[ "web1", "db1", "cache1"]
for server in l1:
  print(f"Pinging {server}... OK")

# Given a list of disk usages [40, 70, 90, 55] (in %), write a script that checks each and prints whether it’s under or over the threshold (e.g., 80%).
l1=[40, 70, 90, 55]
for disk in l1:
  if disk<80:
    print(f"disk usage {disk}% is under threshold")
  else:
    print(f"disk usage {disk}% is over threshold")

# Store a tuple of running service names (e.g., ("nginx", "docker", "ssh")). Print the second service and convert it to a list to add service "kubernetes".
t=("nginx", "docker", "ssh")
print(f"second service name is {t[1]}")
l=list(t)
l.append("kubernetes")
print(f"all service names are {l}")

# Create a dictionary "config" that holds a server's configurations:  hostname = web1, ip = 192.168.1.10, port =  80. Print each key and value in a readable format.
mydict = {
    "hostname" :"web1",
    "ip": "192.168.1.10",
    "port": "80"
}
for key,value in mydict.items():
    print(f"{key} is {value}")

# You have a list of IP addresses with duplicates. Display the unique IP's (Hint: You can use set).
ips=["0.0.0.0","0.0.0.0"]
print(set())

# Define two sets: web_servers and db_servers. Perform and print: Servers common to both, Servers only in web, All unique servers.
web_servers=["1.1.1.1","3.3.3.3","5.5.5.5","6.6.6.6"]
db_servers=["1.1.1.1","2.2.2.2","4.4.4.4","6.6.6.6"]
common=list(set(web_servers) & set(db_servers))
print(common)
only_web=set(web_servers)-set(db_servers)
print(only_web)
unique=list(set(web_servers) | set(db_servers))
print(unique)
