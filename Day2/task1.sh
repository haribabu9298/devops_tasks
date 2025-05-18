#clone from https://github.com/logpai/loghub/blob/master/Linux/Linux_2k.log
#grep error 
cat Linux_2k.log | grep error

#using awk cmd to print time stamp , loglevel
cat Linux_2k.log | awk '{print $1 $2 " " $4}'

#use sed cmd to replace ip with string
sed -E 's/([0-9]{1,3}\.){3}[0-9]{1,3}/d[REDACTED_IP]/g' Linux_2k.log