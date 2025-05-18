#Volume Management & Disk Usage
#attching loop device filesystem to /mnt/devops_data
#Create a large regular file on disk that will be used to create the loop device
sudo dd if=/dev/zero of=/root/virtual.ext4 bs=1M count=100
100+0 records in
100+0 records out
104857600 bytes (105 MB, 100 MiB) copied, 0.0876149 s, 1.2 GB/s

#check for available loop device 
losetup -f
/dev/loop14

#we can use /dev/loop14 for loop device 
losetup /dev/loop14 /root/virtual.ext4

#Create an ext4 filesystem using /dev/loop14
mkfs -t ext4 -v /dev/loop14

#mount loop device to mount path
sudo mount -o loop /dev/loop14 /mnt/devops_data

#check the mount 
df -h

#detach loop device
umount  /mnt/devops_data
losetup -d /dev/loop14