import os
# Create a script that writes the following lines to a file named log.txt
# Server started at 10:00 AM
# Health check passed
# Backup completed
file_name="log.txt"
with open(file_name,'w') as fw:
    fw.write('''Server started at 10:00 AM
Health check passed
Backup completed''')

# Read the contents of log.txt and print each line with line numbers prefixed like:
# 1: Server started at 10:00 AM
with open(file_name,'r') as fr:
    l=list(fr.read().split("\n"))
i=1
for line in l:
    print(f"{i}: {line}")
    i+=1
# Append a new entry like "Deployment completed at 11:00 AM" to log.txt.
with open(file_name,'a') as fa:
    fa.write("\nDeployment completed at 11:00 AM")

# Check if a file named config.ini exists. If not, create it and write default content:
# [server]
# port=8080
config_file="config.ini"
if not os.path.isfile(config_file):
    with open(config_file,'w') as fw:
        fw.write('''[server]
port=8080''')

# Read the config.ini file and extract the port number using Python.
with open(config_file,'r') as fr:
    print(fr.read().split("\n")[1].split("=")[1])
# Write a script that deletes a file temp.txt only if it exists. If it doesn’t, print a warning.
if os.path.exists("temp.txt"):
    os.remove("temp.txt")
else:
    print("warning")