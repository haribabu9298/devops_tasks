# *DAILY TASK *

# Automate Backups with Shell Scripting

# Write a shell script to back up /devops_workspace as backup_$(date +%F).tar.gz.
# Save it in /backups and schedule it using cron.
# Make the script display a success message in green text using echo -e.
GREEN='\033[0;32m'
NC='\033[0m' # No Color
tar -cvzf backups/backup_$(date +%F).tar.gz devops_workspace
echo -e "${GREEN}Took backup sucessfully"

# create crontab
# crontab -e
# 2 * * * * /Users/hgunupur/Downloads/devops_tasks/Day2/task4.sh

# list corntabs running on system
# crontab -l
# 2 * * * * /Users/hgunupur/Downloads/devops_tasks/Day2/task4.sh