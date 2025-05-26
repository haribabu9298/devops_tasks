import os 
# List all files and directories in a given path
path="/Users/hgunupur/Downloads/devops_tasks"
print(os.listdir(path))

# Delete a file or directory
os.remove("hari.txt")
os.rmdir("hari")

# Print all environment variables
print(os.environ)

# Set a custom environment variable, DB_ADMIN as user(Extract user from environment variables)
os.environ['user']='DB_ADMIN'
print(os.environ.get('user'))

# Install curl using os module
os.system('sudo apt update && sudo apt install curl')

# Create a script that checks disk usage by calling df -h using os module
os.system('df -h')